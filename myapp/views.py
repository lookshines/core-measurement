from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from decouple import config, Csv

# Create your views here.
def handle_contact_form(request):
    """
    Handles contact form processing and email sending.
    Returns a tuple: (form instance, success boolean)
    """
    form = ContactForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        message = form.save()
        
        # Send email notification
        send_mail(
            subject=f"New Contact Message from {message.fullname}",
            message=(
                f"Name: {message.fullname}\n"
                f"Email: {message.email}\n"
                f"Phone: {message.phone}\n"
                f"Message: {message.message}"
            ),
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=config("RECIPIENT_LIST", cast=Csv()),  # Change this
            fail_silently=False,
        )
        messages.success(request, "Thank you! Your message has been sent successfully.")
        form1 = ContactForm()
        return form1, True
    return form, False

def home(request):
    form, success = handle_contact_form(request)
    
    context = {
        'form': form
    }
    
    return render(request, "index.html", context)

def about(request):
    return render(request, "about-us.html")

def services(request):
    return render(request, "services.html")

def hse(request):
    return render(request, "hse.html")

def contact(request):
    form, success = handle_contact_form(request)
    
    context = {
        'form': form
    }
    
    return render(request, "contact.html", context)