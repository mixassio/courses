# -*- coding: utf-8 -*-

# The real question is: how can we improove this code?!

right_answers = 0

right_label = 'Правильный ответ!'
wrong_label = 'Неправильный ответ!'

# Question 1

question_1 = 'Сколько типов чисел есть в Python3?'
answer_1 = '3'
user_answer_1 = input(question_1)

if answer_1 == user_answer_1:
    right_answers += 1
    print(right_label)
else:
    print(wrong_label)

# Question 2

question_2 = 'Какая последняя актуальная версия?'
answer_2 = '3.6.0'
user_answer_2 = input(question_2)

if answer_2 == user_answer_2:
    right_answers += 1
    print(right_label)
else:
    print(wrong_label)

# Question 3

question_3 = 'Как превратить что-то в строку?'
answer_3 = 'str()'
user_answer_3 = input(question_3)

if answer_3 == user_answer_3:
    right_answers += 1
    print(right_label)
else:
    print(wrong_label)

# Result

print('Вы правильно ответили на {} из 3 вопросов.')
