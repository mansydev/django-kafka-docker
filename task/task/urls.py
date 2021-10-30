from django.contrib import admin
from django.urls import path, include
# from mcq_test.views import *

urlpatterns = [
    path('admins/', admin.site.urls),
    path('', include('mcq_test.urls', namespace="mcq_test")),
    path('score/', include('score.urls', namespace="score")),
]
