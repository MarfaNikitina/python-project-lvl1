#!/usr/bin/env python3
import prompt
from brain_games.games.calc import create_random_expr


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    if name:
        print('Hello, {}!'.format(name))
    print('What is the result of the expression?')
    i = 0
    while i <= 2:
        ran_expression = create_random_expr()
        print('Question: {}'.format(ran_expression))
        true_answer = str(eval(ran_expression))
        answer = prompt.string('Your answer: ')
        if answer == true_answer:
            print('Correct!')
        else:
            print(
                "'{}' is wrong answer ;(. "
                "Correct answer was '{}'.".format(answer, true_answer)
            )
            print("Let's try again, {}!".format(name))
            break
        i += 1
    print('Congratulations, {}!'.format(name))


if __name__ == '__main__':
    main()
