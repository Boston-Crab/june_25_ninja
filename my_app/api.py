from ninja import NinjaAPI
from my_app.models import MonkeyBarMenuItem, MonkeyBarEmployee
from my_app.schema import (
    MonkeyBarEmployeeSchema,
    MonkeyBarMenuItemSchema
)
from typing import List


api = NinjaAPI()

@api.get("/monkey-bar", response=List[MonkeyBarMenuItemSchema])
def monkey_bar(request):
    menu_items = MonkeyBarMenuItem.objects.all()
    return menu_items

@api.get("/monkeys", response=List[MonkeyBarEmployeeSchema])
def monkeys(request):
    all_monkeys = MonkeyBarEmployee.objects.all()
    return all_monkeys