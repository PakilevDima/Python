# sentence = 'the rocket came back from mars'
# vowels = [print(i) for i in sentence if i in 'aeiou']

# original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
# prices = [i if i > 0 else 0 for i in original_prices]
# print(prices)

# quote = "life, uh, finds a way"
# uinque_vowels = {i for i in quote if i in 'aeiou'}
# print(*uinque_vowels)

# print(squares := {i: i*i for i in range(10)})

# import random
# def get_weather_data():
#     return random.randrange(90, 110)
# hot_temps = [temp for i in range(20) if (temp := get_weather_data()) >= 100]
# print(hot_temps)
# print(x := 120)
# print(x)

# print(sum(i * i for i in range(100000)))

# print(sum(qoute := [nums := 1 for i in (input()) if i == ' ']) + 1) # если пробелы не в конце и не в начале
# print(len(list(word for word in input().split())))
# nums = input()
# if len(nums) == 6:
#     new_nums = nums[1::]
#     nums = nums[0] + new_nums[::-1]
#     print(nums)
# else:
#     nums = nums[::-1]
# for i in nums:
#     if nums[0] == '0':
#         nums = nums.replace('0', '', 1)
# print(nums)

# def countdown(num):
#     print("Начало")
#     while num > 0:
#         yield num
#         num -= 1
# print(val := countdown(5))
# print(next(val))
# print(next(val))
# print(next(val))
# print(next(val))
# print(next(val))
# print(next(val))

# my_lisy = ['a', 'b', 'c']
# print(gen_ogj := (x for x in my_lisy))
# for val in gen_ogj:
#     print(val)

# import sys
# g = (i * 2 for i in range(100000) if i % 3 == 0 or i % 5 == 0)
# print(sys.getsizeof(g) / 1024)

# import re
# result = re.findall(r'AV', "AV Analytics Vidhya AV")
# result = re.sub(r'India', 'the World', 'AV is largest Analytics community of India')
# print(*result)

# n = list(input())
# answer = []
# i2 = 0
#
# for i in n:
#     try:
#         i2 = n[n.index(i) + 1]
#     except IndexError:
#         print(answer)
#         break
#     if i != ' ' and i2 != ' ':
#         answer.append(f'{i}{i2}')

# import re
#
# print(result := re.findall(r'\d{2}-\d{2}-\d{4}', 'Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABS 67-8945 12-01-2009'))

# import re
# print(result := re.findall(r'\b[aeiouAEIOU]\w+', 'AV is largest Analytics community of India'))

# import re
# print(result := re.findall(r'\B[aeiouAEIOU]\w', 'AV is largest Analytics community of India'))

# string = 'abd abc Ds ds Ds gf hg'.split()
# answer = set(string)
# for i in answer:
#     print(f'{i}: {string.count(i)}')

# import time
# seconds = time.time()
# # # print("Секунды с начала эпохи = ", seconds // 360)
# # # local_time = time.ctime(952154212)
# # # print(local_time)
# # # print("Сейчас.")
# # # time.sleep(10.4)
# # # print("Через 2.4 секунды")
# # result = time.localtime()
# # # print(result)
# # # print(time.gmtime())
# # t = (2019, 12, 7, 14, 30, 30, 5, 341, 0)
# # print(time.asctime(t))
# # # 1575700230.0
# # named_tuple = time.localtime()
# # time_string = time.strftime("%m/%d/%Y, %H:%M", named_tuple)
# # print(time_string)
# print(f"Письмо отправлено: {time.strftime('%d числа %m месяца в %H:%M', time.localtime())}")

# import re
# list_my = ['9999', '9999999', '9999x9999', '9920240456']
# for i in list_my:
#     result = re.findall(r'\d', i)
#     if result[0] == 8 or 9 and len(result) == 10:    # моё решение
#         print('YES')
#     else:
#         print('No')
# for val in list_my:
#     if re.match(r'[8-9]{1}[0-9]{9}', val) and len(val) == 10:
#         print('YES')
#     else:
#         print('No')
# import re
# line = 'asdf ikdkd;jfks,ikkd;l,dk'
# result = re.sub(r'\W\b', ' ', line)
# print(result)

# import datetime
# dt_now = datetime.datetime.now()
# print(dt_now)
# current_date = datetime.date.today()
# print(current_date)
# current_date_time = datetime.datetime.now()
# current_time = current_date_time.time()
# print(current_time)
#
# from datetime import date
# first_date = date(2020, 10, 2)
# second_date = date(2020, 10, 30)
# delta = second_date - first_date
# print(delta)

# l = [1, 2, 3, 4, 5, 6]
# def modify_list(l):
#     i = 0
#     n = len(l)
#     while i < n:
#         if l[i] % 2 != 0:
#             l.pop(i)
#             n -= 1
#         else:
#             l[i] = l[i] // 2
#             i += 1
# modify_list(l)
# print(l)

# import re
# n = input()
# list_new = re.findall(r'(\d)[^\+]', n)
# # for i in list_new:
# #     if i not in znaks:
# #         if list_new.index(i) != list_new[-1]:
# #             if list_new[list_new.index(i) + 1] != '+':
# #                 answer.append(i)
# list_new.append(n[-1])
# print(list_new)
# def hello_world():
#     print("Hello world!")
# def wrapper_function(func):
#     print("получена {} функция".format(func))
#     func()
#     return func
# hello = wrapper_function(hello_world)
# hello()
# print(type(hello))

def sum_count(a, b, c):
    if a + b == c or a + c == b or b + c == a:
        return 'yes'
    else:
        return 'no'
print(sum_count(4, 8, 4))