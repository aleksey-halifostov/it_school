inputdata = ['Страна', 'шалаш', 'Летел', 'вертолёт', 'УЧУ', 'мэм', 'язык']

data = list(filter(lambda elem: elem.upper() == elem[::-1].upper(), inputdata))

print(data)
