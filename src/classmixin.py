class ClassMixin:

    def print_repr(self):
        """
        Выводит в консоль сообщение о создании экзэмпрляра класса и его атрибуты.
        """

        print(f"Создан экземпляр класса {repr(self)}")
        return
