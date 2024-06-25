from ninja import Schema

class MonkeyBarMenuItemSchema(Schema):
    id: int
    product_title: str
    product_description: str
    product_cost: int
    product_stock: int
    amount_sold: int

class MonkeyBarEmployeeSchema(Schema):
    id: int
    name: str
    salary: int