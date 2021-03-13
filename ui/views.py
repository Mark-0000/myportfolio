from django.shortcuts import render, redirect
from .forms import ContactForm
from django.urls import reverse
from .models import Project, Skill, Service


# Create your views here.
def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return redirect(reverse('index') + '#contact')
    else:
        pass

    context = {
        'projects': Project.objects.all(),
        'skills': Skill.objects.all(),
        'services': Service.objects.all()
    }
    return render(request, 'ui/index.html', context)
