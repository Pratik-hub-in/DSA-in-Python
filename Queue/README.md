# Queue

The **Queue** folder contains Python implementations of fundamental Queue operations and important queue-based algorithms.

A Queue is a linear data structure that follows the **FIFO (First In, First Out)** principle.

---

## 📚 Topics Covered

- Queue using Python List
- Queue using Deque
- Queue using Linked List
- Circular Queue
- Queue using Two Stacks
- Priority Queue
- Deque
- First Non-Repeating Character
- Rotting Oranges
- Round Robin Scheduling

---
## 📋 Implementations

| No. | Implementation | Status |
|-----|----------------|--------|
| 01 | Queue Using List | ✅ |
| 02 | Queue Using Deque | ✅ |
| 03 | Queue Using Linked List | ✅ |
| 04 | Circular Queue | ✅ |
| 05 | Queue Using Two Stacks | ✅ |
| 06 | Priority Queue | ✅ |
| 07 | Deque | ✅ |
| 08 | First Non-Repeating Character | ✅ |
| 09 | Rotting Oranges | ✅ |
| 10 | Round Robin Scheduling | ✅ |
---
## ⚡ Implementation Comparison

| Implementation | Enqueue | Dequeue | Space | Main Concept |
|----------------|---------|---------|-------|--------------|
| Python List | O(1) | O(n) | O(n) | Basic implementation |
| Python Deque | O(1) | O(1) | O(n) | Efficient built-in Queue |
| Linked List | O(1) | O(1) | O(n) | Dynamic implementation |
| Circular Queue | O(1) | O(1) | O(n) | Fixed-size efficient Queue |
---

## 🔑 Core Queue Operations

| Operation | Description | Complexity |
|-----------|-------------|------------|
| Enqueue | Add element at rear | O(1) |
| Dequeue | Remove element from front | O(n)* |
| Front | View first element | O(1) |
| Rear | View last element | O(1) |
| Is Empty | Check queue status | O(1) |

\* `dequeue()` is O(n) in this list-based implementation because `pop(0)` shifts the remaining elements.

---

## 🎯 Learning Objectives

- Understand the FIFO principle.
- Implement queues using different data structures.
- Understand the difference between List and Deque.
- Learn circular and priority queues.
- Apply queues to real-world algorithmic problems.
- Understand BFS and scheduling applications.

---

## 🌍 Real-World Applications

Queues are commonly used in:

- CPU Scheduling
- Printer Queues
- Task Scheduling
- Breadth-First Search (BFS)
- Network Packet Processing
- Customer Service Systems
- Operating System Process Management




---

## ⭐ Priority Queue

A Priority Queue processes elements according to their priority.

This repository uses Python's `heapq` module to implement a
Min Priority Queue.

### Complexity

| Operation | Complexity |
|-----------|------------|
| Enqueue | O(log n) |
| Dequeue | O(log n) |
| Peek | O(1) |
| Is Empty | O(1) |

### Applications

- CPU Scheduling
- Dijkstra's Algorithm
- Prim's Algorithm
- Task Scheduling
- Network Packet Processing
- Event Simulation

---

## 🔄 Deque

A Deque (Double-Ended Queue) allows insertion and deletion
from both the front and rear.

### Applications

- Sliding Window Problems
- Palindrome Checking
- Browser History
- Task Scheduling
- Undo/Redo Systems
- BFS Variations

---

## 🔤 First Non-Repeating Character

This problem demonstrates how a Queue can be combined with
frequency counting.

### Data Structures Used

- Queue (`deque`) → Maintains character order
- Dictionary / Counter → Stores character frequencies

### Complexity

| Operation | Complexity |
|-----------|------------|
| Frequency Counting | O(n) |
| Queue Processing | O(n) |
| Total | O(n) |
| Extra Space | O(n) |

### Example

Input:

"swiss"

Output:

"w"
---

## 🍊 Rotting Oranges

The Rotting Oranges problem demonstrates **Multi-Source BFS**.

### Concepts Used

- Queue
- BFS
- Multi-Source BFS
- Matrix Traversal
- Level-Order Processing

### Complexity

| Complexity | Value |
|------------|-------|
| Time | O(rows × columns) |
| Space | O(rows × columns) |

### Applications

BFS-based techniques are useful in:

- Shortest Path Problems
- Network Propagation
- Infection Spread Simulation
- Grid Traversal
- Distance Calculation
- Flood Fill Problems
---
## 🖥️ Round Robin Scheduling

Round Robin is a preemptive CPU scheduling algorithm.

Each process receives a fixed amount of CPU time called
the **Time Quantum**.

If a process is not completed during its turn, it is placed
at the rear of the Queue.

### Concepts Used

- Queue
- FIFO
- CPU Scheduling
- Time Quantum
- Preemption
- Gantt Chart

### Important Formulas

Turnaround Time:

    TAT = Completion Time - Arrival Time

Waiting Time:

    WT = Turnaround Time - Burst Time

### Applications

- Operating Systems
- Time-Sharing Systems
- CPU Scheduling
- Process Management
- Multi-tasking Systems
