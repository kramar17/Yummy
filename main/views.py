from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import DishCategory, Dish, Gallery
from .forms import ReservationForm
from django.views.generic import TemplateView

from django.contrib.auth.decorators import login_required, user_passes_test


def is_manager(user):
    return user.groups.filter(name='manager').exists()


class IndexView(TemplateView):
    template_name = 'main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = DishCategory.objects.filter(is_visible=True)
        gallery = Gallery.objects.all()
        form = ReservationForm()

        context['title_menu'] = 'Check Our <span>Yummy Menu</span>'
        context['title_gallery'] = 'Check <span>Our Gallery</span>'
        context['categories'] = categories
        context['gallery'] = gallery
        context['form'] = form

        return context

    def post(self, request):
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ваше бронювання прийнято!')
            return redirect('main:index')


@login_required(login_url='/login/')
@user_passes_test(is_manager)
def manager(request):
    return HttpResponse('Manager page')