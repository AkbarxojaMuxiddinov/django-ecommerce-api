# E-Commerce Backend API

Полноценный REST API для интернет-магазина, построенный на **Django**, **Django REST Framework (DRF)** и **SimpleJWT**.

## 🚀 Функционал
- **Accounts:** Регистрация, аутентификация через JWT (access/refresh токены).
- **Products & Categories:** Категории, каталог товаров и управление остатками.
- **Cart:** Персональная корзина для каждого пользователя с динамическим расчетом стоимости.
- **Orders:** Оформление заказа (checkout), автоматический перенос товаров из корзины и списание со склада.

## 🛠 Технологии
- Python 3.x
- Django & Django REST Framework
- djangorestframework-simplejwt
- SQLite / PostgreSQL

## 🏁 Инструкция по запуску

1. **Клонировать репозиторий:**
   ```bash
   git clone [https://github.com/ваш-username/название-репозитория.git](https://github.com/ваш-username/название-репозитория.git)
   cd название-репозитория