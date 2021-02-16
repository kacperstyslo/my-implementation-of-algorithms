import os
import re


class MonkeyEscape:

    def __str__(self):
        algorithm_rules = """The cheerful monkey has found a new fun.She put n cages with animals (there is exactly one animal in one cage) in a circle and jumps on them.The monkey always jumps two frames and always opens the one it is standing on.The monkey will stop when it jumps onto the previously opened cage.Your task is to find out how many pets will escape.It is known that all cages are initially closed and each animal (except for a happy monkey) takes the opportunity and runs away if it can.Input The first line of input contains one integer z, denoting the number of data sets.The following lines describe subsequent sets.Each row of the set contains two integers n and d, denoting the number of frames and the monkey's jump length, respectively (d = 1 means that the monkey will jump to the next frame in the sequence)."""
        return re.sub(r'(?<=[.])(?=[^\s])', f'\n', algorithm_rules)

    @staticmethod
    def monkey_from_the_zoo_get_data(tests=False, z=None, k_l=None, d_l=None):
        if k_l is None or d_l is None:
            k_l, d_l = [], []
        if not tests:
            z = int(input('Z: '))
            for _ in range(z):
                k = int(input("Number of cages(k): "))
                k_l.append(k)
                d = int(input("The jump value(d): "))
                d_l.append(d)
            for _ in range(z):
                print(MonkeyEscape.monkey_from_the_zoo(k_l[0], d_l[0]))
        for _ in range(z):
            return MonkeyEscape.monkey_from_the_zoo(k_l[0], d_l[0])
        del k_l[0], d_l[0]

    @staticmethod
    def monkey_from_the_zoo(k, d):
        if d > k:
            k, d = d, k
        if d == 0:
            return MonkeyEscape.monkey_from_the_zoo(d, k - d)
        return k


if __name__ == '__main__':
    debug = False  # Change value of debug from False to True to print algorithm rules
    if debug:
        print(MonkeyEscape().__str__())
        os.system('pause')
        os.system('cls')
    MonkeyEscape().monkey_from_the_zoo_get_data()
