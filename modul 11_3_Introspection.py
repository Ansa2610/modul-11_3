def introspection_info(obj):
	# Тип объекта
	obj_type = type(obj).__name__

	# Атрибуты объекта
	attributes = [at for at in dir(obj) if not callable(getattr(obj, at))]

	# Методы объекта
	methods = [method for method in dir(obj) if callable(getattr(obj, method))]

	# Модуль, к которому объект принадлежит
	module = obj.__class__.__module__

	# Словарь с информацией об объекте
	my_dic = {
		'type':obj_type,
		'attributes': attributes,
		'methods':methods,
		'modul': module,
	}

	return my_dic

number_info = introspection_info(42)
print(number_info)
