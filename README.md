# Testing code using pytest

Demo of `pytest` framework


## Commands

Activate virtual environment:

```python
source .venv/bin/activate
```

Include print statements in the test output:
```python
pytest -s
```

Test only specific marks

```python
pytest 
```

## Classes

- use `setup_method` for constructors and other steps to do prior to testing
- use `tardown_method` for cleaning up after the test (deleting objects)
- define test functions inside the class or somewhere else

```python
# Define test class for testing Rectangle class
class TestRectangle:
    # Method used to initialize class objects and prepare the testing
    def setup_method(self, method):
        self.rectangle = shapes.Rectangle(3, 4)  # example object

    # Method used to clean up after tests
    def teardown_method(self, method):
        del self.rectangle  # delete object after use

    def test_area(self):
        assert self.rectangle.area() == self.rectangle.width * self.rectangle.height
```

## Fixtures

Fixtures provide a fixed baseline so that tests execute reliably and produce consistent, repeatable, results. Initialization may setup services, state, or other operating environments. These are accessed by test functions through arguments; for each fixture used by a test function there is typically a parameter (named after the fixture) in the test function’s definition.

>source: https://docs.pytest.org/en/6.2.x/fixture.html

## Definition

```python
@pytest.fixture(
)
def circle_collection() -> list[shapes.Circle]:
    # ...
    return [unit_circle, small_circle, big_circle]
```

## Usage

Use fixture name as test function parameter. This executes the fixtures in the given order prior to the actual test function. 

```python
# Test function using the fixture
def test_circles(circle_collection) -> None:  #  .. AND MORE FIXTURES AS PARAMS IF NEEDED
```

### Accessing fixtures

#### `conftest.py`

Defines fixtures accessible globally within the module

#### Using `scope` parameter

```python
@pytest.fixture(
    scope="module"
)
```

and also adding `import` statement to the respective file like this:
```python
from test.test_fixtures import circle_collection  # Import the fixture
```

### Cleaning up

When teardown is wanted for fixtures, use `yield` instead of `return`:

```python
def circle_collection() -> list[shapes.Circle]:
    # code here
    yield [
        unit_circle,
        small_circle,
        big_circle,
    ]  # alternative to return, but enables cleaning up afterwards
    del unit_circle, small_circle, big_circle  # clean-up steps (teardown code)
```

“Yield” fixtures yield instead of return. With these fixtures, we can run some code and 
pass an object back to the requesting fixture/test, just like with the other fixtures. 
The only differences are:
    - return is swapped out for yield.
    - Any teardown code for that fixture is placed after the yield.

Once pytest figures out a linear order for the fixtures, it will run each one up until it
returns or yields, and then move on to the next fixture in the list to do the same thing.
Once the test is finished, pytest will go back down the list of fixtures, but in the reverse order, 
taking each one that yielded, and running the code inside it that was after the yield statement.

>source: https://docs.pytest.org/en/6.2.x/fixture.html

## Marks

### Skip

```python
@pytest.mark.skip(reason="Showcase of skip mark, delete if needed")
class TestCase1:
    # Test function using the fixture imported from test_fixures.py
    def test_circles(self, circle_collection) -> None:
        for circle in circle_collection:
```

This leads to the test being skipped:

![](doc/skip.png)

## Links

- [Freecodecamp.org pytest tutorial](https://www.youtube.com/watch?v=cHYq1MRoyI0)
- [pytest documentation](https://docs.pytest.org/en/6.2.x/contents.html)

