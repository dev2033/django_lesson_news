"""
Весь закоментированный код представлений является альтернативой
кода представлений на основе классов
"""
# from django.shortcuts import render, get_object_or_404, redirect
# from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import News, Category
from .forms import NewsForm


class HomeNews(ListView):
    """
    Выводит все новости на главной странице.
    Метод select_related('category'), сокращает колличество
    запросов к БД, объединяя множество sql запросов в 1 сложный.
    Также можно использовать атрибут queryset, указывая
    Модель.Объекты.select_related(и название связи)
    """
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    paginate_by = 4

    # queryset = News.objects.select_related('category')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related('category')


# def index(request):
#     news = News.objects.all()
#     context = {
#         'news': news,
#         'title': 'Список новостей',
#     }
#     return render(request, template_name='news/index.html', context=context)


class NewsByCategory(ListView):
    """
    Выводит категории новости
    Метод select_related('category'), сокращает колличество
    запросов к БД, объединяя множество sql запросов в 1 сложный
    """
    model = News
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'],
                                   is_published=True).select_related('category')


# def get_category(request, category_id):
#     """"""
#     news = News.objects.filter(category_id=category_id)
#     category = Category.objects.get(pk=category_id)
#     context = {
#         'news': news,
#         'category': category
#     }
#     return render(request, template_name='news/category.html', context=context)


class ViewNews(DetailView):
    """Показ новости"""
    model = News
    # pk_url_kwarg = 'news_id'

    # используется джангой по умолчанию
    # template_name = 'news/news_detail.html'
    context_object_name = 'news_item'


# def view_news(request, news_id):
#     # news_item = News.objects.get(pk=news_id)
#     news_item = get_object_or_404(News, pk=news_id)
#     context = {
#         "news_item": news_item,
#     }
#     return render(request, 'news/view_news.html', context=context)


class CreateNews(LoginRequiredMixin, CreateView):
    """Создание новости"""
    form_class = NewsForm
    template_name = 'news/add_news.html'
    # нужна для редиректа на какой то url после добавлений новости
    # (если в моделях не используется get_absolute_url)

    # success_url = '/'

    # также можно использовать функцию reverse_lazy - ленивый url reverse

    # success_url = reverse_lazy('home')

    # перекидывает пользователя на страницу авторизации для добавления новости
    # login_url = 'login/'

    # также можно вызывать исключение - доступ запрещен (403 ошибка)
    raise_exception = True


# def add_news(request):
#     if request.method == 'POST':
#         form = NewsForm(request.POST)
#         if form.is_valid():
#             # для формы не связаной с моделью
#             # news = News.objects.create(**form.cleaned_data)
#
#             # для формы связоной с моделью
#             news = form.save()
#             return redirect(news)
#     else:
#         form = NewsForm()
#     return render(request, 'news/add_news.html', {'form': form})
