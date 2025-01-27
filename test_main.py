from main import *


def test_linear_search():
	""" done. """
	assert linear_search([1, 2, 3, 4, 5], 5) == 4
	assert linear_search([1, 2, 3, 4, 5], 1) == 0
	assert linear_search([1, 2, 3, 4, 5], 6) == -1
	""" worst case input value is last element in list or not in the list aka o(n)"""


def test_binary_search():
	assert binary_search([1, 2, 3, 4, 5], 5) == 4
	assert binary_search([1, 2, 3, 4, 5], 1) == 0
	assert binary_search([1, 2, 3, 4, 5], 6) == -1
	### TODO: add two more tests here.
	assert binary_search([1, 2, 5, 8, 9], 8) == 3
	assert binary_search([1, 4, 5, 7, 12], 11) == -1
	###
	""" worst case input value is when it is not in the list at o(logn)"""


def test_compare_search():
	res = compare_search(sizes=[10, 100])
	print(res)
	assert res[0][0] == 10
	assert res[1][0] == 100
	assert res[0][1] < 1
	assert res[1][1] < 1
