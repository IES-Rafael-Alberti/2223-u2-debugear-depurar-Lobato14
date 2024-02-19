import pytest
from src.algoritmo_burbuja import ordenacion_burbuja

def test_ordenacion_burbuja():
    assert ordenacion_burbuja([8, 3, 1, 19, 14]) == [1, 3, 8, 14, 19]