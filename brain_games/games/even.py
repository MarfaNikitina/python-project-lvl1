#!/usr/bin/env python3
from random import randint
RULE = 'Answer "yes" if the number is even, ' \
       'otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def generate_question_and_answer():
    question = randint(1, 100)
    if is_even(question):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
