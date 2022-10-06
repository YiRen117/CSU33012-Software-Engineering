from unittest.mock import patch
import io

from calculator import *


def test_run_calculator():
    assert runCalculator("123+456") == 579
    assert runCalculator("1+2+3+4+5") == 15
    assert runCalculator("15-12") == 3
    assert runCalculator("100-50-10-15") == 25
    assert runCalculator("2x3") == 6
    assert runCalculator("14x15x7") == 1470
    assert runCalculator("6x3-7") == 11
    assert runCalculator("12+14-5+8+2") == 31
    assert runCalculator("100x3-200+100-50") == 150
    assert runCalculator("200-12x6") == 128


@patch('sys.stdout', new_callable=io.StringIO)
def test_read_input_invalid_inputs(mock_stdout):
    readInput("200++15")
    assert mock_stdout.getvalue() == "Error: Duplicated operators.\n"
    readInput("invalid input")
    assert mock_stdout.getvalue() == "Error: unexpected character.\n"
    readInput("200 100+10")
    assert mock_stdout.getvalue() == "Error: Duplicated operands.\n"
