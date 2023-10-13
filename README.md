# Python Exercises
[![codecov](https://codecov.io/gh/alefeans/python-exercises/branch/master/graph/badge.svg)](https://codecov.io/gh/alefeans/python-exercises) [![MIT License](https://img.shields.io/badge/license-MIT-007EC7.svg?style=flat)](/LICENSE) [![Python](https://img.shields.io/badge/python-3.6-blue.svg)]()

Here, you'll find solved code challenges from platforms like [Hackerhank](https://www.hackerrank.com/), [Practice Python](https://www.practicepython.org/), [Project Euler](https://projecteuler.net/), some programming book exercises (e.g. [Elements of Programming Interviews](http://elementsofprogramminginterviews.com/)), common algorithms and data structures [implementation](dsa/), and [others](others/).

## Running the Code

Until this commit, the code were all made using only the standard library, so the requirements are here just for the *tests*:

```
git clone https://github.com/alefeans/python-exercises.git .
python {platform}/{challenge}/{challenge}.py
```

## Tests

Activate your Python virtual environment and run:

```
poetry install

# or

pip install .
```

Then:

```
pytest
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
