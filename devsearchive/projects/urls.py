
from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects/<str:pk>',views.createProject,name="project_form_create"),
    path('update/<str:pk>',views.updateProject,name="project_form_update"),
    path('delete/<str:pk>',views.deleteProject,name="project_form_delete")
]
