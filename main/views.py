from django.shortcuts import render
from .models import DishCategory
from django.http import HttpResponse


def index(request):
    categories = DishCategory.objects.filter(is_visible=True)
    context = {
        'categories': categories
    }
    return render(request,'main.html', context=context)
