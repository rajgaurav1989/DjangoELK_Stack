from django import forms

class BulkUploadForm(forms.Form):
    up_file = forms.FileField(label='Select a file')