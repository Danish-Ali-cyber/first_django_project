from django.urls import path
from . import views







urlpatterns = [
    path('',views.home,name='index'),
    path('complaint',views.complaint,name='complaint'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('forgotpassword',views.forgotpassword,name='forgotpassword'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('academic',views.academic,name='academic'),
    path('hostel',views.hostel,name='hostel'),
    path('mess',views.mess,name='mess'),
    path('complaintform1',views.complaintform1,name='complaintform1'),
    path('feedback',views.feedback,name='feedback'),
   
]