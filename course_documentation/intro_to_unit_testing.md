# Intro to Unit Testing with Python

The following notes are mostly based on this post by Martin Fowler: https://martinfowler.com/bliki/UnitTest.html, and some from this guide: https://medium.com/@adocquin/mastering-unit-tests-in-python-with-pytest-a-comprehensive-guide-896c8c894304

## Why write tests?

- Important for robust and maintainable code
- You can go faster, make changes and refactor with more confidence, because you know your tests will stop you if you try to break something
- More bugs are caught bfore reaching the main code base and production.
- The tests can serve as documentation for how the code is supposed to work and how it is supposed to be used.

## What is a unit test?

Compared to other tests, unit tests are:

- Smaller in scope, low-level and focusing on a small part of the system.
- Written by the programmer as part of the development, not by a dedicated tester.
- Significantly faster

## What is a unit?

- In object-oriented programming, it is typically a class
- In functional or procedual programming, it is typically a function

## Sociable versus Solitary Tests

- Sociable tests rely on other units to fullfil their behaviour
- Solitary tests use test doubles (for example mocks) to substitute for example talking to a remote service during the test.

## Structure

- Arrange
- Act
- Assert
- Clean up?

## When to run the tests and how fast should they be?

- After a code change, run all relevant tests (compile suite) (a few seconds)
- Before mergin with main code base, run all tests (commit suite) (< 10 min)
- The test suit should run fast enough that you are not discouraged from running it frequently enough
- Frequently enough so that when a bug is detected, there is not too much changes to look through to find the bug.

## Hands on exercise

See [Exercise 6](exercises/6_more_on_unit_testing.md).
