from django.shortcuts import render
from django.http import HttpResponse
from .models import project
from .forms import ProjectForm
# Create your views here.


def createProject (request,pk):

    form =ProjectForm()
    
    if request.method == 'POST':
        # print('FORM DATA:',request.POST)
        title=request.POST['title']
        print(title)    

        project.objects.create(title=title)
    # projects=project.objects.all()
    # print(projects)
    context={'form': form}
    return  render(request,'project.form.html',context)




def updateProject(request,pk):

    get=project.objects.get(id='55a7b050-fd9d-4f20-a297-75eb6668c380')
    form=ProjectForm(instance=get)


    if request.method=='POST':
        form=ProjectForm(request.POST,instance=get)
        print(request.POST['title'])
        get.title=request.POST['title']
        get.save()


    context={'form': form}
    return  render(request,'project.form.html',context)

def deleteProject(request,pk):

    get=project.objects.get(id='938fdf36-bd08-4001-b9a3-58d313eaf8d6')
    form=ProjectForm(instance=get)


    if request.method=='POST':
        get.delete()


    context={'form':form}
    return  render(request,'delete.html',context)
 
    