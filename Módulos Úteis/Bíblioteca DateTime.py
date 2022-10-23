import datetime

dir(datetime)
print(dir(datetime))

"""Agora vamos ver os métodos da classe datetime"""
datetime.date.today()  # Retorna a data atual
print(datetime.date.today())


datetime.datetime.now()  # Retorna a data e hora atual
print(datetime.datetime.now())

datetime.datetime.now().year  # Retorna o ano atual
print(datetime.datetime.now().year)

datetime.datetime.now().month  # Retorna o mês atual
print(datetime.datetime.now().month)

datetime.datetime.now().day  # Retorna o dia atual
print(datetime.datetime.now().day)

datetime.datetime.now().hour  # Retorna a hora atual
print(datetime.datetime.now().hour)


data = datetime.date(2020, 7, 10)  # Cria uma data
print(data)

data.strftime('%d/%m/%Y')  # Formata a data
print(data.strftime('%d/%m/%Y'))

data.strftime('%A %B %Y')  # Formata a data
print(data.strftime('%A %B %Y'))

data.strftime('%A %B %Y %H:%M:%S')  # Formata a data
print(data.strftime('%A %B %Y %H:%M:%S'))

data.day  # Retorna o dia
print(data.day)

data.month  # Retorna o mês
print(data.month)

data.year  # Retorna o ano
print(data.year)

data.weekday()  # Retorna o dia da semana
print(data.weekday())

data.isoweekday()  # Retorna o dia da semana
print(data.isoweekday())

horario = datetime.datetime(2020, 7, 10, 15, 30, 20)  # Cria um horário e data
print(horario)

horario.strftime('%d/%m/%Y %H:%M:%S')  # Formata o horário e data
print(horario.strftime('%d/%m/%Y %H:%M:%S'))

horario.hour  # Retorna a hora
print(horario.hour)

horario.minute  # Retorna o minuto
print(horario.minute)

horario.second  # Retorna o segundo
print(horario.second)

horario.microsecond  # Retorna o microsegundo
print(horario.microsecond)
