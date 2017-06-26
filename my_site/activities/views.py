from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, render_to_response

from . import forms
from . import models
# Create your views here.


def availability_page(request):
    items = models.Available.objects.all()
    return render_to_response('availability.html', {'items': items})


def activity_list(request):
    activities = models.Activity.objects.all()
    return render(request, 'activities/activity_list.html', {'activities': activities})


def activity_detail(request, pk):
    activity = get_object_or_404(models.Activity, pk=pk)
    return render(request, 'activities/activity_detail.html', {'activity': activity})


def package_detail(request, activity_pk, package_pk):
    package = get_object_or_404(models.PartyPackage, activity_id=activity_pk, pk=package_pk)
    return render(request, 'activities/package_detail.html', {'package': package})


@login_required
def activity_create(request):
    form = forms.ActivityForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.add_message(request, messages.SUCCESS,
                             "Activity added!")
    context = {
        'form': form
    }

    return render(request, "activities/activity_form.html", context)


@login_required
def availability_create(request):
    form = forms.AvailableForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.add_message(request,  messages.SUCCESS,
                             "Person added!")

    context = {
            'form': form,
    }
    return render(request, "activities/available_form.html", context)


@login_required
def package_create(request):
    form = forms.PartyPackageForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.add_message(request, messages.SUCCESS,
                             "Packageg added!")
    return render(request, "activities/package_form.html", {"form": form})
