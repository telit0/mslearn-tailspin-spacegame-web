from rest_framework.generics import ListAPIView

from .serializers import SoftwareSerializer,SoftwareInstallInfo
from .models import Software

class SoftwareAPI(ListAPIView):
    queryset=Software.objects.all() #select all elements
    serializer_class=SoftwareSerializer #convert to json
    

class SoftwareInfo(ListAPIView):
    serializer_class=SoftwareInstallInfo
    def get_queryset(self):
        id=self.kwargs['id']
        queryset=Software.objects.filter(id=id)
        return queryset