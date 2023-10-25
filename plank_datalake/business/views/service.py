from django.shortcuts import render,redirect, get_object_or_404
from django.urls import reverse
from django.http import Http404
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages
from business.models import Service
from business.forms import ServiceForm
import base64

def crip(text):
    crip = base64.b64encode(text.encode()).decode()
    return crip

def uncrip(crip):
    text = base64.b64decode(crip).decode()
    return text

def parse_html_path(template_path,page):
    html_location = template_path + f'{page}.html'
    return html_location


#######################################
"""
SERVICE NEW_SERVICE
SERVICE PROFILE

"""
#######################################

SERVICE_PATH = 'business/SERVICE/'

def new_service(request):
    service_all = Service.objects.all()
    
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        html_location = parse_html_path(SERVICE_PATH,'new_service')
        if form.is_valid():
            service = form.save()
            return redirect('new_service')
        else:
            print(form.errors)
            response_dict = {
                'form': form,
                'service_all':service_all
            }
            return render(request, html_location, response_dict)
    else:
        form = ServiceForm()
        html_location = parse_html_path(SERVICE_PATH,'new_service')
        dict_form = {
            'form': form,
            'service_all':service_all
        }
    return render(request, html_location, dict_form)