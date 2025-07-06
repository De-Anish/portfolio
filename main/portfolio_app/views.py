
from django.shortcuts import render, redirect
from django.contrib import messages
from django import forms
from django.core.mail import send_mail
from django.conf import settings

# Contact Form using Django Forms
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Your Name'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Your Email'
    }))
    subject = forms.CharField(max_length=200, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Subject'
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'rows': 5,
        'placeholder': 'Your Message'
    }))

def home(request):
    return render(request, 'portfolio_app/home.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            
            # Send email
            try:
                send_mail(
                    subject=f"Portfolio Contact: {subject}",
                    message=f"From: {name} ({email})\n\n{message}",
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.EMAIL_HOST_USER],
                    fail_silently=False,
                )
                messages.success(request, 'Your message has been sent successfully!')
                return redirect('contact')
            except Exception as e:
                messages.error(request, 'Sorry, there was an error sending your message. Please try again.')
    else:
        form = ContactForm()
    
    return render(request, 'portfolio_app/contact.html', {'form': form})

def demo_videos(request):
    return render(request, 'portfolio_app/demo_videos.html')

def deployed_projects(request):
    return render(request, 'portfolio_app/deployed_projects.html')
