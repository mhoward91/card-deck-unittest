# Card-Deck-Unittest

Comprehensive unit test script, testing methods relating to a deck of cards implemented using a Card & Deck class.

## Description

The primary purpose of this project is to demonstrate ability to write, understand and execute unit tests. The unit tests are based on two classes and their associated methods, intended to represent a deck of cards. An individual card is represented as an instance of the Card class, while the Deck class has a list attribute, which holds each of the 52 card objects.

Each of the methods contained within these two classes are tested in the unit tests.

## Getting Started

### Dependencies

To clone and run this app on your machine, you'll need [Git](https://git-scm.com) and [Python 3](http://python.org/).

### Installation


1. Fork and clone this repository
```
$ git clone https://github.com/mhoward91/card-deck-unittest.git
```

2. Change directory to this repository
```
$ cd card-deck-unittest
```

_Note: no further packages are required beyond the python built-in modules_

### Exectuting unit tests

```
$ python test_card-deck.py

Ran 9 tests in 0.004s

OK
```
The unit tests can be run with verbose flag, to display more detailed information regarding the tests run.

```
$ python test_card_deck.py -v

test_init (__main__.CardTests)
each card has a suit & value ... ok
test_repr (__main__.CardTests)
each card returns its correct string representation ... ok
...
```

## License

This project is licensed under the MIT License - see the LICENSE.md file for details
