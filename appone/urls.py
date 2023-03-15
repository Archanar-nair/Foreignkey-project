from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('addcourse/',views.addcourse,name='addcourse'),
    path('addstudent/',views.addstudent,name='addstudent'),
    path('coursedb/',views.coursedb,name='coursedb'),
    path('studentdb/',views.studentdb,name='studentdb'),
    path('showstudent/',views.showstudent,name='showstudent'),
    path('edit/<int:pk>',views.edit,name='edit'),
    path('editdb/<int:pk>', views.editdb,name='editdb'),
    path('Delete/<int:pk>', views.Delete,name='Delete')
   


]
