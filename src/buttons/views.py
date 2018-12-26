from django.shortcuts import render
from .models import Button, ButtonCategory
# from .filters import BtnFilter


def home(request):
    btn_category = ButtonCategory.objects.all()
    return render(request, 'main/index.html', {'btn_category': btn_category})


def btn_info(request, model_no):
    btn_categories = ButtonCategory.objects.all()
    return render(request, 'main/button_info.html', {'btn_categories': btn_categories})

#
# def search(request):
#     btn_list = Button.objects.all()
#     btn_filter = BtnFilter(request.GET, queryset=btn_list)
#     return render(request, 'main/search.html', {'filter': btn_filter})
