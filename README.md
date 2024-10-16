# lab-django
Lab de Django para workshop 

**Importante:** Sempre ao aplicar um comando usando o manage.py. Certifique-se de estar no diretório do seu projeto.
## First-Step 
Criar o ambiente virtual e instalar django e rest framework
```bash
pip install django
```
```bash
pip install djangorestframework
```

## Segundo passo
Criar o projeto django com o comando:
```bash
 django-admin startproject lista
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

## Terceiro passo
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

## Quarto passo 
Na pasta da sua aplicação `api`, crie um arquivo chamado `urls.py`
Esse arquivo vai ser destinado à conectar as views nas rotas

## Quinto passo
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

## Sexto Passo
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


