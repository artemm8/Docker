from django.db import models

# Create your models here.

class ToDoList(models.Model):
    title=models.CharField(max_length=100)
    text=models.CharField(max_length=800)
    data=models.DateTimeField(auto_now_add=True)
    complete=models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title
