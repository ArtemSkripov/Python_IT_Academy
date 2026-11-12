# Задание 2
# Создайте декоратор ignore_duplicates, который не позволяет
# выполнить функцию два раза подряд с одинаковыми
# аргументами.
# Пример:
# @ignore_duplicates
# def send_message(text):
# print(f"Отправлено: {text}")
# Вызовы
# send_message("Привет")
# send_message("Привет")
# send_message("Как дела?")
# send_message("Как дела?")
# send_message("Привет")
# должны вывести
# Отправлено: Привет
# Повторный вызов проигнорирован.
# Отправлено: Как дела?
# Повторный вызов проигнорирован.
# Отправлено: Привет

def ignore_duplicates(func):
  prev = None

  def wrapper(*args, **kwargs):
    nonlocal prev
    if prev == (args, kwargs):
      print("Повторный вызов проигнорирован.")
      return
    prev = (args, kwargs)
    return func(*args, **kwargs)

  return wrapper
