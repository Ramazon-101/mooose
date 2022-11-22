from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('about/', about),
    path('blog/', articles),
    path('detail/<slug:slug>/', blog_detail),


]