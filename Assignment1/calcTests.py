from calculator import *


def test_run_calculator():
    assert runCalculator(['123', '+', '456']) == '579'
    assert runCalculator(['1', '+', '2', '+', '3', '+', '4', '+', '5']) == '15'
    assert runCalculator(['15', '-', '12']) == '3'
    assert runCalculator(['100', '-', '50', '-', '10', '-', '15']) == '25'
    assert runCalculator(['2', '*', '3']) == '6'
    assert runCalculator(['14', '*', '15', '*', '7']) == '1470'
    assert runCalculator(['6', '*', '3', '-', '7']) == '11'
    assert runCalculator(['12', '+', '14', '-', '5', '+', '8', '+', '2']) == '31'
    assert runCalculator(['100', '*', '3', '-', '200', '+', '100', '-', '50']) == '150'
    assert runCalculator(['200', '-', '12', '*', '6']) == '128'
    assert runCalculator(['-2', '*', '6']) == '-12'
    assert runCalculator(['12', '+', '-4']) == '8'
    assert runCalculator(['18', '-', '-6']) == '24'


def test_read_input_invalid_inputs():
    assert readInput("invalid input") == -1
    assert readInput("+-*") == -2
    assert readInput("20++10") == -3
    assert readInput("20 15") == -4


def test_infix_to_postfix():
    assert infixToPostfix(['5', '+', '6', '-', '7']) == ['5', '6', '+', '7', '-']
    assert infixToPostfix(['3', '+', '2', '*', '4']) == ['3', '2', '4', '*', '+']


def test_calculate():
    assert calculate('5', '+', '5') == '10'
    assert calculate('5', '-', '3') == '2'
    assert calculate('5', '*', '5') == '25'
