# lab-django
Lab de Django para workshop 

**Importante:** Sempre ao aplicar um comando usando o manage.py. Certifique-se de estar no diretório do seu projeto.
## Primeiro passo
Primeiramente, abra o terminal segurando a tecla WINDOWS + r, digite `cmd` na janela que abrir e aperte ENTER 
No terminal, teste se o python e o pip estão instalados:
```bash
python --version && pip --version
```
## Segundo passo
Vamos criar uma pasta clicando com o botão direito na área de trabalho, em seguida vamos navegar até a pasta que criamos com o comando:
```bash
 cd Desktop/[nome da pasta que você criou]
```

Agora vamos criar um ambiente virtual para nosso projeto, instale a biblioteca `virtualenv` com o seguinte comando:
```bash
pip install virtualenv
```
Após a instalação ser concluída, vamos iniciar um ambiente virtual:
```bash
python -m venv venv
```
Por fim, precisamos ativar nosso ambiente virtual. Para isso, ativamos com o seguinte comando:
```bash
venv\Scripts\activate
```
Após a ativação, você deverá ver `(venv)` na frente do caminho do seu terminal.

## Terceiro passo
Agora vamos instalar django e o rest framework
```bash
pip install django
```
```bash
pip install djangorestframework
```

## Quarto passo
Criar o projeto django com o comando:
```bash
 django-admin startproject backend
```
Conecte o rest_framework no arquivo `settings.py`

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework' #Adicione isso à lista
]
```

## Quinto passo
Crie a aplicação `api` com o comando:
```bash
python manage.py startapp api
```
Adicione `API` à `settings.py`
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'api' #Adicione isso
]
```

## Sexto passo 
Na pasta da sua aplicação `api`, crie um arquivo chamado `urls.py`
Esse arquivo vai ser destinado à conectar as views nas rotas

## Sétimo passo
Conectar as urls do projeto às urls da aplicação 
Para isso, no arquivo `urls.py` do seu PROJETO, importe a seguinte função
```python
from django.urls import path, include
```
Em seguida, adicione à lista `urlpatters` o seguinte elemento:
```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls'))
]
```

## Testando uma View
Crie uma função (view) no arquivo `views.py` da sua aplicação
```python
from rest_framework.views import APIView
from rest_framework.response import Response

class BaseView(APIView):
    def get(self, request):
        return Response("Hello World")
```

Antes de tester a view, mapeie-a no arquivo `urls.py` da sua APLICAÇÃO.
```python
from django.urls import path
from .views import BaseView

urlpatterns = [
    path('', BaseView.as_view())
]

```

Para testar o funcionamento da API, use o comando:
```bash
python manage.py runserver
```
**Importante** -> Para acessar a sua view, a url deve conter /api no final. 

## Oitavo Passo
Criar os models (banco de dados) 
No arquivo `models.py` na pasta de sua aplicação. Crie a seguinte tabela: 
```python
from django.db import models

# Create your models here
class Task(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=100)
    due_to = models.DateTimeField(blank=True, auto_now=False)
    is_completed = models.BooleanField()

    def __str__(self):
        return self.name

```
No terminal, use os comandos:
```bash
  python manage.py makemigrations
```
```bash
  python manage.py migrate
```
Agora , o seu banco de dados SQLite foi gerado.

## Usando o ADMIN

Para usar o admin, é necessário criar um superuser com o seguinte comando:

```bash
  python manage.py createsuperuser
```
Será necessário informar um nome de usuário, email e senha.

No arquivo `admin.py` , cadastre os seus models á plataforma.
```python
from django.contrib import admin
from .models import Task

# Register your models here.
admin.site.register(Task)
```

Agora, aplique o comando: 
```bash
python manage.py runserver
```

Para acessar a interface ADMIN, use a URL /admin
## Criando as views
Agora vamos criar as views para servir os dados do nosso modelo
## View para servir todas as tarefas de um usuário
Criamos uma classe e dois métodos, um para o método GET e um POST
```python
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

```
## View para servir uma tarefa específica
Vamos adicionar a lógica para trabalhar com uma tarefa baseada em seu id. Nessa classe disponibilizaremos os métodos GET, PUT, PATCH e DELETE
```python
class SingleTaskView(APIView):
    def get(self, request, id):
        task = get_object_or_404(Task, pk=id)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    
    def put(self, request, id):
        task = get_object_or_404(Task, pk=id)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": {"note": serializer.data}}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        task = get_object_or_404(Task, pk=id)
        serializer = TaskSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        task = get_object_or_404(Task, pk=id)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
```
## Criando as rotas
Agora que temos as views, podemos associá-las a endpoints da seguinte maneira:
```python
from django.urls import path
from .views import BaseView

urlpatterns = [
    path('', TaskView.as_view()), #Para o endpoint http://127.0.0.1:8000/api
    path(/<id>, SingleTaskView.as_view()) #Para o endpoint http://127.0.0.1:8000/api/<id>
]

```