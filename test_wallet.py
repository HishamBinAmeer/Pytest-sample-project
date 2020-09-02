import pytest
from wallet import Wallet, insufficientAmount

@pytest.fixture
def my_wallet():
	'''Returns a Wallet instance with a zero balance'''
	return Wallet()
	

@pytest.mark.parametrize("earned,spent,expected",[(130,110,20),(20,2,18),])

def test_transaction(my_wallet, earned,spent,expected):
	my_wallet.add_cash(earned)
	my_wallet.spend_cash(spent)
	assert my_wallet.balance==expected

# @pytest.fixture
# def empty_wallet():
# 	'''Returns a wallet instance with a zero balance'''
# 	return Wallet()


@pytest.fixture
def wallet():
	'''Returns a wallet instance with a balance of 20'''
	return Wallet(20)

def test_default_initial_amount(my_wallet):
	assert my_wallet.balance==0


def test_setting_initial_amount(wallet):
	assert wallet.balance==20


def test_wallet_add_cash(wallet):
	wallet.add_cash(80)
	assert wallet.balance==100


def test_wallet_spend_cash(wallet):
	wallet.spend_cash(10)
	assert wallet.balance==10


def test_wallet_spend_cash_raises_exception_on_insufficient_amount(my_wallet):
	with pytest.raises(insufficientAmount):
		my_wallet.spend_cash(100)