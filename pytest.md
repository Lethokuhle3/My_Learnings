**What is pytest?**


- Testing framework for python,
auto-discovery of tests

>why pytest?

>>simplied syntax

>>rich assertion introspection

>>powerful fixtures system

>>compatibility

>>extensibility

1. Install pytest
```py
 pip install pytest

```
2. Create a test file
test_example.py

3. Write a Function to Test
```py
# example.py
def add(a, b):
    return a + b
```

4. Write a Test Function
```py
# test_example.py
from example import add

def test_add():
 result = example.add(15,3)
  assert result == 18

      OR
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
```

Run the test ..pytest


Fixtures: to avoid repeating yourself
@pytest.fixture

'  **Mark and parametrize:**
@pytest.mark.slow
If you want it to be slow

how to run it ---pytest.mark.slow

```py
@pytest.mark.skip(reason="This feature is currently broken")
def test_add():
 assert my_functions.add(1,2)== 3
```

```py
@pytest.mark.xfail(reason="we know we cannot devide by 0")
def test_divide_zero_broken():
 my_function.divide(4,0)
 ```

```py
 @pytest.mark..parametrize("side_length, expected_area", [(5,25)])
 def test_multiple_square_areas(side_length, expected_area):
 assert shapes.Shapes(side_length).area()== expected_area

 ```


 mocks: how mocking works with pytest
```py

 import unittest.mock as mock

 @mock.patch("source.service, get_user_from_db")
 def test_get_user_from_db():
 pass
 ```


 you can also test using apis