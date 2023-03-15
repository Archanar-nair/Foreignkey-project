from django.shortcuts import render,redirect
from appone.models import course
from appone.models import student

# Create your views here.
def home(request):
    return render(request,'home.html')
def addcourse(request):
    return render(request,'addcourse.html')
def addstudent(request):
    courses=course.objects.all()
    return render(request,'addstudent.html',{'course':courses})
def coursedb(request):
    if request.method=='POST':
        course_name=request.POST.get('course')
        fee=request.POST.get('fee')
        coursedb=course(course_name=course_name,fee=fee)
        coursedb.save()
        return redirect('/')

def studentdb(request):
    if request.method=="POST":
        name=request.POST.get('name')
        age=request.POST.get('age')
        address=request.POST.get('address')
        date=request.POST.get('date')
        sel=request.POST['select']
        course1=course.objects.get(id=sel)
        studentdb=student(name=name,age=age,address=address,date=date,course=course1)
        studentdb.save()
        return redirect('/')

def showstudent(request):
        student1=student.objects.all()
        return render(request,'showstudent.html',{'students':student1})

def edit(request,pk):
      studentdb=student.objects.get(id=pk)
      course1=course.objects.all()
    
      return render(request,'edit.html',{'students':studentdb,'courses':course1})

def editdb(request,pk):
     if request.method=='POST':
          studentdb=student.objects.get(id=pk)
          studentdb.name=request.POST['name']
          studentdb.age=request.POST['age']
          studentdb.address=request.POST['address']
          studentdb.date=request.POST['date']
          student_course=request.POST['select']
          course1=course.objects.get(id=student_course)
          studentdb.course=course1
          studentdb.save()
          return redirect('showstudent')
     return render(request,'edit.html')
     
          

def Delete(request,pk):
    stud=student.objects.get(id=pk)
    stud.delete()
    return redirect('showstudent')



