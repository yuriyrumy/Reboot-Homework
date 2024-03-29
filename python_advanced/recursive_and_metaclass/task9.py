# Напишіть метаклас, який буде перейменовувати всі атрибути, назва яких починається з '__' на атрибути '__private_{attr}

class RenamePrivateAttr(type):
    def __new__(cls, cls_name, bases, attrs):
        rename_private_attr = dict()
        for name, value in attrs.items():
            if name.startswith(f'_{cls_name}__') and not name.endswith('__'):
                new_attr_name = f'__private_{name[len(cls_name) + 3:]}'
                rename_private_attr[new_attr_name] = value
            else:
                rename_private_attr[name] = value
        # print(attrs)
        # print(rename_private_attr)
        return super().__new__(cls, cls_name, bases, rename_private_attr)


class MyClass(metaclass=RenamePrivateAttr):
    __balance = 100
