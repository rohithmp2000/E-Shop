from django.contrib import admin
from django.urls import path

from shopapp import  views, seller_view, user_view

urlpatterns = [
    path('', views.home, name='home'),
    path('login_view/', views.login_view, name='login_view'),
    path('select_role/', views.select_role, name='select_role'),
    path('seller_register/', views.seller_register, name='seller_register'),
    path('user_register/', views.user_register, name='user_register'),
    path('logout_view/', views.logout_view, name='logout_view'),


    # path('admin_home/',admin_views.admin_home,name='admin_home'),
    # path('nurse/',admin_views.nurse,name='nurse'),
    # path('nurse_update/<int:user_id>/',admin_views.nurse_update,name='nurse_update'),
    # path('nurse_delete/<int:user_id>/',admin_views.nurse_delete,name='nurse_delete'),
    # path('user_view/',admin_views.user_view,name='user_view'),
    # path('user_delete/<int:user_id>/', admin_views.user_delete, name='user_delete'),
    # path('user_update/<int:user_id>/', admin_views.user_update, name='user_update'),
    # path('add_hospital/', admin_views.add_hospital, name='add_hospital'),
    # path('hospital/', admin_views.hospital, name='hospital'),
    # path('user_update/<int:id>/', admin_views.hospital_update, name='hospital_update'),
    # path('hospital_delete/<int:id>/', admin_views.hospital_delete, name='hospital_delete'),
    # path('add_vaccine/', admin_views.add_vaccine, name='add_vaccine'),
    # path('vaccine/', admin_views.vaccine, name='vaccine'),
    # path('vaccine_update/<int:id>/', admin_views.vaccine_update, name='vaccine_update'),
    # path('vaccine_delete/<int:id>/', admin_views.vaccine_delete, name='vaccine_delete'),
    # path('vaccine_approve/<int:id>/', admin_views.vaccine_approve, name='vaccine_approve'),
    # path('vaccine_reject/<int:id>/', admin_views.vaccine_reject, name='vaccine_reject'),
    # path('complaint_admin/', admin_views.complaint_admin, name='complaint_admin'),
    # path('reply_complaint/<int:id>/', admin_views.reply_complaint, name='reply_complaint'),
    # path('appointment_admin/', admin_views.appointment_admin, name='appointment_admin'),
    # path('approve_appointment/<int:id>/', admin_views.approve_appointment, name='approve_appointment'),
    # path('reject_appointment/<int:id>/', admin_views.reject_appointment, name='reject_appointment'),
    # path('vaccinated_list/', admin_views.vaccinated_list, name='vaccinated_list'),
    # path('add_reportcard/', admin_views.add_reportcard, name='add_reportcard'),
    # path('report_card/', admin_views.report_card, name='report_card'),


    path('seller_home/', seller_view.seller_home, name='seller_home'),
    path('seller_acceptorder/', seller_view.seller_acceptorder, name='seller_acceptorder'),
    path('seller_addproduct/', seller_view.seller_addproduct, name='seller_addproduct'),
    path('added/', seller_view.addproduct, name='added'),
    path('remove/<int:id>',seller_view.removeproduct, name="removeproduct"),
    # path('hospital_nurse/', nurse_views.hospital_nurse, name='hospital_nurse'),
    # path('schedule_add/', nurse_views.schedule_add, name='schedule_add'),
    # path('schedule/', nurse_views.schedule, name='schedule'),
    # path('schedule_update/<int:id>/', nurse_views.schedule_update, name='schedule_update'),
    # path('schedule_delete/<int:id>/', nurse_views.schedule_delete, name='schedule_delete'),
    # path('complaint_add/', nurse_views.complaint_add, name='complaint_add'),
    # path('complaint_add/', nurse_views.complaint_add, name='complaint_add'),
    # path('complaint/', nurse_views.complaint, name='complaint'),
    # path('appointments_nurse/', nurse_views.appointments_nurse, name='appointments_nurse'),
    # path('mark_vaccinated/<int:id>/', nurse_views.mark_vaccinated, name='mark_vaccinated'),


    path('user_home/', user_view.user_home, name='user_home'),
    # path('schedule_user/', user_views.schedule_user, name='schedule_user'),
    # path('take_appointment/<int:id>/', user_views.take_appointment, name='take_appointment'),
    # path('appointments/', user_views.appointments, name='appointments'),
    # path('complaint_add_user/', user_views.complaint_add_user, name='complaint_add_user'),
    # path('complaint_user/', user_views.complaint_user, name='complaint_user'),
    # path('user_profile/', user_views.user_profile, name='user_profile'),
    # path('profile_update/<int:user_id>/', user_views.profile_update, name='profile_update'),
    # path('reportcard_user/', user_views.reportcard_user, name='reportcard_user'),

    path('store/', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
	path('payment/', views.payment, name="payment"),
]


















