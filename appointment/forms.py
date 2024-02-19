from typing import Any, Mapping
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList

from .models import Calendar, Appointment, Attendee, Availability
from django.forms import formset_factory, modelformset_factory

from account.models import Service

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
                "class": "form-check-input"
            },
        ),
    )

    require_confirmation = forms.BooleanField(
        required=False,
        label="confirmation nécessaire",
        widget=forms.CheckboxInput(attrs={"class": "form-check-input"})
    )

    class Meta:
        model = Calendar
        fields = ["appointments_limit_per_day", "active", "require_confirmation"]


class CreateAppointmentForm(forms.ModelForm):
    # calendar_id = None

    # def __init__(self, calendar_id: int, data: Mapping[str, Any] | None = ..., files: Mapping[str, File] | None = ..., auto_id: bool | str = ..., prefix: str | None = ..., initial: dict[str, Any] | None = ..., error_class: type[ErrorList] = ..., label_suffix: str | None = ..., empty_permitted: bool = ..., instance: Model | None = ..., use_required_attribute: bool | None = ..., renderer: Any = ...) -> None:
    #     self.calendar_id = calendar_id
    #     super().__init__(data, files, auto_id, prefix, initial, error_class, label_suffix, empty_permitted, instance, use_required_attribute, renderer)

    service = forms.ModelChoiceField(
        queryset=Service.objects.filter(user__calendar=1),
        required=False,
        label="Service",
        widget=forms.Select(attrs={"class": "form-select", "size": 10})
    )

    date = forms.DateField(
        required=True,
        label="Date",
        widget=forms.DateInput(attrs={"class": "form-control", "size": 10})
    )

    start_time = forms.TimeField(
        required=True,
        label="Début",
        widget=forms.TimeInput(attrs={"class": "form-control", "size": 6})
    )

    end_time = forms.TimeField(
        required=True,
        label="Fin",
        widget=forms.TimeInput(attrs={"class": "form-control", "size": 6})
    )

    class Meta:
        model = Appointment
        fields = ["service", "date", "start_time", "end_time"]


class EditAvailabilityForm(forms.ModelForm):
    day_of_week = forms.CharField(
        required=True,
        label="Jour",
        widget=forms.Select(attrs={"class": "form-select", })
    )

    start_time = forms.TimeField(
        required=False,
        label="Début",
        widget=forms.TimeInput(attrs={"class": "form-control", "size": 6})
    )

    end_time = forms.TimeField(
        required=False,
        label="Fin",
        widget=forms.TimeInput(attrs={"class": "form-control", "size": 6})
    )

    class Meta:
        model = Availability
        fields = ["day_of_week", "start_time", "end_time"]

EditAvailabilityFormSet = modelformset_factory(
    Availability,
    # form=EditAvailabilityForm,
    fields=["day_of_week", "start_time", "end_time"],
    max_num=7,
    labels={
        "day_of_week": "Jour",
        "start_time": "Début",
        "end_time": "Fin",
    },
    widgets={
        "day_of_week": forms.Select(attrs={"class": "form-select"}),
        "start_time": forms.TimeInput(attrs={"class": "form-control", "size": 6}),
        "end_time": forms.TimeInput(attrs={"class": "form-control", "size": 6}),
    },
)

