from django.shortcuts import render
from django.apps import apps
from datetime import date
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from datetime import date

from .models import Employee

# Create your views here.

# TODO: Create a function for each path created in employees/urls.py. Each will need a template as well.

def create(request):
    logged_in_user = request.user
    if request.method == "POST":
        name_from_form = request.POST.get('name')
        zip_from_form = request.POST.get('zip_code')
        badge_number_from_form = request.POST.get('badge_number')
        new_employee = Employee(name=name_from_form, user=logged_in_user, zip_code=zip_from_form, badge_number=badge_number_from_form)
        new_employee.save()
        return HttpResponseRedirect(reverse('employees:index'))
    else:
        return render(request, 'employees/create.html')

def edit_profile(request):
    logged_in_user = request.user
    logged_in_employee = Employee.objects.get(user=logged_in_user)
    if request.method == "POST":
        name_from_form = request.POST.get('name')
        zip_from_form = request.POST.get('zip_code')
        logged_in_employee.name = name_from_form
        logged_in_employee.zip_code = zip_from_form
        logged_in_employee.save()
        return HttpResponseRedirect(reverse('employees:index'))
    else:
        context = {
            'logged_in_employee': logged_in_employee
        }
        return render(request, 'employees/edit_profile.html', context)

def route(request):
    logged_in_user = request.user
    logged_in_employee = Employee.objects.get(user=logged_in_user)
    logged_in_employee_zip_code = logged_in_employee.zip_code
    today = date.today
    Customer = apps.get_model('customers.Customer')
    all_customers = Customer.objects.all()
    customer_same_zip_code = all_customers.filter('logged_in_employee_zip_code'=all_customers.zip_code)
    and_not_suspended = customer_same_zip_code.exclude('customer_same_zip_code.suspend_start__lt'=today).exclude('customer_same_zip_code.suspend_end__gt'=today)
    and_not_picked_up = and_not_suspended.exclude('date_of_last_pickup'=today)
    context = {
        'and_not_picked_up': and_not_picked_up,
        'today': today
    }
    return render(request, 'employees/route.html', context)


# create qurey and filter to diplay customers for the day

# create link to confirm completion and charge $20 to the customers account

# create filter to show customers who have pickup that day


def index(request):

    # The following line will get the logged-in user (if there is one) within any view function
    logged_in_user = request.user
    try:
        # This line will return the employee record of the logged-in user if one exists
        logged_in_employee = Employee.objects.get(user=logged_in_user)

        today = date.today()
        
        
        context = {
            'logged_in_employee': logged_in_employee,
            'today': today
        }
        return render(request, 'employees/index.html', context)
        
    except ObjectDoesNotExist:
        return HttpResponseRedirect(reverse('employees:create'))
    # This line will get the Customer model from the other app, it can now be used to query the db for Customers
    
    # return render(request, 'employees/index.html')
