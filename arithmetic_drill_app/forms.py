from django import forms

class DrillForm(forms.Form):
    num_questions = forms.IntegerField(label='Number of questions')
    min_num = forms.IntegerField(label='Minimum number')
    max_num = forms.IntegerField(label='Maximum number')
