from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('signupform/', views.signupform, name='signupform'),
    path('loginform/', views.loginform, name='loginform'),
    path('cart/', views.cart, name='cart'),
    path('addstrain', views.addstrain, name='addstrain'),
    path('orders/', views.orders, name='orders'),
    path('strains/', views.strains, name='strains'),
    path('deletestrain/<id>', views.deletestrain, name='deletestrains'),
    path('addStrainToDb', views.addStrainToDb, name="addStrainToDb"),
    path('usersignup', views.userSignUp, name='usersignup'),
    path('userlogin', views.userlogin, name='userlogin'),
    path('editstrain/<id>', views.editstrain, name='editstrain'),
    path('deliverydetails', views.deliverydetails, name='deliverydetails'),
    path('resetpassword', views.resetpassword, name='resetpassword'),
    path('logoutuser/', views.logoutuser, name='logoutuser'),
    path('adminbase', views.adminbase, name='adminbase'),
    path('sliders/', views.sliders, name='sliders'),
    path('searchresult/', views.searchresult, name='searchresult')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
