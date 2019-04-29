# import os

# from django.shortcuts import render
# from django.shortcuts import render, redirect, get_object_or_404, render_to_response
# from django.template import RequestContext
# from django.core.urlresolvers import reverse
# from django.contrib.auth.decorators import login_required, user_passes_test
# from django.contrib import messages
# from django.http import HttpResponse, HttpResponseRedirect
# from django.views.decorators.csrf import csrf_exempt
# from django.conf import settings
# from django.db.models import Count, Sum, Q
# from employees.models import *
# from fleet_management.models import *
# from fleet_management.exporter import extract_employee_data, extract_driving_licences_data
# import threading
# import re

# from forms import EmployeeForm, EmployeeFilterForm, DrivingLicenceForm, DrivingLicenceFilterForm

# from django.template import Context
# import StringIO
# from reportlab.pdfgen import canvas
# from xhtml2pdf import pisa
# from django.views.generic import View
# from io import BytesIO
# from django.template.loader import get_template

# @login_required
# def employees(request, template="employees/employees.html"):
#     context = {}
# #    district_list = request.user.get_user_district
#     region_id = request.user.get_user_region

#     employees = Employee.objects.exclude(driver_vehicle__start_date__isnull=False,
#                                          driver_vehicle__end_date__isnull=True)
#     employee_filter_form = EmployeeFilterForm(request.GET or None)
#     heading = "Unassigned Drivers"

#     if not request.user.is_superuser:
#         if region_id:
#             employees = employees.filter(region__id=region_id)
#         else:
#             employees = Employee.objects.none()

#     if u'filter' in request.GET or u'extract' in request.GET:
#         if employee_filter_form.is_valid():
#             employees = employee_filter_form.filter()
#             if not request.user.is_superuser:
#                 if region_id:
#                     employees = employees.filter(region__id=region_id)
#                 else:
#                     employees = Employee.objects.none()
#             assigned = employee_filter_form.cleaned_data['assigned']
#             if assigned == "assigned":
#                 heading = "Assigned Drivers"
#             elif assigned == "unassigned":
#                 heading = "Unassigned Drivers"
#             else:
#                 heading = "All Drivers"


#     if u'extract' in request.GET:
#         download_thread = threading.Thread(target=extract_employee_data,
#                                            args=(request.user, 'all_employees', employees,
#                                                  employee_filter_form.cleaned_data))
#         download_thread.start()
#         messages.success(request, 'Your extract has been added to the download queue. Queue processing may take a while. Check your report in downloads.')

#     context['all_employees'] = employees
#     context['employee_filter_form'] = employee_filter_form
#     context['heading'] = heading
#     return render(request, template, context)

# @login_required
# def edit_employee(request, employee_id=None, template="employees/employee_edit.html", context=None):

#     context = context or {}
#     incidents = ['windscreen','smash and grab','road accident','vehicle']

#     employee = Employee.objects.get(pk=employee_id) if employee_id else None

#     vehicle_history = VehicleDriver.objects.filter(driver__id=employee_id)

#     traffic_incidents = Incident.objects.filter(driver_id=employee_id,incident_type='traffic fine')\
#                                  .values('id','reference_number','vehicle__registration_number','incident_date','cost','incident_type')\
#                                  .order_by('incident_date')
#     other_incidents = Incident.objects.filter(driver_id=employee_id,incident_type__in=incidents)\
#                                  .values('id','reference_number','vehicle__registration_number','incident_date','cost','incident_type')\
#                                  .order_by('incident_date')
#     insurance_incidents = InsuranceClaim.objects.filter(driver=employee)\
#                                                 .values('id','insurance_reference_number','vehicle__registration_number','incident_date','quote_amount')\
#                                                 .order_by('incident_date')

#     employee_form = EmployeeForm(request.POST or None, instance=employee)
#     driving_licence_form = DrivingLicenceForm(request.POST or None, request.FILES or None)

#     if u'save' in request.POST:
#         if driving_licence_form.is_valid():
#             licence = driving_licence_form.save(commit=False)
#             licence.employee = employee
#             licence.save()
#             return redirect(reverse('employees:employees'))

#     if u'cancel' in request.POST:
#         return redirect(reverse('employees:employees'))

#     context['employee'] = employee
#     context['vehicle_history'] = vehicle_history
#     context['employee_form'] = employee_form
#     context['driving_licence_form'] = driving_licence_form
#     context['traffic_incidents'] = traffic_incidents
#     context['other_incidents'] = other_incidents
#     context['insurnace_incidents'] = insurance_incidents

#     return render(request, template, context)

# def edit_driving_licence(driving_licence_form, employee, has_errors, user):
#     if driving_licence_form.is_valid():
#         licence = driving_licence_form.save(commit=False)
#         licence.employee = employee
#         licence.save()
#     elif driving_licence_form.errors or has_errors:
#         has_errors = True

#     return has_errors

# @login_required
# def view_employee(request, employee_id=None, template="employees/employee_edit.html", context=None):

#     context = context or {}
#     incidents = ['windscreen','smash and grab','road accident','vehicle']

#     employee = Employee.objects.get(pk=employee_id) if employee_id else None

#     drivervehicle = VehicleDriver.objects.filter(driver=employee_id)

#     traffic_incidents = Incident.objects.filter(driver_id=employee_id,incident_type='traffic fine')\
#                                  .values('id','reference_number','vehicle__registration_number','incident_date','cost','incident_type')\
#                                  .order_by('incident_date')
#     other_incidents = Incident.objects.filter(driver_id=employee_id,incident_type__in=incidents)\
#                                  .values('id','reference_number','vehicle__registration_number','incident_date','cost','incident_type')\
#                                  .order_by('incident_date')
#     insurance_incidents = InsuranceClaim.objects.filter(driver=employee)\
#                                                 .values('id','insurance_reference_number','vehicle__registration_number','incident_date','quote_amount')\
#                                                 .order_by('incident_date')

#     employee_form = EmployeeForm(request.POST or None, instance=employee)
#     driving_licence_form = DrivingLicenceForm(request.POST or None, request.FILES or None)

#     if u'save' in request.POST:
#         if employee_form.is_valid() and driving_licence_form.is_valid():
#             employee = employee_form.save(request.user)
#             employee.save()

#             licence = driving_licence_form.save(commit=False)
#             licence.employee = employee
#             licence.save()

#             next = request.POST.get('next', '/')

#             return HttpResponseRedirect(next)

#     if u'cancel' in request.POST:
#         next = request.POST.get('next', '/')
#         return HttpResponseRedirect(next)

#     context['employee'] = employee
#     context['employee_form'] = employee_form
#     context['driving_licence_form'] = driving_licence_form
#     context['traffic_incidents'] = traffic_incidents
#     context['other_incidents'] = other_incidents
#     context['insurnace_incidents'] = insurance_incidents

#     return render(request, template, context)

# @login_required
# def drivers_licence_expiry(request, template="employees/reports/_driver_licence_expiry.html"):

#     context = {}
#     driving_licence_expiry_filter_form = DrivingLicenceFilterForm(request.GET or None)

#     driving_licences = DrivingLicence.objects.all()

#     if u'search' in request.GET or u'extract' in request.GET:
#         if driving_licence_expiry_filter_form.is_valid():
#             driving_licences = driving_licence_expiry_filter_form.filter(driving_licences)

#     if u'extract' in request.GET:

#         download_thread = threading.Thread(target=extract_driving_licences_data,
#                                            args=(request.user, 'all_driving_licences', driving_licences,
#                                                  driving_licence_expiry_filter_form.cleaned_data))
#         download_thread.start()
#         messages.success(request, 'Your extract has been added to the download queue. Queue processing may take a while. Check your report in downloads.')

#     context['all_driving_licence'] = driving_licences
#     context['driving_licence_expiry_filter_form'] = driving_licence_expiry_filter_form
#     return render(request, template, context)

# def driver_summary_document(request, driver_id, letter=False):

#     context = {}
#     driver = Employee.objects.get(pk=driver_id)
#     curr_vehicle = driver.curr_vehicle
#     driver_licence_expiry_date = driver.driving_licence
#     traffic_fines = Incident.objects.filter(driver=driver_id, incident_type='traffic fine').order_by('-id')
#     incidents = Incident.objects.filter(driver=driver_id, incident_type__in = ['vehicle','windscreen', 'tyres','other']).order_by('-id')

#     template = get_template('employees/widgets/documents/driver_summary_pdf.html')
#     context = {
#         'pagesize': 'A4',
#         "driver":driver,
#         "curr_vehicle":curr_vehicle,
#         "traffic_fines":traffic_fines,
#         "driver_licence_expiry_date":driver_licence_expiry_date,
#         "incidents":incidents,
#         'STATIC_URL' : settings.STATIC_URL
#       }


#     html = template.render(context)
#     pdf = render_to_pdf('employees/widgets/documents/driver_summary_pdf.html', context)
#     if pdf:
#         today = datetime.today().strftime("%Y%m%d_%H%M")
#         response = HttpResponse(pdf, content_type='application/pdf')
#         filename = "driver_summary_%s.pdf" %(today)
#         content = "inline; filename='%s'" %(filename)
#         download = request.GET.get("download")
#         if download:
#             content = "attachment; filename='%s'" %(filename)
#         response['Content-Disposition'] = content
#         return response
#     return HttpResponse("Not found")


# def render_to_pdf(template_src, context_dict={}):
#     template = get_template(template_src)
#     html  = template.render(context_dict)
#     result = BytesIO()
#     pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
#     if not pdf.err:
#         return HttpResponse(result.getvalue(), content_type='application/pdf')
#     return None