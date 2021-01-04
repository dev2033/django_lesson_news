from django import forms
from django.core.exceptions import ValidationError

# from .models import Category
from .models import News

import re


class NewsForm(forms.ModelForm):
    """Форма для добавления новости на сайт"""
    class Meta:
        model = News
        # fields = '__all__'
        fields = ['title', 'content', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control"}),
            'content': forms.Textarea(attrs={"class": "form-control",
                                             'rows': 5}),
            'category': forms.Select(attrs={"class": "form-control"})
        }

    def clean_title(self):
        """
        Кастомный валидатор.
        Получаем очищенные данные и проверяем чтобы название
        новости не начилось с числа
        """
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Название не должно называться с цифры')
        return title

    # """
    # Форма для добавление новости на сайт.
    # Форма не связанная с моделью
    # """
    # title = forms.CharField(max_length=150, label='Название',
    #                         widget=forms.TextInput(attrs={
    #                             "class": "form-control"
    #                         }))
    # content = forms.CharField(label='Текст', required=False,
    #                           widget=forms.Textarea(attrs={
    #                             "class": "form-control",
    #                             "rows": 5,
    #                             }))
    # is_published = forms.BooleanField(label='Опубликовано', initial=True)
    # category = forms.ModelChoiceField(queryset=Category.objects.all(),
    #                                   label='Категория',
    #                                   empty_label='Выберите категорию',
    #                                   widget=forms.Select(attrs={
    #                                       "class": "form-control"
    #                                   }))
