import random

from board import brd

from sp import slowprint

from sp import slowprint1

from sp import slowprint3

from time import sleep

from clr import clearConsole

import welcome


def d():
    slowprint3(welcome.w)

    slowprint1("\nWelcome to STEIMER's Millionaire Questionaire.\n\n")

    slowprint1("There are " + str(int(len(brd.keys()))) + " Board Questions")

    slowprint1("\nSorry for any misspellings!")

    print("")

    num = 0

    answer = int(input("How many Questions do you want to answer? "))

    print("")

    while num < answer:
        print("")
        rn6 = random.randrange(0, len(brd.keys()))
        rn = rn6
        ch = brd

        sleep(1)

        el = ([key for key in ch.keys()][rn])

        slowprint1(str(el))

        print("")

        sleep(8.0)

        slowprint("You have 10 seconds left to guess the answer:\n")

        sleep(10.0)
        el1 = ([value for value in ch.values()][rn])

        slowprint(str(el1))

        print("")

        num += 1

        sleep(2)

        if num < answer:
            slowprint1("\nPress enter to proceed to the next question: \n")

            input("")
        else:
            slowprint1("\nThat was the last question, I hope you did well!")
            sleep(3)

        clearConsole()

    slowprint("Thanks for playing!")

    slowprint3(welcome.b)
    slowprint("\nWould you like to play another round? ( y / n )\n")
    a = input("")
    if a == "y":
        d()
    else:
        exit()