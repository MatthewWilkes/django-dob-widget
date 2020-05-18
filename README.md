# django-dob-widget

[![Build Status](https://travis-ci.org/MatthewWilkes/django-dob-widget.svg?branch=master)](https://travis-ci.org/MatthewWilkes/django-dob-widget)


A Django date widget optimised for usability in entering dates of birth.

This is based on the guidelines put forward by the UK Government Digital Service at https://designnotes.blog.gov.uk/2013/12/05/asking-for-a-date-of-birth/

Usage:

    from django import forms
    from dobwidget import DateOfBirthWidget
    
    class PersonModelForm(forms.ModelForm):
        """
        Model form for people.
        """
        
        class Meta(object):
            model = Person
            fields = ['name', 'date_of_birth']
            widgets = {
                'date_of_birth': DateOfBirthWidget(),
            }
      

The DateOfBirthWidget can take an optional order parameter, to make it useful in non-UK jurisdictions:

  
        class Meta(object):
            model = Person
            fields = ['name', 'date_of_birth']
            widgets = {
                'date_of_birth': DateOfBirthWidget(order='MDY'),
            }


## Changes

### 1.2.0

* Add support for Django 1.10

### 1.1.3

* Handle far future dates that raise OverflowError when given to datetime.date

### 1.1.2

* Do not clear inputs if an invalid date is entered

### 1.1.1

* Bug fix around character-based input

### 1.1.0

* Allow attrs of the individual subwidgets to be set using day_attrs, month_attrs and year_attrs.

### 1.0.0

* Initial release

## Contributors

* "Matthew Wilkes" <matt@matthewwilkes.name>
* "Martin Sanders" <martin@forwardpartners.com>
