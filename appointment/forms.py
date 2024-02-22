from django import forms
from django.forms import BaseModelFormSet

from .models import Calendar, Appointment, Availability
from django.forms import formset_factory, modelformset_factory


class EditCalendarForm(forms.ModelForm):

    appointments_limit_per_day = forms.IntegerField(
        required=False,
        label="Rendez-vous par jour",
        widget=forms.NumberInput(attrs={"class": "form-control", "size": 10})
    )

    active = forms.BooleanField(
        required=False,
        label="Activer",
        widget=forms.CheckboxInput(
            attrs={
                "class": "form-check-input form-switch"
            },
        ),
    )

    class Meta:
        model = Calendar
        fields = ["appointments_limit_per_day", "active"]


class CreateAppointmentForm(forms.ModelForm):

    date = forms.DateField(
        required=True,
        label="Date",
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date", "size": 10})
    )

    start_time = forms.TimeField(
        required=True,
        label="Début",
        widget=forms.TimeInput(attrs={"class": "form-control", "type": "time", "size": 6})
    )

    end_time = forms.TimeField(
        required=True,
        label="Fin",
        widget=forms.TimeInput(attrs={"class": "form-control", "type": "time", "size": 6})
    )

    message = forms.CharField(
        required=True,
        label="Message",
        widget=forms.Textarea(attrs={"class": "form-control", "rows": "3"})
    )

    class Meta:
        model = Appointment
        fields = ["date", "start_time", "end_time", "message"]


# class EditAvailabilityForm(forms.ModelForm):
#     day_of_week = forms.CharField(
#         required=True,
#         label="Jour",
#         widget=forms.Select(attrs={"class": "form-select", })
#     )

#     start_time = forms.TimeField(
#         required=False,
#         label="Début",
#         widget=forms.TimeInput(attrs={"class": "form-control", "size": 6})
#     )

#     end_time = forms.TimeField(
#         required=False,
#         label="Fin",
#         widget=forms.TimeInput(attrs={"class": "form-control", "size": 6})
#     )

#     class Meta:
#         model = Availability
#         fields = ["day_of_week", "start_time", "end_time"]


class BaseAvailabilityFormSet(BaseModelFormSet):
    def __init__(self, calendar_id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.queryset = Availability.objects.filter(calendar=calendar_id)

EditAvailabilityFormSet = modelformset_factory(
    Availability,
    formset=BaseAvailabilityFormSet,
    # form=EditAvailabilityForm,
    fields=["day_of_week", "start_time", "end_time"],
    max_num=7,
    labels={
        "day_of_week": False,
        "start_time": False,
        "end_time": False,
    },
    widgets={
        "day_of_week": forms.Select(attrs={"class": "form-select", "disabled": "disabled"}),
        "start_time": forms.TimeInput(attrs={"class": "form-control", "type": "time", "size": 6}),
        "end_time": forms.TimeInput(attrs={"class": "form-control", "type": "time", "size": 6}),
    },
)

