# django-dob-widget

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

### 1.0

Initial release

## Authors

* "Matthew Wilkes" <matt@matthewwilkes.name>

