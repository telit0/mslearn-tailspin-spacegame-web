from rest_framework.generics import ListAPIView
from django.http import JsonResponse
from django.core import serializers

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

    def get_param(id):
        #data=list(Software.objects.filter(id=id))
        data=list(Software.objects.filter(id=id).values('id','name','displayName','publisher','description','detectionRules','returnCodes','installStr','uninstallStr','srcFile'))
        #data=Software.objects.filter(id=id)
        return JsonResponse(data,safe=False)
        #return JsonResponse(SoftwareInstallInfo(data),safe=False)