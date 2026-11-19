from functools import wraps

def handle_errors(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args,**kwargs)
        except ZeroDivisionError:
            return 'Ошибка: деление на ноль'
        except ValueError:
            return 'Ошибка: некорректное значение'
        except Exception as e:
            return f'Произошла непредвиденная ошибка.{e}'
    return wrapper

@handle_errors
def devide(a,b):
    return(a/b)

print(devide(10,2))
print(devide(10,0))
print(devide(10,'s'))