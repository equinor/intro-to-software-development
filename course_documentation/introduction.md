# Introduction

## Round around the table

- Name
- Where and what you study
- Internship location (Trondheim, Bergen, Stavanger, Oslo?)
- Short about the project
- Optionally what you hope to learn in the course

## Content for the Git & Python parts

In this part of course, we will set up a simple Python package. It will concern some simple
calculations within the geology domain, so we will name it `geo-calculator`.

Along the way, you will get familiar with the packaging structure of Python and how a
modern Python package typically looks.

We will also embed git into our workflow, learn / refresh the basic git commands, and
possibly touch upon some more advanced commands.

Quite early we will write some unit tests, which verify intended functionality.

We will set up a workflow in GitHub Actions for doing continuous integration with your
remote repository, including running your tests and static code analysis.

Towards the end of this section we will use what we have learned to implement the
calculation of a specified geological property.

The main learning goal is to be familiar with the development process, and learn some
software craftsmanship along the way.

## Exercises

- The exercises are described in "course_documentation/exercises".
- Disclaimer for the exercises: There are probably errors and discrepancies in the exercise descriptions. We will walk through the exercises together. If there are inconsistencies or something is off / missing; do as I say, not as I wrote. And not the least, ask questions and help each other.

## Course outline

0. Working environment
1. Setup package structure
   - Create files
   - Commit work to local
   - Push to remote
2. Writing your first test
   - TDD; make failing test, then let it pass
   - implement find_average
   - Present some benefits of writing good tests (in advance). E.g. change code with confidence later
3. Continuous integration
   - Add workflow
   - Add formating
   - Add typehinting
   - Create Pull Request (make this mandatory on your fork)
4. Implement gardners equation
   - Receive a finished test for gardners equation
   - Bonus: Play around with Pytest approx. Find out from docs what the default tolerance is
   - Receive a finished test (skipped) for inverse gardners equation
   - Bonus: Add requirement to handle negative velocity (new test, skipped initially)
5. Optional Exercises
