from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .form import Cofee

def home(request):
    if request.method == 'POST':
        if 'Espresso' in request.POST:
            form = Cofee()
            f = form.milk01(1,0)
            mix = "กาแฟ 1 ช๊อต"
            args = {'mix': mix, }
            return render(request, 'app_mvc/home.html', args)
        elif 'Cappuccino' in request.POST:
            form = Cofee()
            f = form.milk01(1,1)
            mix = "กาแฟ 1 ช๊อต และนม 1 ช๊อต"
            args = {'mix': mix}
            return render(request, 'app_mvc/home.html', args)
        elif 'Latte' in request.POST:
            form = Cofee()
            f = form.milk01(1,2)
            mix = "กาแฟ 1 ช๊อต และนม 2 ช๊อต"
            args = {'mix': mix}
            return render(request, 'app_mvc/home.html', args)
        elif 'Americano' in request.POST:
            form = Cofee()
            f = form.milk01(1,0)
            mix = "กาแฟ 1 ช๊อต และน้ำร้อน 2 ช๊อต"
            args = {'mix': mix}
            return render(request, 'app_mvc/home.html', args)
        elif 'Summary' in request.POST:
            text01 = "จำนวนแก้ว"
            text02 = "ช๊อต"
            text03 = "กาแฟ"
            text04 = "นม"
            form = Cofee()
            f = form.milk01(0,0)
            args = {
                'cofee':f,
                'text01':text01,
                'text02':text02,
                'text03':text03,
                'text04':text04,
                }
            return render(request, 'app_mvc/home.html', args)
    else:
        return render(request, 'app_mvc/home.html')
