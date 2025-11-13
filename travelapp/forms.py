from django import forms
from .models import Enquiry

COUNTRIES = [
    ('', 'Select your country'),
    ('AF', 'Afghanistan'),
    ('AL', 'Albania'),
    ('DZ', 'Algeria'),
    ('AS', 'American Samoa'),
    ('AD', 'Andorra'),
    # Add more countries here
    ('ZW', 'Zimbabwe'),
]

class EnquiryForm(forms.ModelForm):
    your_country = forms.ChoiceField(
        choices=COUNTRIES, 
        label='Your Country', 
        widget=forms.Select(attrs={'placeholder': 'Select your country'})
    )
    no_of_days = forms.IntegerField(
        min_value=1, 
        label='No of days', 
        widget=forms.NumberInput(attrs={'placeholder': 'Enter number of days'})
    )
    no_of_adults = forms.IntegerField(
        min_value=1, 
        label='No. of Adults', 
        widget=forms.NumberInput(attrs={'placeholder': 'Enter number of adults'})
    )
    no_of_children = forms.IntegerField(
        min_value=0, 
        label='No. of children', 
        widget=forms.NumberInput(attrs={'placeholder': 'Enter number of children'})
    )

    class Meta:
        model = Enquiry
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter your name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email'}),
            'contact_number': forms.TextInput(attrs={'placeholder': 'Enter your contact number'}),
            'dest_name': forms.Select(attrs={'placeholder': 'Select destination'}),  # Use Select widget here
            'message': forms.Textarea(attrs={'placeholder': 'Enter your message'}),
            'your_country': forms.Select(attrs={'placeholder': 'Select your country'}),
        }
