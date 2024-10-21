from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Task
from rest_framework import status
from .serializers import TaskSerializer

class TasksView(APIView):
    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": {"note": serializer.data}}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        
class SingleTaskView(APIView):
    def get(self, request, id):
        task = Task.objects.get(pk=id)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    
    def put(sekf, request, id):
        task = Task.objects.get(pk=id)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": {"note": serializer.data}}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        task = Task.objects.get(pk=id)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
