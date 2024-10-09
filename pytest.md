 ![Screenshot 2024-10-09 224335](https://github.com/user-attachments/assets/68844d3e-8586-4e2d-bd7b-68f54dcd6bb5)
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
 def test_get_use![Screenshot 2024-10-09 224546](https://github.com/user-attachments/assets/ebb4b308-e3d9-458e-80c5-fd2513a05552)
r_fr![Screenshot 2024-10-09 224533](https://github.com/user-attachments/assets/bd264748-18c1-4f0f-84c4-5cccd65e2a57)
om_db():
 pass
 ```![Screenshot 2024-10-09 224533](https://github.com/user-attachments/assets/b8264c60-7166-4e73-90a4-48a48d143c43)
![Screenshot 2024-10-09 224546](https://github.com/user-attachments/assets/77bc195b-f2a4-4a57-8ec6-9da9e0d83605)



 you can also test using apis
