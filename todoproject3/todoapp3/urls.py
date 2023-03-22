from . import views
from django.urls import path
app_name='todoapp3'


urlpatterns = [
    path('',views.home,name='home'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
]
