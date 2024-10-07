# finance/models.py

from django.db import models

# Модель для категорий доходов и расходов
class Category(models.Model):
    CATEGORY_TYPES = (
        ('income', 'Доход'),  # Категория доходов
        ('expense', 'Расход'),  # Категория расходов
    )

    name = models.CharField(max_length=100)  # Название категории
    category_type = models.CharField(max_length=7, choices=CATEGORY_TYPES)  # Тип: доход или расход

    def __str__(self):
        return f'{self.name} ({self.get_category_type_display()})'
        # Метод __str__ возвращает строковое представление объекта, полезно для отображения в админке

# Модель для транзакций
class Transaction(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # Связываем транзакции с категориями
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Сумма транзакции
    description = models.TextField(null=True, blank=True)  # Описание транзакции (опционально)
    date = models.DateField(auto_now_add=True)  # Дата создания транзакции, автоматически ставится при создании

    def __str__(self):
        return f'{self.category.name}: {self.amount} ({self.date})'
        # Здесь мы показываем название категории и сумму транзакции в строковом представлении