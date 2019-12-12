from django.contrib import admin
from django.urls import path
from core.views import homepage, about

urlpatterns = [                         
    path('admin/', admin.site.urls),    # localhost:8000/admin/
    path('', homepage),                 # localhost:8000
    path('about/', about)               # localhost:8000/about/
]
