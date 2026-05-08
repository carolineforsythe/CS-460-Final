# The Torchbearer

**Student Name:** Caroline Forsythe
**Student ID:** 827344993
**Course:** CS 460 – Algorithms | Spring 2026

> This README is your project documentation. Write it the way a developer would document
> their design decisions , bullet points, brief justifications, and concrete examples where
> required. You are not writing an essay. You are explaining what you built and why you built
> it that way. Delete all blockquotes like this one before submitting.

---

## Part 1: Problem Analysis

> Document why this problem is not just a shortest-path problem. Three bullet points, one
> per question. Each bullet should be 1-2 sentences max.

- **Why a single shortest-path run from S is not enough:**
  _A shortest-path run from S is not enough because it will not reach all of the relics and it is not 
 guaranteed to finish at T, both of which are required. Even though it finds the cheapest route, it likely does
not find the route that fits the requirements within the project._

- **What decision remains after all inter-location costs are known:**
  _The decision that remains is the order in which the relics should be visited before reaching the end, T._

- **Why this requires a search over orders (one sentence):**
  _This requires search over orders because there are k! sequences in which the relics can be visited in and there isn't 
a guaranteed greedy local choice that will find the optimal route._

---

## Part 2: Precomputation Design

### Part 2a: Source Selection

> List the source node types as a bullet list. For each, one-line reason.

| Source Node Type | Why it is a source                                                                                               |
|------------------|------------------------------------------------------------------------------------------------------------------|
| _spawn_          | _this is the original source point where the torchbearer starts every time_                                      |
| _relic_          | _this room is in the map and must be visited by the torchbearer, and is a source for the next location traveled_ |

### Part 2b: Distance Storage

> Fill in the table. No prose required.

| Property | Your answer                                                                            |
|---|----------------------------------------------------------------------------------------|
| Data structure name | nested directory                                                                       |
| What the keys represent | the outer kep represents the source node and the inner key represents the destination  |
| What the values represent | the values represent the distance (cost) from the source to the destination            |
| Lookup time complexity | O(1)                                                                                   |
| Why O(1) lookup is possible | it is possible becuase a set is used, sets use hashing and have a lookop cost of O(1). |

### Part 2c: Precomputation Complexity

> State the total complexity and show the arithmetic. Two to three lines max.

- **Number of Dijkstra runs:** _k + 1_
- **Cost per run:** _O(mlogn)_
- **Total complexity:** _O((k+1) * mlogn)_
- **Justification (one line):** _Dijkstra's algorithm runs are independent and the graph is explored fully only once. Multiplying the 
number of runs by the total cost per run equals the total complexity, which is O((k+1) * mlogn)._

---

## Part 3: Algorithm Correctness

> Document your understanding of why Dijkstra produces correct distances.
> Bullet points and short sentences throughout. No paragraphs.

### Part 3a: What the Invariant Means

> Two bullets: one for finalized nodes, one for non-finalized nodes.
> Do not copy the invariant text from the spec.

- **For nodes already finalized (in S):**
  _Because S only holds the guaranteed smallest distances, any dist[v] in S will be the most optimal path. No later 
discovered path can be better._

- **For nodes not yet finalized (not in S):**
  _dist[u] holds the shortest path found so far for nodes not yet finalized, and updates if path is found that is shorter than what is currently stored in dist[u].
It only considers routes that pass through nodes in the finalized set S.

### Part 3b: Why Each Phase Holds

> One to two bullets per phase. Maintenance must mention nonnegative edge weights.

- **Initialization : why the invariant holds before iteration 1:**
  _At initialization, the only known node is the source node and the distance cost is 0, because it is the current location of the torchbearer. All other nodes are 
set to inf() because paths to them have not been explored yet. Thus, the invariant holds at initialization._

- **Maintenance : why finalizing the min-dist node is always correct:**
  _The algorithm always picks the non-finalized node with the shortest distance in dist[u]. Due to the fact that there are no negative edge weights (edge weights only 
go from 0-infinity), any alternative path will be equal to or greater than the one stored in dist[u]. This means that the distance is optimal, and finalizing the node holds the invariant._

- **Termination : what the invariant guarantees when the algorithm ends:**
  _When the heap is empty, all reachable nodes have been added to S, and dist[v] holds the actual shortest path for every 
node. Unreachable remain set to inf() The invariant holds._

### Part 3c: Why This Matters for the Route Planner

> One sentence connecting correct distances to correct routing decisions.

_Connecting correct distances leads to correct routing decisions because it ensures that the path taken by the torchbearer is the shortest, lowest cost option that avoids wasting fuel, taking 
long paths, and possibly getting stuck in a dead end (because the paths are directed)._

---

## Part 4: Search Design

### Why Greedy Fails

> State the failure mode. Then give a concrete counter-example using specific node names
> or costs (you may use the illustration example from the spec). Three to five bullets.

- **The failure mode:** _Your answer here._
- **Counter-example setup:** _Your answer here._
- **What greedy picks:** _Your answer here._
- **What optimal picks:** _Your answer here._
- **Why greedy loses:** _Your answer here._

### What the Algorithm Must Explore

> One bullet. Must use the word "order."

- _Your answer here._

---

## Part 5: State and Search Space

### Part 5a: State Representation

> Document the three components of your search state as a table.
> Variable names here must match exactly what you use in torchbearer.py.

| Component | Variable name in code | Data type | Description |
|---|---|---|---|
| Current location | | | |
| Relics already collected | | | |
| Fuel cost so far | | | |

### Part 5b: Data Structure for Visited Relics

> Fill in the table.

| Property | Your answer |
|---|---|
| Data structure chosen | |
| Operation: check if relic already collected | Time complexity: |
| Operation: mark a relic as collected | Time complexity: |
| Operation: unmark a relic (backtrack) | Time complexity: |
| Why this structure fits | |

### Part 5c: Worst-Case Search Space

> Two bullets.

- **Worst-case number of orders considered:** _Your answer (in terms of k)._
- **Why:** _One-line justification._

---

## Part 6: Pruning

### Part 6a: Best-So-Far Tracking

> Three bullets.

- **What is tracked:** _Your answer here._
- **When it is used:** _Your answer here._
- **What it allows the algorithm to skip:** _Your answer here._

### Part 6b: Lower Bound Estimation

> Three bullets.

- **What information is available at the current state:** _Your answer here._
- **What the lower bound accounts for:** _Your answer here._
- **Why it never overestimates:** _Your answer here._

### Part 6c: Pruning Correctness

> One to two bullets. Explain why pruning is safe.

- _Your answer here._

---

## References

> Bullet list. If none beyond lecture notes, write that.

- _Lecture notes_
- _Stack Overflow: (information about sets and arrays) https://stackoverflow.com/questions/72120824/run-time-difference-for-in-searching-through-list-and-set-using-python._
- _Geeks for Geeks: (dijkstra's algorithm information) https://www.geeksforgeeks.org/dsa/dijkstras-shortest-path-algorithm-greedy-algo-7/_
- _source_