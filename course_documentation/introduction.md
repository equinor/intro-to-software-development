# Introduction

## Round around the table

- Name
- Where and what you study
- Internship location (Trondheim, Bergen, Stavanger, Oslo)
- Short about the project
- Optionally what you hope to learn in the course

## Content for the Git & Python parts

- The packaging structure of Python and how a modern Python
  package typically looks.
- Unit tests and the concept of Test Driven Development
- How to embed git into our workflow with basic commands (and possibly some more advanced
  if we have time)
- How to set up a workflow in GitHub Actions for doing Continuous Integration with your
  remote repository, including running your tests and static code analysis.
- Use what we have learned to implement the calculation of a specified geological property

The main learning goal is to be familiar with the development process, and learn some
software craftsmanship along the way.

We assume generall knowledge of Python and will not go through the syntax explicitly,
but please ask immediately if something is unclear or you want it covered a bit more.

For the morning session tomorrow, Tuesday, we want to open up for requests from you for what you want us to cover. You can make suggestions by creating an issue here: https://github.com/equinor/intro-to-software-development/issues.

## Exercises

- The exercises are described in `course_documentation/exercises`.
- You will get the chance to solve the exercises on your own first, before walk
  through them together.
- Please ask questions as we go and help each other out on the different locations.

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
5. Optional Exercises or a topic on request from you
