from django import forms

from contact_form.forms import ContactForm


class CustomContactForm(ContactForm):
    number = forms.IntegerField()

    field_order = ['name', 'email', 'number', 'body']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['placeholder'] = 'Enter Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter Email'
        self.fields['number'].widget.attrs['placeholder'] = 'Enter Mobile Number'
        self.fields['body'].widget.attrs['placeholder'] = 'Enter Message'
