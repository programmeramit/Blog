from django.urls import path,include

from . import views

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('',views.home,name="home"),
    path('create/',views.create_post,name="create_post"),
    path('blog/<int:id>',views.post,name="blog"),
    path('login/', views.login_view, name='login'),
    path('logout/',views.logout_user,name="logout_user"),
    path('signup/',views.signup,name="signup"),



    path('ckeditor/', include('ckeditor_uploader.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
