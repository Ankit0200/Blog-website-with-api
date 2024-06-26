from django.urls import path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', views.home_blog, name='home'),
                  path('contact/', views.contact_blog.as_view(template_name='contact.html'), name='contact'),

                  path('about/', views.about_blog, name='about'),
                  path('show_blog/<int:id>', views.show_blog, name='show_blog'),
                  path('add_blog/', views.add_blog, name='add_blog'),
                  path('delete/<int:id>', views.delete_blog, name='delete'),
                  path('edit_blog/<int:id>', views.edit_blog, name='edit'),
                  path("blogapi/", views.BlogAPI.as_view(), name="blogapi")
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
