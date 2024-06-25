from django.shortcuts import render, redirect
from my_app.api import monkey_bar, monkeys
from my_app.models import MonkeyBarMenuItem


def index(request):
    menu_items = monkey_bar(request)
    employees = monkeys(request)

    if request.method == 'POST':
        customer_select_id = request.POST.get('customer_select')

        item = MonkeyBarMenuItem.objects.get(pk=customer_select_id)
        item.product_stock -= 1
        item.amount_sold += 1
        item.save()

        return redirect('index')
    
    comparison_numb = -1
    best_selling_item = None
    for item in menu_items:
        if item.amount_sold > comparison_numb:
            comparison_numb = item.amount_sold
            best_selling_item = [item.product_title, item.amount_sold]

    context = {
        'menu_items': menu_items,
        'monkeys': employees,
        'best_seller': best_selling_item
    }

    return render(request, 'my_app/index.html', context)