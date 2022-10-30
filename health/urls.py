from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('aboutus/', views.aboutus, name="aboutus"),
    path('services/', views.services, name="services"),
    path('testimonials/', views.testimonials, name="testimonials"),
    path('findus/', views.findus, name="findus"),
    path('faq/', views.faq, name="faq"),
    path('blogpost/', views.blogpost, name="blogpost"),
    path('gallery/', views.gallery, name="gallery"),
    path('blog/', views.blog, name="blog"),
    path('blogadd/', views.blogadd, name="blogadd"),
    path('blogdelete/<str:id>', views.blogdelete, name="blogdelete"),
    path('blogupdate/<str:id>', views.blogupdate, name="blogupdate"),
    path('contact/', views.contact, name="contact"),
    path('contactadd/', views.contactadd, name="contactadd"),
    path('login/', views.login_users, name="login"),
    path('logout/', views.logout_users, name="logout"),
    path('signup/', views.signup_users, name="signup"),
    path('login/', include("django.contrib.auth.urls")),
]

