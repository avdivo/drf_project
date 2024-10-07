from django.urls import path
from .views import CategoryListCreateView, TransactionListCreateView

urlpatterns = [
    path('categories/', CategoryListCreateView.as_view()),  # Создание и получение категорий
    path('categories/<int:pk>/', CategoryListCreateView.as_view()),  # Редактирование и удаление категории
    path('transactions/', TransactionListCreateView.as_view()),  # Создание и получение транзакций
    path('transactions/<int:pk>/', TransactionListCreateView.as_view()),  # Редактирование и удаление транзакции
]