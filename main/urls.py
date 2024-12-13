from django.urls import path
from .  import views
urlpatterns = [
    path('', views.baseFunc, name='homepage'),
    path('contact/', views.ContactView.as_view(), name='contact_page'),
    path('first/', views.first, name='first_page'),
    path('portfolio/', views.NewProject, name='new_project_page'),
    path('blog/', views.only_Blog, name='blog_page'),
    path('blog_detail/', views.Hello_Blog, name='blog_detail_page'),
    path('project_detail/', views.project_detail, name='project_detail_page'),
]