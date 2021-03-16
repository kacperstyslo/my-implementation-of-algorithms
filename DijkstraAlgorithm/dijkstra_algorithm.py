import pandas as pd
from pandas.testing import assert_frame_equal


class DijkstraAlgorithm:
    def __init__(self):
        self.nodes: dict = {'A': [0], 'B': [0], 'C': [0], 'D': [0]}
        self.edges: dict = {'AB': 2, 'AC': 1, 'BD': 3, 'CD': 5}
        self.found_keys = [key for key in self.edges.keys()]
        self.show_table = lambda: pd.DataFrame(self.nodes)

    def manager(self, test: bool):
        while self.found_keys:
            self.algorithm_step(first_k=self.found_keys[0], second_k=self.found_keys[1])
        if test:
            expected_result = pd.DataFrame({'A': [0], 'B': [0], 'C': [1], 'D': [3]})
            assert_frame_equal(expected_result, self.show_table())
        print(self.show_table())

    def algorithm_step(self, first_k, second_k):
        if self.edges.get(first_k) < self.edges.get(second_k):
            self.nodes[first_k[-1]] = self.edges.get(first_k)
        else:
            self.nodes[second_k[-1]] = self.edges.get(second_k)
        del self.edges[first_k], self.edges[second_k], self.found_keys[0], self.found_keys[0]


if __name__ == '__main__':
    DijkstraAlgorithm().manager(test=True)
