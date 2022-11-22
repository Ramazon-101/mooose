from django.shortcuts import render
from .forms import ContactForm
from .models import Subscribe


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
    email = request.GET.get('email')
    if email:
        Subscribe.objects.create(email=email)
    context = {
        'form': form
    }
    return render(request, 'website/contact.html', context)

