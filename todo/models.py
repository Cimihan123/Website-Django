from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.


Tags_Chocies = (

    ('computer' , 'computer'),
    ('books' , 'books'),
    ('furniture' , 'furniture'),

)



class Todo(models.Model):

    title = models.CharField(max_length = 20)
    date_todo = models.DateTimeField(auto_now=True , blank=True)
    decription = RichTextField(max_length = 200)
    active = models.BooleanField(default=False)
    image = models.ImageField(upload_to='todopics')
    tags = models.CharField(choices=Tags_Chocies,max_length=10)


    def __str__(self):

        return str(self.title[:10])


class Comment(models.Model):
    todo = models.ForeignKey(Todo,on_delete=models.CASCADE,null=True) 
    name = models.CharField(max_length = 20)
    date_todo = models.DateTimeField(auto_now=True , blank=True)
    comment = models.CharField(max_length = 200)

    def __str__(self):

        return str(self.name)