# How to join table in viewset

## Create simple relation in Serialize to map table

[REF](https://stackoverflow.com/questions/43197964/how-to-join-two-models-in-django-rest-framework)

## Django REST Framework API Join table using SerializeMethodField()

[REF](https://stackoverflow.com/questions/42775784/how-to-serialize-a-queryset-from-an-unrelated-model-as-a-nested-serializer?rq=1)

## Django REST Framework API Join Multiple Tables Using viewsets

[REF](https://www.youtube.com/watch?v=XsoCKDOalkw)

```Python
from app.serialzers import JoinTableSerialize
from app.models import JoinTableModel
from rest_framework import viewsets
from django.shortcust import render
from requests

class JoinTableApi(viewsets.ModelViewSet):
    queryset = JoinTableModel.objects.raw('select country.cid, country.cname, state.sname from country inner join ')
    serialzer_class = JoinTableSerialize

    def show(request):
        displaytable = request('http://127.0.0.1:8000/jointablemodel/')
        resutl = displaytables.json()
        return render(request, 'Index.html', ("Jointable":resutl))

```

## MULTIPLE Model Search in Django

[REF](https://www.youtube.com/watch?v=1wi0AHxjcn8)
