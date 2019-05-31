from django.urls import path,include
from .views import form_view,displayData_view,deleteData_view,ApplicationModelDetailView,logout_view,register_view
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    #Landing Form Page
    path('',form_view,name='form'),
    #Article Display Home Page
    path('disp/',displayData_view,name='home'),
    path('home<int:id>', deleteData_view, name='home'),
    #View Clicked Article Page
    path('detail/<int:pk>',ApplicationModelDetailView,name='applicationmodel-detail'),
    #Django Built In Login and Logout Page
    path('login/',LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/',logout_view,name='logout'),
    #Django Register Url
    path('register/',register_view,name="register")
]