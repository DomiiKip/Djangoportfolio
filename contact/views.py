from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages

# Create your views here.
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def home_view(request):
    return render(request, 'home.html')