from django import forms

class Search(forms.Form):
	Url_search = forms.URLField()