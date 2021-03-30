
__all__ = ["Natural"]

# TO DO:
# Создать отдельный файл для подобных функций?
def remove_char(s, n):
    return s[:n] + s[n + 1:]

class Natural():

    # _dig_n - количество разрядов в числе
    # _number - натуральное число, представленое в виде перевёрнутого массива цифр
    def __init__(self, n = None):
        self._number = []
        if n is None:
            self._dig_n = 0
        # Число состоит из нулей
        elif n == "0" * len(n):
            self._number = [0]
            self._dig_n = 1
        else:
            # Убираем все нули
            while n.find("0") != -1:
                n = remove_char(n, n.index("0"))
            self._number = [int(i) for i in n[::-1]]
            self._dig_n = len(self._number)

    def __reversed__(self):
        return reversed(self._number)

    def __str__(self):
        if self._dig_n != 0:
            # Перевод списка в строку
            return ''.join([str(i) for i in reversed(self._number)])
        else:
            return "0"


    def __gt__(self, num):
        '''Модуль переполнения ">". Оформил Шабров Иван'''
        if self._dig_n > num._dig_n:
            return True
        elif self._dig_n < num._dig_n:
            return False
        else:
            for i in range(-1, -(self._dig_n + 1), -1):
                if self._number[i] > num._number[i]:
                    return True
                elif self._number[i] < num._number[i]:
                    return False
        return False



    def __lt__(self, num):
        '''Модуль переполнения "<". Оформил Шабров Иван'''
        if self._dig_n < num._dig_n:
            return True
        elif self._dig_n > num._dig_n:
            return False
        else:
            for i in range(-1, -(self._dig_n + 1), -1):
                if self._number[i] < num._number[i]:
                    return True
                elif self._number[i] > num._number[i]:
                    return False
        return False

    def compare(self, num):
        '''Модуль COM_NN_D. Оформил Шабров Иван'''
        if self > num:
            return 2
        elif self < num:
            return 1
        else:
            return 0

    def __add__(self, num):
        '''Модуль ADD_NN_N. Оформил Крысиль Жексенгалиев'''
        #Сложение натуральных чисел
        res = Natural()
        if self.compare(num) == 1:
            res._dig_n = num._dig_n
            n = self._dig_n
        else:
            res._dig_n = self._dig_n
            n = num._dig_n
        res._number = [0 for i in range(res._dig_n)]
        i = 0
        while i < n:
            x = res._number[i] + self._number[i] + num._number[i]
            if x == 10:
                res._number[i] = 0
                #  расширение массива чисел
                if (i == res._dig_n - 1):
                    res._number.append(0)
                    res._dig_n += 1
                res._number[i + 1] += 1
                if res._number[i + 1] == 10:
                    res._number[i + 1] = 0
                    res._number[i + 2] += 1

            elif x > 10:
                res._number[i] = x - 10
                if (i == res._dig_n - 1):
                    res._number.append(0)
                    res._dig_n += 1
                res._number[i + 1] += 1
            else:
                res._number[i] += self._number[i] + num._number[i]

            i = i + 1
        # Для случая когда числа имеют разные разряды
        # Для случая когда числа имеют разные разряды
        # Для случая когда числа имеют разные разряды
        # подписюн
        j = 0
        while j < abs(self._dig_n - num._dig_n):
            # cтоит ли заменить метод  на переменную или оставить так для читаемости кода?
            if self.compare(num) == 2:
                res._number[j + i] += self._number[j + i]
            else:
                res._number[j + i] += num._number[j + i]
            if res._number[j + i] == 10:
                res._number[j + i] = 0
                if (j + i == res._dig_n - 1):
                    res._dig_n+=1
                    res._number.append(0)

                res._number[j + i + 1] += 1

            j = j + 1
        return res
