class Category:
    name: str
    description: str
    goods: list

    count_of_categories = 0
    count_of_unique_goods = 0

    def __repr__(self):
        return f"{self.name}, {self.description}, {self.goods}"

    def __init__(self, name: str, description: str, goods: list):
        self.name = name
        self.description = description
        self.goods = goods

        Category.count_of_categories += 1
        Category.count_of_unique_goods += len(self.goods)
