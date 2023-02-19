from django import forms
from django.forms import ModelForm
from django import forms




class ContactForm(forms.Form):
    total_area = forms.FloatField(label='total_area', required=True)
    year = forms.FloatField(label='year', required=True)
    pledge = forms.BooleanField(label='pledge', required=False)
    levels = forms.FloatField(label='levels', required=True)
    type_of_building = forms.ChoiceField(
        choices=[('0', 'wooden'), ('1', 'other'), ('2', 'monolithic'), ('3', 'brick'), ('4', 'panel')])
    status = forms.ChoiceField(
        choices=[('0', 'rough finish'), ('1', 'requires repair'), ('2', 'not completed'), ('3', 'average'), ('4', 'good'), ('5', 'free planning')])

    ceilings = forms.FloatField(label='ceilings', required=True)
    telephone_lines = forms.FloatField(label='telephone_lines', required=True)

    parking = forms.BooleanField(label='parking', required=False)
    all_day_security = forms.BooleanField(
        label='all_day_security', required=False)

    fire_alarm = forms.BooleanField(label='fire_alarm', required=False)

    signaling = forms.BooleanField(label='signaling', required=False)

    video_surveillance = forms.BooleanField(
        label='video_surveillance', required=False)

    window_bars = forms.BooleanField(label='window_bars', required=False)

    TV_cable = forms.BooleanField(label='TV_cable', required=False)
    ADSL = forms.BooleanField(label='ADSL', required=False)
    optics = forms.BooleanField(label='optics', required=False)
    wired = forms.BooleanField(label='wired', required=False)
   
  
