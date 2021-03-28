from django.urls import include, path, re_path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'peaks', views.PeakViewSet)
router.register(r'records', views.RecordViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('docs', views.docs, name='docs'),
    path('map', views.map, name='map'),
    path('getrecords/<int:pk>', views.getrecords, name='getrecords'),
    re_path(r'^getpeakswithinBB\/(-?\d+\.\d+),(-?\d+\.\d+),(-?\d+\.\d+),(-?\d+\.\d+)', views.getpeakswithinBB,name='getpeakswithinBB')
]