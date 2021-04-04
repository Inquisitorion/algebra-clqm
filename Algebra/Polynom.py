
from .Rational import *

__all__ = ["Polynom"]

class Polynom():

    # _coef - массив коэффициентов начиная с большего и заканчивая меньшим
    # _coef_n - количество коэффициентов
    def __init__(self, l: list = None):
        if l is None:
            self._coef = []
            self._coef_n = 0
        else:
            self._coef = [Rational(str(i)) for i in l[::-1]]
            self._coef_n = len(l)

    # TO DO:
    # Пофиксить вывод отрицательных коэффициентов
    def __str__(self):
        s = ""
        for i in range(self._coef_n - 1, -1, -1):
            if i != 0:
                s += str(self._coef[i]) + f"x^{i} + "
            else:
                s += str(self._coef[i])
        return s

    def power(self):
        '''Модуль DEG_P_N выполнил и оформил Солодков Никита'''
        return self._coef_n - 1

    def higher_coef(self):
        '''Модуль LED_P_Q выполнил и оформил Шабров Иван'''
        return self._coef[-1]

    # КОД НЕ РАБОТАЕТ
    '''
    def mul_xk(self, k: int):
        #Модуль MUL_Pxk_P выполнила и оформила Реброва Юлия
        b = Polynom(self._coef_n + k)
        b._coef = [0 * (self._coef_n + k)]
        for i in range(self._coef_n):
            b._coef[i] = self._coef[i]
        return b
    '''

    def mul_q(self, num):
        ''' Выполнил Адиль Жексенгалиев'''
        # Модуль P-3
        res = Polynom()
        res._coef_n = self._coef_n
        res._coef = [Rational("1") for i in range(res._coef_n)]
        for i in range(self._coef_n):
            res._coef[i]._numerator = self._coef[i]._numerator * num._numerator
            res._coef[i]._denumerator = self._coef[i]._denumerator * num._denumerator
        return res

    def derivate(self):
        res = Polynom(list(self._coef))
        for i in range(len(self._coef)-1):
            res._coef[i] = self._coef[i+1]*(i+1)
        res._coef = res._coef[:len(self._coef)-1]
        self._coef_n -= 1
        return res