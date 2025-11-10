from django.shortcuts import redirect, render
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
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
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
            return None, True
    else:
        form = ContactForm()
        
    return form, False

def home(request):
    form, success = handle_contact_form(request)
    
    if success and request.method == 'POST':
        return redirect('home')
    
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
    
    if success and request.method == 'POST':
        return redirect('contact')
    
    context = {
        'form': form
    }
    
    return render(request, "contact.html", context)