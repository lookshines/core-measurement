from django import forms
from .models import ContactMessages

class ContactForm(forms.ModelForm):
    
    class Meta:
        model = ContactMessages
        fields = ['fullname', 'email', 'phone', 'message']
        widgets = {
            'fullname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your full name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'your@email.com'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Phone Number'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your mesaage...'}),     
        }
        
        labels= {
            'fullname': 'Name', 
            'email': 'Email', 
            'phone': 'Phone',  
            'message': 'Message'
        }