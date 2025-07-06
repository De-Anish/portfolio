
from django.shortcuts import render, redirect
from django.contrib import messages
from django import forms
from django.core.mail import send_mail
from django.conf import settings

# Contact Form using Django Forms
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    subject = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

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
            
            # Compose email content
            email_subject = f"Portfolio Contact: {subject}"
            email_message = f"""
            New contact form submission:
            
            Name: {name}
            Email: {email}
            Subject: {subject}
            
            Message:
            {message}
            """
            
            try:
                # Send email
                send_mail(
                    email_subject,
                    email_message,
                    settings.DEFAULT_FROM_EMAIL,  # From email
                    [settings.EMAIL_HOST_USER],   # To email (your email)
                    fail_silently=False,
                )
                messages.success(request, 'Your message has been sent successfully! I will get back to you soon.')
                return redirect('contact')
            except Exception as e:
                messages.error(request, f'Sorry, there was an error sending your message. Please try again later. Error: {str(e)}')
    else:
        form = ContactForm()
    
    return render(request, 'portfolio_app/contact.html', {'form': form})

def demo_videos(request):
    return render(request, 'portfolio_app/demo_videos.html')

def deployed_projects(request):
    return render(request, 'portfolio_app/deployed_projects.html')
