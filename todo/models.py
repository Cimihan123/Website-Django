from django.db import models

# Create your models here.


class Todo(models.Model):

    title = models.CharField(max_length = 20)
    date_todo = models.DateTimeField(auto_now=True , blank=True)
    decription = models.CharField(max_length = 200)

    def __str__(self):

        return str(self.title[:10])


class Comment(models.Model):
    todo = models.ForeignKey(Todo,on_delete=models.CASCADE,null=True) 
    name = models.CharField(max_length = 20)
    date_todo = models.DateTimeField(auto_now=True , blank=True)
    comment = models.CharField(max_length = 200)

    def __str__(self):

        return str(self.name)