from django.urls import path
from.import views

urlpatterns = [
    path('webpage/', views.webpage),
    # path('signup/', views.registration,name='signup'),
    path('login/', views.login0),
    path('Signup/',views.register),
    path('products/',views.products),
    path('single products/', views.single)
]