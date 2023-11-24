from django.urls import path
from . import views
from login_page.views import login_page

urlpatterns = [
    path('home',views.home,name='home'),
    path('contact',views.contact),
    path('shop',views.shop),
    path('why',views.why),
    path('testimonial',views.testimonial),
    path('logout',view=views.logout_fun)
]