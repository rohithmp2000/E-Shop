from itertools import product
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Products

# from shopapp.filters import VaccineFilter, UserFilter, HospitalFilter, ScheduleFilter
from shopapp.forms import SellerRegister, UserRegister
# , HostpitalForm, VaccineAdd, ScheduleAdd, ComplaintForm
from shopapp.models import Seller, User
# , Hospital, Vaccine, VaccinationSchedule, Complaint, Appointment
from django.contrib.auth.decorators import login_required


@login_required(login_url='login_view')
def seller_home(request):
    currentuser = request.user
    # print (currentuser)
    # print (currentuser.id)
    sellerid = Seller.objects.get(user_id=currentuser.id)
    items = Products.objects.filter(product_seller_id=sellerid.id)
    # print (sellerid.id)
    return render(request, 'seller/home.html',{'items':items })

@login_required(login_url='login_view')
def seller_acceptorder(request):
    return render(request, 'seller/acceptorder.html')

@login_required(login_url='login_view')
def seller_addproduct(request):
    # if request.method == 'POST':
    #     data = Products()
    #     data.product_name=request.POST.get('product_name')
    #     data.stock=request.POST.get('stock')
    #     data.image=request.POST.get('photo')
    #     data.price=request.POST.get('price')
    #     currentuser = request.user
    #     sellerid = Seller.objects.get(user_id=currentuser.id)
    #     data.product_seller = sellerid.id
    #     data.save()
    # else :
        return render(request, 'seller/addproduct.html')

def addproduct(request):
    if request.method == 'POST':
        data = Products()
        data.product_name=request.POST.get('product_name')
        data.stock=request.POST.get('stock')
        data.image=request.POST.get('photo')
        data.price=request.POST.get('price')
        currentuser = request.user
        sellerid = Seller.objects.get(user_id=currentuser.id)
        data.product_seller = sellerid
        data.save()
        return render(request, 'seller/addproduct.html')

def removeproduct(request,id):  
    items = Products.objects.get(id=id) 
    print (id)
    items.delete()
    return redirect('seller_home')

# @login_required(login_url='login_view')
# def vaccine_nurse(request):
#     v = Vaccine.objects.all()
#     vaccineFilter = VaccineFilter(request.GET, queryset=v)
#     v = vaccineFilter.qs
#     context = {
#         'vaccine': v,
#         'vaccineFilter': vaccineFilter,
#     }
#     return render(request, 'nurse/vaccine.html', context)


# @login_required(login_url='login_view')
# def users_nurse(request):
#     v = User.objects.all()
#     userFilter = UserFilter(request.GET, queryset=v)
#     v = userFilter.qs
#     context = {
#         'user': v,
#         'userFilter': userFilter,
#     }
#     return render(request, 'nurse/user.html', context)


# @login_required(login_url='login_view')
# def hospital_nurse(request):
#     v = Hospital.objects.all()
#     hospitalFilter = HospitalFilter(request.GET, queryset=v)
#     v = hospitalFilter.qs
#     context = {
#         'hospital': v,
#         'hospitalFilter': hospitalFilter,
#     }
#     return render(request, 'nurse/hospital.html', context)


# @login_required(login_url='login_view')
# def schedule_add(request):
#     form = ScheduleAdd()
#     if request.method == 'POST':
#         form = ScheduleAdd(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.info(request, 'Vaccination Schedule Added Successfully')
#             return redirect('schedule')
#     else:
#         form = ScheduleAdd()
#     return render(request, 'nurse/schedule_add.html', {'form': form})


# @login_required(login_url='login_view')
# def schedule(request):
#     n = VaccinationSchedule.objects.all()
#     scheduleFilter = ScheduleFilter(request.GET, queryset=n)
#     n = scheduleFilter.qs
#     context = {
#         'schedule': n,
#         'scheduleFilter': scheduleFilter,
#     }
#     return render(request, 'nurse/schedule.html', context)


# @login_required(login_url='login_view')
# def schedule_update(request, id):
#     n = VaccinationSchedule.objects.get(id=id)
#     if request.method == 'POST':
#         form = ScheduleAdd(request.POST or None, instance=n)
#         if form.is_valid():
#             form.save()
#             messages.info(request, 'Vaccination Schedule Updated Successfully')
#             return redirect('schedule')
#     else:
#         form = ScheduleAdd(instance=n)
#     return render(request, 'nurse/schedule_update.html', {'form': form})


# @login_required(login_url='login_view')
# def schedule_delete(request, id):
#     n = VaccinationSchedule.objects.get(id=id)
#     if request.method == 'POST':
#         n.delete()
#         messages.info(request, 'Vaccination Schedule Deleted Successfully')
#         return redirect('schedule')
#     else:
#         return redirect('schedule')


# @login_required(login_url='login_view')
# def complaint_add(request):
#     form = ComplaintForm()
#     u = request.user
#     if request.method == 'POST':
#         form = ComplaintForm(request.POST)
#         if form.is_valid():
#             obj = form.save(commit=False)
#             obj.user = u
#             obj.save()
#             messages.info(request, 'Complaint Registered Successfully')
#             return redirect('complaint')
#     else:
#         form = ComplaintForm()
#     return render(request, 'nurse/complaint_add.html', {'form': form})


# @login_required(login_url='login_view')
# def complaint(request):
#     n = Complaint.objects.filter(user=request.user)
#     return render(request, 'nurse/complaint.html', {'complaint': n})


# @login_required(login_url='login_view')
# def appointments_nurse(request):
#     a = Appointment.objects.filter(status=1).order_by('schedule__hospital')
#     return render(request, 'nurse/appointments.html', {'appointment': a})


# @login_required(login_url='login_view')
# def mark_vaccinated(request, id):
#     a = Appointment.objects.get(id=id)
#     vaccine = Vaccine.objects.filter(approval_status=1)
#     context = {
#         'vaccine': vaccine,
#         'a': a,
#     }
#     try:
#         if request.method == 'POST':
#             vacc = request.POST.get('vaccine')

#             a.vaccinated = True
#             a.vaccine_name = Vaccine.objects.get(id=vacc)
#             a.save()
#             return redirect('appointments_nurse')
#     except ValueError:
#         messages.info(request, 'Please Select a Vaccine')
#     return render(request, 'nurse/mark_vaccinated.html', context)
