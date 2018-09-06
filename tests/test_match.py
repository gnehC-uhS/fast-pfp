"""
.. module:: test_fastpfp
   :synopsis: Unit tests for fastpfp module
"""

import numpy as np

from fastpfp.util import graph2matrices
from fastpfp.match import num_nodes, match_graphs


def test_num_nodes():
    L1, A1 = graph2matrices(4, [(0, 1), (0, 2), (2, 3)])
    L2, A2 = graph2matrices(4, [(0, 1), (0, 2)])
    n1, n2 = num_nodes(A1, A2)
    assert n1 == 4
    assert n2 == 3


def test_match_identity():
    L, A = graph2matrices(3, [(0, 1), (0, 2)])

    P = match_graphs(A, A, L, L, device_id=-1)

    P_expected = np.array([[1, 0, 0],
                           [0, 1, 0],
                           [0, 0, 1]])
    assert np.allclose(P, P_expected)


def test_shuffled():
    L1, A1 = graph2matrices([[0], [1], [2]], [(0, 1), (0, 2)])
    L2, A2 = graph2matrices([[1], [0], [2]], [(1, 0), (1, 2)])

    P = match_graphs(A1, A2, L1, L2, device_id=-1)

    P_expected = np.array([[0, 1, 0],
                           [1, 0, 0],
                           [0, 0, 1]])
    assert np.allclose(P, P_expected)


def test_match():
    L1, A1 = graph2matrices(4, [(0, 1), (0, 2), (2, 3)])
    L2, A2 = graph2matrices(4, [(0, 1), (0, 2)])

    P = match_graphs(A1, A2, L1, L2, device_id=-1)

    P_expected = np.array([[1, 0, 0],
                           [0, 1, 0],
                           [0, 0, 1],
                           [0, 0, 0]])
    assert np.allclose(P, P_expected)
