import pytest
from shop.store import add_product, connect, find, sell


def test_sell_reduces_stock():
    db = connect()
    add_product(db, "apple", 0.5, 10)
    assert sell(db, "apple", 4) == 2.0
    assert find(db, "apple")[2] == 6


def test_cannot_oversell():
    db = connect()
    add_product(db, "pear", 0.8, 1)
    with pytest.raises(ValueError):
        sell(db, "pear", 2)
