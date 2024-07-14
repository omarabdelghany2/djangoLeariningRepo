from django.db import models
import uuid
# Create your models here.



class Tag(models.Model):

    name=models.CharField(max_length=200)
    created=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4,primary_key=True,unique=True,editable=False)

    def __str__(self):
        return self.name
    


class project(models.Model):

    tags=models.ManyToManyField(Tag,blank=True)

    title=models.CharField(max_length=200)
    description=models.TextField(null=True,blank=True)
    #featured_image
    demo_link=models.CharField(max_length=1000,blank=True,null=True)
    source_link=models.CharField(max_length=1000,blank=True,null=True)
    voteTotal=models.IntegerField(default=0)
    voteratio=models.IntegerField(default=0)
    created=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)


    def __str__(self):
        return self.title
    

class review(models.Model):

    VOTE_TYPE=(('UP','UP'),
               ('DOWN','DOWN'))

    project=models.ForeignKey(project,on_delete=models.CASCADE,null=True,blank=True)
    body=models.TextField(null=True,blank=True)
    value=models.CharField(max_length=50,choices=VOTE_TYPE,null=True,blank=True)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    id=models.UUIDField(default=uuid.uuid4,primary_key=True,unique=True,editable=False)

    def __str__(self):
        return self.value
    

