from django.shortcuts import render
from .models import Button, ButtonCategory
# from .filters import BtnFilter


def home(request):
    # btn_categories = ButtonCategory.objects.all()
    btns = Button.objects.all()
    return render(request, 'main/button_info.html', {'btns': btns})
    # return render(request, 'main/button_info.html', {'btn_categories': btn_categories})


def btn_info(request, model_no):
    btn_categories = ButtonCategory.objects.all()
    return render(request, 'main/button_info.html', {'btn_categories': btn_categories})

#
# def search(request):
#     btn_list = Button.objects.all()
#     btn_filter = BtnFilter(request.GET, queryset=btn_list)
#     return render(request, 'main/search.html', {'filter': btn_filter})
