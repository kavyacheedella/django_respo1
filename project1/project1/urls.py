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
from django.urls import path,re_path
from basic1.views import home,contact,services,index,sample,sample1,sample2,createData,createProduct,userdata,employee_data
from orderdetails.views import OrderPlacing
from moviedetails.views import BookMyshow,get_all_movies
from bookstore.views import bookdetails,get_details,update_book_details,del_book_details,update_book_by_author_regex,delete_book_by_author_regex
from registrations.views import student_registration,get_student_details
from eligibility_checking.views import attend_exam
from sign_up_page.views import signup

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
    path('placing/',OrderPlacing),
    path('bookticket/',BookMyshow),
    path('movies/',get_all_movies),
    path('registeration/',student_registration),
    path('studentdetails/',get_student_details),
    path('books/',bookdetails),
    path('bookdetails/',get_details),
    path('updatebookdetails/',update_book_details),
    # path('delbookdetails/<str:ref_author>/',del_book_details)
    re_path(r'^delbookdetails/(?P<ref_author>[A-za-z\. ]+)/$',del_book_details),
    path('delbookdetailsregex/',delete_book_by_author_regex),
    path('updatebookdetailsregex/',update_book_by_author_regex),
    path('student_eligibility/',attend_exam),
    path('normal_user_checking/',signup)
]
