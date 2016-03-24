# -*- coding: utf-8 -*-
from django import forms
from dobwidget import DateOfBirthWidget

from .models import Person


class PersonModelForm(forms.ModelForm):
    """
    Model form for people.
    """

    class Meta(object):
        model = Person
        widgets = {
            'date_of_birth': DateOfBirthWidget(),
        }
    

class DMYPersonModelForm(forms.ModelForm):
    """
    Model form for people in DMY areas.
    """

    class Meta(object):
        model = Person
        widgets = {
            'date_of_birth': DateOfBirthWidget(order='DMY'),
        }
    

class MDYPersonModelForm(forms.ModelForm):
    """
    Model form for people in DMY areas.
    """

    class Meta(object):
        model = Person
        widgets = {
            'date_of_birth': DateOfBirthWidget(order='MDY'),
        }
    
class YMDPersonModelForm(forms.ModelForm):
    """
    Model form for people in DMY areas.
    """

    class Meta(object):
        model = Person
        widgets = {
            'date_of_birth': DateOfBirthWidget(order='YMD'),
        }

