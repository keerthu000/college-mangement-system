from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('loginn',views.loginn,name='loginn'),
    path('teacher_signup',views.teacher_signup,name='teacher_signup'),
    path('usercreate',views.usercreate,name='usercreate'),
    path('teacher_login',views.teacher_login,name='teacher_login'),
    path('teachershow',views.teachershow,name='teachershow'),
    path('edit_teacher',views.edit_teacher,name='edit_teacher'),
    path('loginpage',views.loginpage,name='loginpage'),
    # path('welcome',views.welcome,name='welcome'),
    path('course',views.course,name='course'),
    path('super',views.super,name='super'),
    path('add_course',views.add_course,name='add_course'),
    path('add_student',views.add_student,name='add_student'),
    path('add_studentdb',views.add_studentdb,name='add_studentdb'),
    path('show_student',views.show_student,name='show_student'),
    path('edit/<int:pk>',views.edit,name='edit'),
    path('editpage/<int:pk>',views.editpage,name='editpage'),
    path('deletepage/<int:pk>',views.deletepage,name='deletepage'),
    path('logout',views.logout,name='logout')

]