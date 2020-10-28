from rest_framework.generics import ListAPIView

from .serializers import SoftwareSerializer
from .models import Software

class SoftwareAPI(ListAPIView):
    queryset=Software.objects.all() #select all elements
    serializer_class=SoftwareSerializer #convert to json