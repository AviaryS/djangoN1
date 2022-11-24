from django.contrib import admin
from django.urls import path
from Arseniy import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home', kwargs={'fullName': 'Муратов Арсенйи Дмитриевич', 'age': '16 лет', 'interests': 'Люблю кодить!'}),
    path('about/', views.about, name='about', kwargs={'home': 'Гусь-Хрустального', 'estimates': 'получал 4-5', 'isLikeStudy': 'Обожаю учиться'}),
    path('contacts/', views.contacts, name='contacts', kwargs={'github': 'https://github.com/AviaryS', 'tg': '@AviaryS'})
]
