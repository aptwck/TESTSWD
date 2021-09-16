from django import forms

class Sendmail(forms.Form):
    Email = forms.EmailField()
    Message = forms.CharField(widget=forms.Textarea)
    
    def __str__(self):
        return self.Email + ' ' + self.Message