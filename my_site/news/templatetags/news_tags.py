from django import template
from django.db.models import Count, F
from django.core.cache import cache

from news.models import Category


register = template.Library()


@register.simple_tag(name='get_list_categories')
def get_categories():
    """Возвращает все категории"""
    return Category.objects.all()


@register.inclusion_tag('news/list_categories.html')
def show_categories():
    """
    Возвращает список категории и показывает
    колличество новостей каждой категории
    Также показан пример работы с кэшем
    """
    # показывает колличество ВСЕХ не отсортированных новостей
    # categories = Category.objects.annotate(
    # cnt=Count('news')
    # ).filter(cnt__gt=0)

    # показывает колличество новостей, которые
    # отсортированы (опубликованы/не опубликованы)
    categories = cache.get('categories')
    if not categories:
        # пытаемся получить данные из кэша, если их
        # там нет, мы добаляем их в кэш из БД
        categories = Category.objects.annotate(cnt=Count(
            'news', filter=F('news__is_published'))
        ).filter(cnt__gt=0)
        categories.set('categories', categories, 30)
    return {"categories": categories}
