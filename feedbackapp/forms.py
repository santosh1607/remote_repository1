from django import forms
class FeedbackForm(forms.Form):
    name=forms.CharField(
        label="Enter your name",
        widget=forms.TextInput(
            attrs={
                'placeholder':'Your name',
                'class':'form-control'
            }
        )
     )
    ratting = forms.IntegerField(
        label="Enter your ratting",
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Your ratting',
                'class': 'form-control'
            }
        )
    )
    feedback = forms.CharField(
        label="Enter your feedback",
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Your feedback',
                'class': 'form-control'
            }
        )
    )