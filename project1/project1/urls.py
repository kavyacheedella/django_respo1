"""
URL configuration for project1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from basic1.views import home,contact,services,index,sample,sample1,sample2,createData,createProduct,userdata,employee_data
from orderdetails.views import OrderPlacing

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index , name='index'),
    path('home/',home , name = 'home'),
    path('services/',services , name= 'services'),
    path('contact/',contact , name = 'contact'),
    path('sample/' , sample),
    path('sample1/' , sample1),
    path('sample2/' , sample2),
    path('create/',createData),
    path('productcreate/',createProduct),
    path('user1data/', userdata),
    path('employeedetails/',employee_data),
    path('placing/',OrderPlacing)
]
