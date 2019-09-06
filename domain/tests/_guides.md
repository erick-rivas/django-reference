# Tests

Represents the domain methods test cases

## Table of content

-  [Guidelines](#guidelines)
-  [Example](#example)

## Guidelines

-  Start file name with test_
>  Example test_players.py

-  Run with:
```
$ python3 manage.py test domain/tests
```

## Example

```python
class Test(TestCase):  #

    def test(self):
        res = "hi!"
        self.assertEqual("hi!", res)
```
