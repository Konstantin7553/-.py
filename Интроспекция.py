def introspection_info(obj):
    info = {}
    info['тип'] = type(obj).__name__
    all_atributes = dir(obj)
    atributes = []
    methods = []

    for attr in all_atributes:
        try:
            attr_value = getattr(obj, attr)
            if callable(attr_value):
                methods.append(attr)

            else:
                atributes.append(attr)
        except:
            continue
    info['атрибуты'] = atributes
    info['методы'] = methods
    info['модуль'] = obj.__mod__
    return info

number_info = introspection_info(42)
print(number_info)


