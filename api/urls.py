from django.urls import include, re_path  
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns=[
    re_path(r'^api/mercaderia/$',views.MercaderiaViewSet.as_view()),
]
