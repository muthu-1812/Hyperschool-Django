from django.db import models
from django.forms import ModelForm
from .models import Course
from django import forms

# class SearchForm(ModelForm):
#     class Meta:
#        model = Course
#        fields = ["title"]
#     def __init__(self, title=None, **kwargs):
#         super(SearchForm, self).__init__(**kwargs)
#         if title:
#             self.fields['course'].queryset = models.Course.objects.filter(title=title)
#
#


class SearchForm(forms.Form):
    q = forms.CharField(required=False, label='')
