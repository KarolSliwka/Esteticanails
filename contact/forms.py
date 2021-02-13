from django import forms


class ContactForm(forms.Form):
    """ """
    name = forms.CharField(required=True)
    from_email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=32, required=False)
    subject = forms.CharField(required=False)
    message = forms.CharField(widget=forms.Textarea, required=True)

    def __init__(self, *args, **kwargs):
        """ This function will add placeholders and classes and set autofocus on
        name field """
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Full Name',
            'from_email': 'Email Address',
            'phone_number': 'Phone Number',
            'subject': 'Subject',
            'message': 'Message',
        }

        # Change number of visible rows in textarea field
        self.fields['message'].widget.attrs = {'rows': 5}
        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
