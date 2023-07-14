import os
import numpy as np


def return_hello():
    return 'hello'


def return_env_variable():
    return os.environ.get('SERVICE_NAME')


def np_add(a, b):
    """This function adds two numpy arrays element-wise"""
    return np.add(a, b)


def print_file_content():
    with open('shared/shared_file.txt', 'r') as file:
        content = file.read()
        return content


def run():
    print(f'return_hello: {return_hello()}')
    print(f'return_env_variable: {return_env_variable()}')
    print(f'shared_file_in_hello: {print_file_content()}')

    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])

    print('a = [1, 2, 3]')
    print('b = [4, 5, 6]')

    print(f'np_add(a, b): {np_add(a, b)}')  # Prints: [5 7 9]

    print('Exit')


if __name__ == '__main__':
    run()

