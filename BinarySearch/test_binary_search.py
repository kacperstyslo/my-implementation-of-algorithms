import pytest
from BinarySearch.binary_search import *


def test_output_from_p0_q0():
    assert BinaryAlgorithm().binary_search_algorithm(tests=True, p_q_l=[0, 0]) == 'NIE'


def test_output_from_p2_q12():
    assert BinaryAlgorithm().binary_search_algorithm(tests=True, p_q_l=[2, 12]) == 2


def test_output_from_p3_q14():
    assert BinaryAlgorithm().binary_search_algorithm(tests=True, p_q_l=[3, 14]) == 2


def test_output_from_p7_q14():
    assert BinaryAlgorithm().binary_search_algorithm(tests=True, p_q_l=[7, 14]) == 'NIE'


def test_output_from_p1020_q14():
    assert BinaryAlgorithm().binary_search_algorithm(tests=True, p_q_l=[1013, 14]) is None


def test_output_from_p10_q1019():
    assert BinaryAlgorithm().binary_search_algorithm(tests=True, p_q_l=[10, 1019]) is None