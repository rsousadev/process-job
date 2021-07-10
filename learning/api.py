
from rest_framework import viewsets, pagination
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import AddressSerializer, StudentSerializer
from .models import Address, Student


class MyPagination(pagination.PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 50
    

class AddresViewSet(viewsets.ModelViewSet):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()
    pagination_class = MyPagination
    filterset_fields = ['zip', 'address', 'neighborhood', 'city', 'state']

class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    pagination_class = MyPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'name', 'enrollment_date', 'school_year', 'gender', 'birth_date']
