from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['game', 'rating', 'comment']

        widgets = {
            'game': forms.Select(attrs={'class': 'form-control'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'max': 10}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }
