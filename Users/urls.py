from django.urls import path  
from Users import views
from django.conf.urls.static import static 
from django.conf import settings 

app_name = 'Users'
urlpatterns = [   
    path('', views.user_index,name='user_index'),  
    path('addnew',views.addnew),  
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.destroy),
    path('adminlogin/',views.Adminlogin,name='adminlogin')
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
