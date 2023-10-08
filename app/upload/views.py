from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
# Create your views here.
def image_upload(request) :
    if request.method=="POST" and request.FILES["image_file"] :
        image_file=request.FILES["image_file"]
        fs=FileSystemStorage()
        file_name=fs.save(image_file.name,image_file)
        image_url=fs.url(file_name)
        return render(request,"upload.html",{"image_url":image_url})
    return render(request,"upload.html")