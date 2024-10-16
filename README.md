# lab-django
Lab de Django para workshop 

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
python manage.py startproject lista
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

Para testar o funcionamento da API, use o comando:
```bash
python manage.py runserver
```


