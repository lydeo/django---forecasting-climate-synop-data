from django import forms


class FormField(forms.Form):
    
    input_bulan = forms.ChoiceField(label="Bulan: ")
    input_tahun = forms.ChoiceField(label="Tahun: ")