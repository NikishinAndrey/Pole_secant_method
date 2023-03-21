import matplotlib.pyplot as plt
import numpy as np


def fun_1(x):
    return x ** 4 + 3 * x ** 3 + 4 * x ** 2 + x - 3


def fun_2(x):
    return 3 * x - 4 * np.log(x) - 5


def der_1(x):
    return 4 * x ** 3 + 9 * x ** 2 + 8 * x + 1


def der_2(x):
    return 3 - 4 / x


def sec_der_1(x):
    return 12 * x ** 2 + 18 * x + 8


def sec_der_2(x):
    return 4 / (x ** 2)


N = 50
eps = 1e-15
a1_x = 0
b1_x = 1
a2_x = 2
b2_x = 4

epsilon_comp = 1e-16


#  Реализация метода половинного деления

def bisection(func, a, b, e, N):
    a_y = func(a)
    b_y = func(b)
    if a_y * b_y >= 0:
        return None
    result = []
    for i in range(N):
        c = 0.5 * (a + b)
        tol = 0.5 * (b - a)
        result.append(c)
        if tol < e:
            return c, tol, i, result
        fc = func(c)
        if abs(fc) < epsilon_comp:
            return c, tol, i, result
        if a_y * fc < 0:
            b = c
            b_y = fc
        else:
            a = c
            a_y = fc
    return c, tol, i, result


#  Реализация полюсного метода секущих

def pole_secant_method(func, func_der, func_sec_der, a, b, e, N):
    a_y = func(a)
    b_y = func(b)
    if a_y * b_y >= 0:
        return None
    result = []
    sec_der_y = func_sec_der(a)
    if a_y * sec_der_y > 0:
        x0 = a
    else:
        x0 = b
    x1 = x0 - func(x0) / func_der(x0)
    for i in range(N):
        coefficient = (func(x1) * (x0 - x1)) / (func(x0) - func(x1))
        x2 = x1 - coefficient
        tol = abs(coefficient)
        x0 = x1
        x1 = x2
        result.append(x2)
        if tol < e:
            return x2, tol, i, result
        if abs(func(x2)) < epsilon_comp:
            return x2, tol, i, result
    return x2, tol, i, result


etf = bisection(fun_1, a1_x, b1_x, eps, N)  # ElementsTupleFunction
list_1 = etf[3]
solve_1 = etf[0]
etf = bisection(fun_2, a2_x, b2_x, eps, N)
list_2 = etf[3]
solve_2 = etf[0]
etf = pole_secant_method(fun_1, der_1, sec_der_1, a1_x, b1_x, eps, N)
list_3 = etf[3]
solve_3 = etf[0]
etf = pole_secant_method(fun_2, der_2, sec_der_2, a2_x, b2_x, eps, N)
list_4 = etf[3]
solve_4 = etf[0]


def chart(solving, list):
    for i in range(len(list)):
        list[i] -= solving
        list[i] = abs(list[i])
    return list


def chart_help(list):
    new_list = []
    for i in range(len(list)):
        new_list.append(i + 1)
    return new_list


def chart2():
    epsilon = 1e-15
    list_epsilon = []
    list_etf1 = []
    list_etf2 = []
    list_etf3 = []
    list_etf4 = []
    for i in range(13):
        list_etf1.append(bisection(fun_1, a1_x, b1_x, epsilon, N)[2])
        list_etf2.append(bisection(fun_2, a2_x, b2_x, epsilon, N)[2])
        list_etf3.append(pole_secant_method(fun_1, der_1, sec_der_1, a1_x, b1_x, epsilon, N)[2])
        list_etf4.append(pole_secant_method(fun_2, der_2, sec_der_2, a2_x, b2_x, epsilon, N)[2])
        list_epsilon.append(epsilon)
        epsilon *= 10
    return list_epsilon, list_etf1, list_etf2, list_etf3, list_etf4


def chart3():
    list_bca1 = []  # bc = boundary condition
    list_bca2 = []
    list_bcb1 = []
    list_bcb2 = []
    list_num1 = []
    list_num2 = []
    a1 = -1
    b1 = 2
    a2 = 1.7
    b2 = 4.7
    for i in range(14):
        list_num1.append(bisection(fun_1, a1, b1, eps, N)[2])
        list_num2.append(bisection(fun_2, a2, b2, eps, N)[2])
        list_bca1.append(a1)
        list_bcb1.append(b1)
        a1 += 0.1
        b1 -= 0.1
        list_bca2.append(a2)
        list_bcb2.append(b2)
        a2 += 0.1
        b2 -= 0.1
    return list_num1, list_num2, list_bca1, list_bca2, list_bcb1, list_bcb2


def chart4():
    epsilon = 1e-16
    list_epsilon = []
    list_etf1 = []
    list_etf2 = []
    list_etf3 = []
    list_etf4 = []
    line = []
    for i in range(14):
        list_etf1.append(bisection(fun_1, a1_x, b1_x, epsilon, N)[1])
        list_etf2.append(bisection(fun_2, a2_x, b2_x, epsilon, N)[1])
        list_etf3.append(pole_secant_method(fun_1, der_1, sec_der_1, a1_x, b1_x, epsilon, N)[1])
        list_etf4.append(pole_secant_method(fun_2, der_2, sec_der_2, a2_x, b2_x, epsilon, N)[1])
        list_epsilon.append(epsilon)
        epsilon *= 10
    return list_epsilon, list_etf1, list_etf2, list_etf3, list_etf4


plt.figure(1)
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.title("График алгебраической функции")
x1 = np.linspace(a1_x, b1_x, 1000)
y1 = fun_1(x1)
plt.plot(x1, y1, label=f'$x^4 + 3x^3 + 4x^2 + x - 3$')
plt.legend()
plt.figure(2)
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.title("График трансцендентной функции")
x2 = np.linspace(a2_x, b2_x, 1000)
y2 = fun_2(x2)
plt.plot(x2, y2, color='r', label=f'$3x - 4lnx - 5$')
plt.legend()
plt.figure(3)
plt.grid()
plt.xscale('log')
plt.xlabel('точность')
plt.ylabel('количество итераций')
plt.title("График зависимости количества итераций от задаваемой точности")
plt.plot(chart2()[0], chart2()[1], label='Метод половинного деления для алгебраической функциии')
plt.plot(chart2()[0], chart2()[2], label='Метод половинного деления для трансцендентной функции')
plt.plot(chart2()[0], chart2()[3], label='Полюсный метод секущих для алгебраической функциии')
plt.plot(chart2()[0], chart2()[4], label='Полюсный метод секущих для трансцендентной функции')
plt.legend()
plt.figure(4)
plt.yscale('log')
plt.grid()
plt.xlabel('номер итерации')
plt.ylabel('абсолютная ошибка')
plt.title("График зависимости абсолютной ошибки от номера итерации")
plt.plot(chart_help(list_1), chart(-1 / 2 + np.sqrt(5) / 2, list_1), label='Метод половинного деления для алгебраичес'
                                                                           'кой функциии')
plt.plot(chart_help(list_2), chart(3.2299594397279283, list_2), label='Метод половинного деления для трансцендент'
                                                                      'ной функции')
plt.plot(chart_help(list_3), chart(-1 / 2 + np.sqrt(5) / 2, list_3), label='Полюсный метод секущих для алгебраичес'
                                                                           'кой функциии')
plt.plot(chart_help(list_4), chart(3.2299594397279283, list_4),
         label='Полюсный метод секущих для трансцендентной функции')
plt.legend()
plt.figure(5)
plt.grid()
plt.xscale('log')
plt.yscale('log')
plt.xlabel('задаваемая точность')
plt.ylabel('реальная точность')
plt.title("График зависимости реальной точности от задаваемой точности")
plt.plot(chart4()[0], chart4()[1], label='Метод половинного деления для алгебраической функциии')
plt.plot(chart4()[0], chart4()[2], label='Метод половинного деления для трансцендентной функции')
plt.plot(chart4()[0], chart4()[3], label='Полюсный метод секущих для алгебраической функциии')
plt.plot(chart4()[0], chart4()[4], label='Полюсный метод секущих для трансцендентной функции')
plt.plot(chart4()[0], chart4()[0], label='Идеальная погрешность')
plt.legend()
plt.show()
