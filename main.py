'''
1. Выполнить задание уровня light
2. Написать декоратор, замеряющий объем оперативной памяти, потребляемый
декорируемой функцией.
3. 4. Сравнить объем оперативной памяти для функции создания генератора и
функции создания списка с элементами: натуральные числа от 1 до 1000000.
'''
import time
import psutil
import os

def getMemory( f ):
    def wrapper( *args, **wargs ):
        p = psutil.Process( os.getpid() )
        m1 = p.memory_info().rss/1000000

        f( *args, **wargs )


        m2 = p.memory_info().rss / 1000000
        print( 'Функция ',f.__name__,'- память:', m2-m1 )

    return wrapper

@getMemory
def getList(n):
    lst = [x for x in range(1, n+1 )]
    return lst

@getMemory
def getGenList(n):
    for x in range(1, n + 1):
        yield x

getList(1000000)
getGenList(1000000)