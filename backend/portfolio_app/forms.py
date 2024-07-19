from django import forms

class UploadFileForm(forms.Form):
    region_1 = forms.FileField(label='Upload Region 1 CSV')
    region_2 = forms.FileField(label='Upload Region 2 CSV')
    region_3 = forms.FileField(label='Upload Region 3 CSV')