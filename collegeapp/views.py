from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from collegeapp.models import Course
from collegeapp.models import Student
from collegeapp.models import Usermember
from django.contrib.auth.models import User
import os

# Create your views here.
def home(request):
    return render(request,'home.html')
def loginn(request):
    return render(request,'loginn.html')
# def welcome(request):
#     return render(request,'welcome.html')
def course(request):
    return render(request,'course.html')
def super(request):
    return render(request,'welcome.html')
def teacher_signup(request):
    course=Course.objects.all()
    return render(request,'sign.html',{'course':course})
def teacher_login(request):
    return render(request,'teacherlogin.html')
def teachershow(request):
    user_id=request.user.id
    show=Usermember.objects.get(user=user_id)
    return render(request,'seepro.html',{'sh':show})
def edittecherpage(request):
    return render(request,'edi')
def edit_teacher(request):
    if request.user.is_authenticated:
        current_user=request.user.id
        user1=Usermember.objects.get(user_id=current_user)
        user2=User.objects.get(id=current_user)
        if request.method=="POST":
            if len(request.FILES)!=0:
                if len(user1.image)>0:
                    os.remove(user1.image.path)
                    user1.image=request.FILES.get('file')
                user2.first_name=request.POST.get('fname')
                user2.last_name=request.POST.get('lname')
                user2.username=request.POST.get('uname')
                user2.password=request.POST.get('password')
                user2.email=request.POST.get('email')
                user1.address=request.POST.get('adress')
                user1.age=request.POST.get('age')
                user1.number=request.POST.get('contact_num')
                user1.save()
                user2.save()
                return redirect('showteacher')
            return render(request,'editteacher.html',{"users":user1})
    return render('/')


def usercreate(request):
    if request.method=='POST':
        firstname=request.POST['fname']
        lastname=request.POST['lname']
        username=request.POST['uname']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        age=request.POST['age']
        address=request.POST['adress']
        email=request.POST['email']
        contact_num=request.POST['cnum']
        sel=request.POST['sel']
        course1=Course.objects.get(id=sel)
        image=request.FILES.get('file')
      

        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'This username is already exist!!!!!!!!!!!!!!!')
                return redirect('teacher_signup')
            else:
                user=User.objects.create_user(
                    first_name=firstname,
                    last_name=lastname,
                    username=username,
                    password=password,
                    email=email)
                user.save()
                u=User.objects.get(id=user.id)
                member=Usermember(address=address,age=age,number=contact_num,image=image,user=u,course=course1)
                member.save()
                return redirect('loginn')

        else:
            messages.info(request,'Pasword doesnot match!!!!!!!!!!')
            return  redirect('teacher_signup')
        
    else:
        return redirect(request,'teacher_signup')


def loginpage(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is  not  None:
            if user.is_staff:
                login(request,user)
                return redirect('super')
            else:
                login(request,user)
                auth.login(request,user)
                messages.info(request,f'Welcome {username}')
                return redirect('teacher_login')
        else:
            messages.info(request,'Invalid Username or Password. Try again.')
            return redirect('loginn')
    else:
        return redirect('loginn')   

    
def add_course(request):
    if request.method=='POST':
        course_name=request.POST.get('course')
        course_fee=request.POST.get('amount')
        course=Course(course_name=course_name,fee=course_fee)
        course.save()
        return redirect('super')
def add_student(request):
    course=Course.objects.all()
    return render (request,'addstudent.html',{'course':course})

        
def add_studentdb(request):
    if request.method=='POST':
        student_name=request.POST['name']
        student_address=request.POST['address']
        age=request.POST['age']
        jdate=request.POST['date']
        sel=request.POST['sel']
        course1=Course.objects.get(id=sel)
        student=Student(student_name=student_name,student_address=student_address,student_age=age,joining_date=jdate,course=course1)
        student.save()
        return redirect('super')
@login_required(login_url='home')
def show_student(request):
    student=Student.objects.all()
    return render(request,'showstudent.html',{'students':student})
def edit(request,pk):
    stu=Student.objects.get(id=pk)
    course=Course.objects.all()
    return render(request,'edit.html',{'stud':stu,'course':course})
def editpage(request,pk):
    if request.method=='POST':
        student=Student.objects.get(id=pk)
        student.student_name=request.POST.get('name')
        student.student_address=request.POST.get('address')
        student.student_age=request.POST.get('age')
        student.joining_date=request.POST.get('date')
        course=request.POST.get('sel')
        course1=Course.objects.get(id=course)
        student.course=course1
        student.save()
        return redirect('show_student')
    return render(request,'edit.html')

def deletepage(request,pk):
    stu=Student.objects.get(id=pk)
    stu.delete()
    return redirect('show_student')
@login_required(login_url='home')
def logout(request):
    request.session['userid']=""
    auth.logout(request)
    return redirect('home')