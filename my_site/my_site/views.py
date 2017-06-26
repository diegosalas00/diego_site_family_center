from django.contrib import messages
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from . import forms


def home_page(request):
    return render(request, 'home.html')


def contact_page(request):
    return render(request, 'contact_page.html')


def edit_page(request):
    return render(request, 'edit_page.html')


def reserved_view(request):
    form = forms.ReservedForm()
    if request.method == 'POST':
        form = forms.ReservedForm(request.POST)
        if form.is_valid():
            send_mail(
                'Reservation from {}'.format(form.cleaned_data['name']),
                'Activity: {activity} \n'
                'Party Package: {party_packages} \n'
                'Reservation Date: {date} \n'
                'Drinks: {drink} \n'
                'Snacks: {snack} \n'
                'Questions: {questions}'.format(**form.cleaned_data),
                '{name} <{email}>'.format(**form.cleaned_data),
                ['diegosalas00@hotmail.com']
            )
            messages.add_message(request, messages.SUCCESS,
                                 'Thanks you for your reservation!')
            return HttpResponseRedirect(reverse('reserved'))
    return render(request, 'reserved_form.html', {'form': form})
