import pytest
from shop.pricing import apply_discount, subtotal


def test_subtotal():
    assert subtotal([(2.5, 2), (1.0, 3)]) == 8.0


def test_discount():
    assert apply_discount(200, 10) == 180.0


def test_discount_range():
    with pytest.raises(ValueError):
        apply_discount(100, 120)
