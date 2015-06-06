__author__ = 'Tarun Behal'

from django import forms
from .models import UserProfile, CampaignZone, Plantation


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class BootstrapTwoCol:
    bootstrap_two_col = {
        'normal_row': '<div class="form-group">\
            <span class="col-xs-2">%(label)s</span> \
            <div class="col-xs-10">%(field)s%(help_text)s</div></div>',
        'error_row': '%s',
        'row_ender': '</div>',
        'help_text_html': ' <span class="helptext">%s</span>',
        'errors_on_separate_row': True
    }

    def as_two_col_layout(self):
        return self._html_output(**self.bootstrap_two_col)


class JoinCampaignForm(forms.Form, BootstrapTwoCol):
    zone = forms.ModelChoiceField(queryset=CampaignZone.objects.all())


class AddPlantationForm(forms.ModelForm, BootstrapTwoCol):

    class Meta:

        model = Plantation
        fields = ['photo']
