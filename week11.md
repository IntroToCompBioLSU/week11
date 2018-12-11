# Week 11 Outline

## The logic of object-oriented programming

- The point of OOP is to be able to bundle data and functions into logical units.
- When this is done well, it makes our code much easier to read and use.
- Baseball stats example
  - Since the World Series was just on, we can use a baseball example as motivation.
  - A huge number of statistics and outcomes are recorded each game.
  - Imagine that we want to write a program that will allow us to easily access relevant information quickly.
  - This is the kind of code that sports stats companies use to come up with those fascinating bits of information on the fly during the game.
    - "The last time a player hit two doubles followed by a triple after breaking his bat was on Monday, Aug. 12, 1983."
  - Let's think about some of the statisitics that are kept: who played, what's the outcome of each at bat, how many errors and who committed them, what happened each pitch (ball, strike, foul, etc.), ...
  - Now, imagine keeping track of all this as "loose" data. We might have a list of names, a list of what happened each at bat, a list of errors, etc.
  - If the data were stored this way and we wanted to know something like, "Who committed the last error and how did they do their last at bat?", it would be a nightmare. We'd have to first go to our list of players committing errors, then figure out what order they batted in the lineup, what order was batting currently, and somehow work backwards through the list of at bats to figure out what they did.
  - WAIT! There's a better way. If we use OOP, we could have created a player object that would automatically store all the relevant information on a player. As soon as we had their name, we could pull up any relevant statistic. We could even come up with new functions to summarize the statistics for each player in any way we wanted.


## Course Registrar Example of OOP

- We'll walk through a simpler example of objects in Python to see how they can be used interactively


## Demography Simulation

- I've got a working version of our demography simulation, although it only incorporates dispersal of a fixed number of individuals, with no reproduction.
- I was lazy and haven't yet commented the dispersal function that's associated with individuals.
- I want you to look over the dispersal function and add comments to indicate the logic that's being used.
- I then want you to look through the code at the bottom that actually runs the simulation and add comments.


## Weekly Assignment (Due Tuesday, Nov. 6th)

- Send me a commented version of the demography simulation
- I want you to begin thinking about the logic of your final project. What kinds of classes will you need? What properties and methods will they have? How will they interact?
  - A key skill with OOP is abstraction. How do you take the real world situation that you want to explore and turn it into Python?
  - Send me a few paragraphs that describe how you're thinking about structuring your code. 
