# Development Log – The Torchbearer

**Student Name:** Caroline Forsythe
**Student ID:** 827344993

---

## Entry 1 – [5/6/2026]: Initial Plan

_I plan to go in order of the sections laid out in the ASSIGNMENT.md file. It will help me keep on task
and complete the assignment in a way that compounds on itself to the final solution. I think starting the project and
doing the testing will be the harder parts of the assignment because it can be daunting. I also think the data
structure aspect of this project will be difficult for me because I do not have a great foundation due to my CS 210 
class being subpar and not fully preparing me for upper division classes. I plan to use resources online to help me
bridge this gap and will give myself more time to work on this project and test my solution(s)._

---
## Entry 2 – [5/7/2026]: [Part 2]
_Completed all of Part 2. Implemented and did testing for my solutions for select_sources(), run_dijkstra() and 
precompute_distances(). Answered related questions in the README._

---
## Entry 3 – [5/8/2026]: [Fix Part 2, Part 3]

_In Part 2, I had the end, T as a source point. This was incorrect because nothing moves on from that point, the 
torchbearer stays stationary and ends there. I edited my graph in README.md and my code in select_sources() to reflect 
this. All questions from Part 3 have been answered in README.md and implemented into torchbearer.py_

---
## Entry 4 – [5/8/2026]: [Part 4]
_Completed all of Part 4. All questions have been answered in README.md and implemented into torchbearer.py._

---
## Entry 5 – [5/11/2026]: [Part 5]

_Completed all of Part 5. All questions have been answered and the code has been implemented in torchbearer.py. 
Some grammatical changes were made to previous answers for other sections. Implemented solve() to be able to start
doing overall testing with all parts combined._
---


## Entry 6 – [Date]: [Part 6, Fix Part 5]

_Completed all of Part 6. All questions have been answered and the code has been implemented in torchbearer.py. I also 
fixed a key mistake I made in part 5 when passing values in the recursive call in _explore(). When I was passing through 
the total cost so far, I was only including cost_so_far, and not travel_cost, which is the current location to the next
relic. This was not giving a fully accurate total distance traveled which caused it to fail test 4. 


---

## Final Entry – [5/12/2026]: Time Estimate


| Part | Estimated Hours |
|---|-----------------|
| Part 1: Problem Analysis | 0.5             |
| Part 2: Precomputation Design | 1.5             |
| Part 3: Algorithm Correctness | 0.75            |
| Part 4: Search Design | 0.5             |
| Part 5: State and Search Space | 2.5             |
| Part 6: Pruning | 1               |
| Part 7: Implementation | 1               |
| README and DEVLOG writing | 1               |
| **Total** | 8.75            |
