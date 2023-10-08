from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .models import ToDoList
# Create your views here.
def todo_view(request) :
    if request.method=="POST":
        title=request.POST.get("title")
        text=request.POST.get("text")
        todolist=ToDoList.objects.create(title=title,text=text)
        allobjects=ToDoList.objects.all()
        return render(request,"home.html",{"image_url":allobjects})
    return render(request,"home.html")

