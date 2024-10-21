from rest_framework.views import APIView
from rest_framework.response import Response

from api.models import Task
from api.serializers import TaskSerializer


class BaseView(APIView):
    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self,request):
        pass
    
    

