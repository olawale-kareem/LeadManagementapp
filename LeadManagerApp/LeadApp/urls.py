# from rest_framework import routers
# from .api import LeadViewSet

# router = routers.DefaultRouter()
# router.register("api/leads", LeadViewSet, 'leads')


# urlpattern = router.urls

from django.urls import path
from LeadApp.views import LeadsListView

urlpatterns = [
    path("leads/", LeadsListView.as_view(), name='leads-list'),
]
