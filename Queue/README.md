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
| 08 | First Non-Repeating Character | ⏳ |
| 09 | Rotting Oranges | ⏳ |
| 10 | Round Robin Scheduling | ⏳ |
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
