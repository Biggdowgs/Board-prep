import os

from time import sleep


def clearConsole():
    command = 'clear'

    if os.name in ('nt', 'dos'):
        command = 'cls'

    os.system(command)

    sleep(0.5)


clearConsole()
