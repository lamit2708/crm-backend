# How to add api endpoint

[ref](https://bezkoder.com/django-postgresql-crud-rest-framework/)
[REF2](https://dev.to/nobleobioma/build-a-crud-django-rest-api-46kc)

## Create Your Model

```Python
from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Author(models.Model):
  name = models.CharField(max_length=200)
  added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  created_date = models.DateTimeField(default=timezone.now)

  def __str__(self):
    return self.name

class Book(models.Model):
  title = models.CharField(max_length=200)
  description = models.CharField(max_length=300)
  author = models.ForeignKey(Author, on_delete=models.CASCADE)
  added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  created_date = models.DateTimeField(default=timezone.now)

  def __str__(self):
    return self.title
```

## Add to Admin bookstore_app/api/admin.py

```Python
from django.contrib import admin
from .models import Author, Book



admin.site.register(Author)
admin.site.register(Book)
```

## Create Super Admin

```bash
python manage.py createsuperuser
```

## Create Serialize bookstore_app/api/serializers.py

```Python
from rest_framework import serializers
from .models import Author, Book

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'added_by', 'created_by']

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'description', 'created_date', 'author', 'added_by']
```

## Add Views for get API

```Python
# ./bookstore_app/api/views.py
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def welcome(request):
content = {"message": "Welcome to the BookStore!"}
return JsonResponse(content)
```

```Python
./bookstore_app/api/views.py
from .serializers import BookSerializer
from .models import Book
from rest_framework import status


@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def get_books(request):
    user = request.user.id
    books = Book.objects.filter(added_by=user)
    serializer = BookSerializer(books, many=True)
    return JsonResponse({'books': serializer.data}, safe=False, status=status.HTTP_200_OK)

```

## User can add a book ./bookstore_app/api/views.py

```Python
from .models import Book, Author
import json
from django.core.exceptions import ObjectDoesNotExist

@api_view(["POST"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def add_book(request):
    payload = json.loads(request.body)
    user = request.user
    try:
        author = Author.objects.get(id=payload["author"])
        book = Book.objects.create(
            title=payload["title"],
            description=payload["description"],
            added_by=user,
            author=author
        )
        serializer = BookSerializer(book)
        return JsonResponse({'books': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
```

## User can update a book entry by id

```Python
# ./bookstore_app/api/views.py


@api_view(["PUT"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def update_book(request, book_id):
    user = request.user.id
    payload = json.loads(request.body)
    try:
        book_item = Book.objects.filter(added_by=user, id=book_id)
        # returns 1 or 0
        book_item.update(**payload)
        book = Book.objects.get(id=book_id)
        serializer = BookSerializer(book)
        return JsonResponse({'book': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
```

```Python
# ./bookstore_app/api/views.py


@api_view(["DELETE"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def delete_book(request, book_id):
    user = request.user.id
    try:
        book = Book.objects.get(added_by=user, id=book_id)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
```

## Add URL

File urls.py

```bash
from django.urls import include, path
from . import views

urlpatterns = [
  ...
  path('getbooks', views.get_books),
  path('addbook', views.add_book),
  path('updatebook/<int:book_id>', views.update_book),
  path('deletebook/<int:book_id>', views.delete_book)
]
```

## Add Custom Router for API

[REF](https://stackoverflow.com/questions/21508982/add-custom-route-to-viewsets-modelviewset)

```Python
class CustomerTransferViewSet(viewsets.ViewSet):
    serializer_class = CustomerTransferSerializer
    queryset = CustomerTransfer.objects.all()
    @list_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def api_with_custom_route(self, request, *args, **kwargs):
        queryset = models.Highlight.objects.all()

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
```

Update with new way
Having default routers from the DRF tutorial will allow you to access this route with:
localhost:8000/snippets/<int:pk>/custom_action/>

```Python
from rest_framework.decorators import action


class SnippetViewSet(viewsets.ModelViewSet):
    ...

    @action(detail=True, methods=['POST'], name='Attach meta items ids')
    def custom_action(self, request, pk=None):
        """Does something on single item."""
        queryset = Snippet.objects.get(pk=pk)
        serializer = self.get_serializer(queryset, many=False)
        return Response(serializer.data)
```

If you have ad-hoc methods that you need to be routed to, you can mark them as requiring routing using the @detail_route or @list_route decorators.

The @detail_route decorator contains pk in its URL pattern and is intended for methods which require a single instance. The @list_route decorator is intended for methods which operate on a list of objects.

The decorators can additionally take extra arguments that will be set for the routed view only. For example...

```Python
    @detail_route(methods=['post'], permission_classes=[IsAdminOrIsSelf])
    def set_password(self, request, pk=None):
```

Theses decorators will route GET requests by default, but may also accept other HTTP methods, by using the methods argument. For example:

```Python
    @detail_route(methods=['post', 'delete'])
    def unset_password(self, request, pk=None):
```

The two new actions will then be available at the urls ^users/{pk}/set_password/$ and ^users/{pk}/unset_password/$

## Full action Viewset

```Python
class SnippsetViewSet(viewsets.ModelViewSet):
    # list, create, retrieve, update, partial_update, destroy
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
```

## Get the lastest one

[REF](https://www.youtube.com/watch?v=riZYgLOYq4g)

```Python
from rest_framework.decorators import action
from rest_framework.response import Response
class SnippetViewset(viewsets.ModelViewSet):
    queryset = Snippet.object.all()
    serializer_class = SnippetSerializer

    @action(method = ['get'], detail = False)
    def newest(self, request):
        newest = self.get_queryset().order_by('created').last()
        serializer = self.get_serializer_class()(newest)
        return Response(serializer.data)
```

## List

```Python
class SnippetViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Snippet.objects.all()
        serialzer = SnippetSerializer(queryset, many= True)
        return Response(serialzier.data)
```
