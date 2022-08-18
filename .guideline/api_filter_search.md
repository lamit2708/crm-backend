# How to implement the filter for django api

## custom 1

[REF](https://sunscrapers.com/blog/the-ultimate-tutorial-for-django-rest-framework-filtering-part-5/)

## Custom 2

[REF](https://stackoverrun.com/vi/q/4720196)

```Python
from django.shortcuts import get_list_or_404

def get_queryset(self):
       filter = {}
       filter['issue_id'] = self.kwargs['issue_id']
       return get_list_or_404(self.queryset, **filter)
```

```Python
class OrdersByCustomer(generics.ListCreateAPIView):
       queryset = Order.objects.all()
       serializer_class = OrderSerializer

       def get_queryset(self):
           customer_pk = self.kwargs['customer_pk']
           return self.queryset.filter(customer__pk=customer_pk)

       def pre_save(self, obj):
           obj.customer_id = self.kwargs['customer_pk']
```

## Custom 3

[REF](https://docs.djangoproject.com/en/3.1/ref/models/querysets/)

## Filter use Operator OR AND

[REF](https://stackoverflow.com/questions/739776/how-do-i-do-an-or-filter-in-a-django-query)
