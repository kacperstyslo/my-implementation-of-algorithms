class BinaryAlgorithm:

    def __init__(self):
        self.result: list = []

    def binary_search_algorithm(self, tests=False, p_q_l=None):
        if p_q_l is None:
            p_q_l = []
        if not tests:
            z = int(input('Z(Number of tests): '))
            if z < 10000:
                for _ in range(z):
                    p_q = str(input('P/Q: ')).split()
                    p_q = list(map(int, p_q))
                    p_q_l.append(p_q[0])
                    p_q_l.append(p_q[1])

        while p_q_l:
            if p_q_l[0] > 1012 or p_q_l[1] > 1018:
                break
            left, right = {n: n ** 3 + n * p_q_l[0] for n in range(1, 11)}, p_q_l[1]
            self.result.append(
                (list(left.keys())[list(left.values()).index(right)]) if right in left.values() else 'NIE')
            del p_q_l[0:2]

        for r in self.result:
            if tests:
                return r
            print(r)


if __name__ == '__main__':
    c = BinaryAlgorithm()
    c.binary_search_algorithm()
