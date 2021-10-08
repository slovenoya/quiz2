from pytest import *
from stock import *
import pytest

user = Portforlio()
user1 = Portforlio()

#1 test if the user starts with 0 shares
def test_init_stock():
    assert user.number_of_shares == 0

#2 test if the user is empty when no share
def test_is_empty():
    assert user.is_empty() == True

#3 test share_num correctly returns the number of different shares
#   each company counts for one type of share
def test_unique_share():
    assert user.unique_share() == 0

#4 test with purchase
def test_purchase():
    user.purchase_share("apple", 100)
    assert user.is_empty() == False
    assert user.number_of_shares == 100
    assert user.unique_share() == 1

# extension of test3
def test_unique_share2(): 
    user.purchase_share("apple", 100)
    assert user.is_empty() == False
    assert user.number_of_shares == 200
    assert user.unique_share() == 1

# extension of test3
def test_unique_share3(): 
    user.purchase_share("amazon", 100)
    assert user.is_empty() == False
    assert user.number_of_shares == 300
    assert user.unique_share() == 2

#5 simple test on sell share
def test_sell_share():
    user.sell_share("apple", 50)
    assert user.is_empty() == False
    assert user.number_of_shares == 250
    assert user.unique_share() == 2

#6 simple test on count certain share
def test_share_num_by_name():
    user1.purchase_share("apple", 40)
    user1.purchase_share("apple", 110)
    user1.purchase_share("amazon", 100)
    user1.sell_share("apple", 10)
    user1.purchase_share("apple", 10)
    assert user1.share_num_by_name("apple") == 150
    assert user1.share_num_by_name("amazon") == 100
    assert user1.number_of_shares == 250

#7 simple test on sell share to zero and removal of company
def test_sell_share():
    user1.sell_share("apple", 150)
    assert user1.number_of_shares == 100
    assert user1.unique_share() == 1

#8 test exception for selling too many shares
def test_share_exception():
    with pytest.raises(ShareSaleException): 
        user1.sell_share("amazon", 1000)

#test on class Share about its behavior
def test_share_sell():
    share = Share("google", 100)
    assert share.hold_count == 100
    share.sell(100)
    assert share.hold_count == 0
