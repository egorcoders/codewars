'''
Инкапсуляция это сокрытие методов от пользователя. Для этого используются
3 вида доступа: public, __private, _protected. В Python она условна, т.к.
существует backdoor: class_sample()._Class__method_name(). Чтобы реально
защитить данные нужно использовать модуль accessify @protected, @private.
'''


#  1st sample
class Car:
    def drive(self):
        print('Car is driving')
        self.__wheels()
        self._motor()

    def __wheels(self):
        print('Wheels are turning')

    def _motor(self):
        print('Motor is working')


# c = Car()
# print(dir(c))
# c._Car__wheels()


#  2d sample
