import pytest

def capital_case(x):
	if not isinstance(x, str):
		raise TypeError('please provide a string argument')
	return x.capitalize()

def test_capital_case():
	assert capital_case('hisham')=='Hisham'


def test_raises_exception_on_non_string_arguments():
	with pytest.raises(TypeError):
		capital_case(6)

