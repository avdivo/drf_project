from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Category, Transaction
from .serializers import CategorySerializer, TransactionSerializer

# ViewSet для работы с категориями
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()  # Получаем все категории
    serializer_class = CategorySerializer  # Указываем сериализатор для категорий
    permission_classes = [IsAuthenticatedOrReadOnly]  # Разрешаем просмотр всем, запись только аутентифицированным

# ViewSet для работы с транзакциями
class TransactionViewSet(ModelViewSet):
    queryset = Transaction.objects.all()  # Получаем все транзакции
    serializer_class = TransactionSerializer  # Указываем сериализатор для транзакций
    permission_classes = [IsAuthenticatedOrReadOnly]  # Разрешаем просмотр всем, запись только аутентифицированным