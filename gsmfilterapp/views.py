from django.shortcuts import render, get_object_or_404, redirect
from .forms import *
from django.contrib import messages
import re
import datetime
from django.urls import reverse_lazy, reverse


def index(request):
    list = [GsmFilter.objects.all().order_by("-id")[0]]
    filtered = re.findall(r"\+(?:[0-9]●?){6,14}[0-9]", str(list))
    # for email in filtered:
    # return email
    if request.method == 'GET':
        form = GsmFilterForm()

    if request.method == 'POST':
        form = GsmFilterForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            text = form.cleaned_data.get("text")
            instance.text = text
            instance.pub_date = datetime.datetime.now()
            instance.save()
            messages.success(request, 'Success !!, Thanks for Submiting')
            return redirect(reverse('index'))
    context = {
        'list': list,
        'filtered': filtered,
        "form": form,
        # "email":email,
    }
    return render(request, 'index.html', context)

