from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field
from .models import Url


class UrlForm(forms.ModelForm):

    class Meta:
        model = Url
        fields = ['url_original']

    def __init__(self, *args, **kwargs):
        super(UrlForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.helper.layout = Layout(
            Field('url_original', placeholder='Original URL')
        )
