from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, status
from LeadApp.models import Lead
from LeadApp.serializers import LeadSerializer


class LeadsListView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        leads = [lead.name for lead in Lead.objects.all()]
        return Response(leads, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = LeadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
