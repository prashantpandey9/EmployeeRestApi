
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from webapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('employee/',views.employeeList.as_view()),
]
