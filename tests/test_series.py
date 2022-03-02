from math_series.series import fibonacci, lucas, sum_series

def test_fibonacci_0():
    assert fibonacci(0) == 0

def test_fibonacci_2():
    assert fibonacci(2) == 1

def test_fibonacci_5():
    assert fibonacci(5) == 5

def test_fibonacci_7():
    assert fibonacci(7) == 13

def test_fibonacci_20():
    assert fibonacci(20) == 6765

def test_lucas_0():
    assert lucas(0) == 2

def test_lucas_2():
    assert lucas(2) == 3

def test_lucas_5():
    assert lucas(5) == 11

def test_lucas_7():
    assert lucas(7) == 29

def test_lucas_20():
    assert lucas(20) == 15127

def test_sum_series_20_fibo():
    assert sum_series(20) == 6765

def test_sum_series_20_lucas():
    assert sum_series(20, one=2, two=1) == 15127

def test_sum_series_20_otherSeries():
    assert sum_series(20, one=5, two=3) == 41200