from rest_framework import serializers
from .models import Software

class SoftwareSerializer(serializers.ModelSerializer):
    class Meta:
        model=Software
        fields=['id','name','logo','publisher','description','version','parameters']

class SoftwareInstallInfo(serializers.ModelSerializer):
    class Meta:
        model=Software
        fields=['id','name','displayName','publisher','description','detectionRules','returnCodes','installStr','uninstallStr','srcFile']
