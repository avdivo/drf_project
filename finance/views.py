from rest_framework.viewsets import ModelViewSet
from .models import Category, Transaction
from .serializers import CategorySerializer, TransactionSerializer

# ViewSet для работы с категориями
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# ViewSet для работы с транзакциями
class TransactionViewSet(ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
