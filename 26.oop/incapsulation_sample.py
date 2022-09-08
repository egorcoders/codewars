'''
Инкапсуляция это сокрытие атрибутов и методов от пользователя. Для этого
используются 3 вида доступа: public, _protected, __private. В Python она
условна, т.к. существует backdoor: class_sample()._Class__method_name().
Чтобы реально защитить данные нужно использовать модуль accessify
@protected, @private. Поскольку это защита на уровне конвенций, при
наличии protected атрибутов / классов мы испольуем их только внутри класса.
'''


#  1st sample
class Car:
    def drive(self):
        print('Car is driving')
        self.__wheels()
        self._motor()

    def check_wheels(self):
        self.__wheels()

    def __wheels(self):
        print('Wheels are turning')

    def _motor(self):
        print('Motor is working')


# c = Car()
# print(dir(c))
# c._motor()  # доступ снаружи
# c.check_wheels()  # доступ изнутри
# c._Car__wheels()  # доступ backdoor


#  2d sample


