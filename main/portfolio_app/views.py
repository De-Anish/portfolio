from django.shortcuts import render, redirect
from django.contrib import messages
from django import forms
from django.core.mail import send_mail  # ✅ Required for sending email
from django.conf import settings         # ✅ For accessing EMAIL settings

# -----------------------------
# ContactForm using Django Forms
# -----------------------------
class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'})
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Message', 'rows': 5})
    )

# ---------------------
# Views for each page
# ---------------------

def home(request):
    return render(request, 'portfolio_app/home.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Extract cleaned data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Construct email body
            full_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

            # Send email to your own inbox
            send_mail(
                subject=f'Contact Form Submission from {name}',
                message=full_message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False,
            )

            messages.success(request, 'Thank you! Your message has been sent successfully.')
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'portfolio_app/contact.html', {'form': form})


def demo_videos(request):
    return render(request, 'portfolio_app/demo_videos.html')


def deployed_projects(request):
    return render(request, 'portfolio_app/deployed_projects.html')
