from rest_framework.views import APIView
from rest_framework.response import Response

from api.models import Task
from api.serializers import TaskSerializer
from rest_framework import status


class TaskView(APIView):
    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": {"note": serializer.data}}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    
    
class SingleTaskView(APIView):
    def get(self,request,id):
        task = Task.objects.get(id=id)
        serializer = TaskSerializer(task)
        return Response(serializer.data)
    def put(self,request,id):
        task = Task.objects.get(id=id)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": {"note": serializer.data}}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

