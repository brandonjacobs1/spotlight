from django import forms
from .models import Spotlight
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field


class DateInput(forms.DateInput):
    input_type = 'date'


class SpotlightForm(forms.ModelForm):
    class Meta:
        model = Spotlight
        fields = "__all__"
        labels = {
            'last_name': 'Couple\'s Last Name',
            'first_name_husband': 'Husband\'s First Name',
            'first_name_wife': 'Wife\'s First Name',
            'status': 'Status',
            'date_asked': 'Asked Date',
            'date_ready': 'Ready Date',
            'date_planned': 'Planned Release Date',
            'date_slacked': 'Sent Date',
            'member_type': 'Type of Member',
            'date_joined': 'Ward Joined Date',
            'bio': 'Bio',
            'image': 'Image'

        }
        widgets = {
            'date_joined': DateInput(),
            'date_slacked': DateInput(),
            'date_ready': DateInput(),
            'date_planned': DateInput(),
            'date_asked': DateInput()
        }

    def __init__(self, *args, **kwargs):
        super(SpotlightForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('last_name'),
            Field('first_name_husband'),
            Field('first_name_wife'),
            Field('status'),
            Field('date_asked'),
            Field('date_ready'),
            Field('date_planned'),
            Field('date_slacked'),
            Field('member_type'),
            Field('date_joined'),
            Field('bio'),
            Field('image'),
            Submit('submit', 'Submit', css_class='btn btn-primary')
        )
