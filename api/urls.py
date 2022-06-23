from django.urls import path,include
from .import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('datasetone', views.DatasetOneView)
router.register('datasetwo', views.DatasetTwoView)


urlpatterns = [
    path('',include(router.urls)),

]