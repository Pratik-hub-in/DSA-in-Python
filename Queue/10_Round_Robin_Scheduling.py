"""
Program: Round Robin CPU Scheduling

Description:
Round Robin is a CPU scheduling algorithm in which each
process gets a fixed amount of CPU time called Time Quantum.

Processes are executed in circular order.

If a process does not finish within its time quantum,
it is placed at the rear of the Queue and gets another
turn later.

Example:

Processes:
P1 = 5 ms
P2 = 4 ms
P3 = 2 ms

Time Quantum = 2 ms

Execution:

P1 → P2 → P3 → P1 → P2 → P1

This implementation uses a Queue to maintain the order
of processes.

Important Terms:
- Burst Time: Total CPU time required by a process.
- Time Quantum: Maximum CPU time given in one turn.
- Completion Time: Time when a process finishes.
- Turnaround Time: Completion Time - Arrival Time.
- Waiting Time: Turnaround Time - Burst Time.

Assumption:
All processes arrive at time 0.

Time Complexity:
- O(number of CPU time slices)
- Each process may enter the Queue multiple times.

Space Complexity:
- O(n)

Learning Outcomes:
- Understand Round Robin CPU Scheduling.
- Learn how Queue is used in Operating Systems.
- Understand Time Quantum.
- Calculate Waiting Time and Turnaround Time.
- Simulate CPU scheduling using a Queue.
"""

from collections import deque
from dataclasses import dataclass


@dataclass
class Process:
    """
    Represents a process in the CPU scheduling system.
    """

    process_id: str
    burst_time: int
    remaining_time: int = 0
    completion_time: int = 0
    waiting_time: int = 0
    turnaround_time: int = 0

    def __post_init__(self):
        self.remaining_time = self.burst_time


def round_robin_scheduling(
    processes: list[Process],
    time_quantum: int
) -> list[tuple[str, int, int]]:
    """
    Simulates Round Robin CPU Scheduling.

    Args:
        processes (list[Process]): List of processes.
        time_quantum (int): Maximum CPU time per turn.

    Returns:
        list[tuple[str, int, int]]:
            Execution timeline containing:
            (process_id, start_time, end_time)
    """

    if time_quantum <= 0:
        raise ValueError("Time Quantum must be greater than zero.")

    if not processes:
        return []

    queue = deque(processes)

    current_time = 0

    execution_timeline = []

    while queue:

        process = queue.popleft()

        start_time = current_time

        execution_time = min(
            process.remaining_time,
            time_quantum
        )

        current_time += execution_time

        process.remaining_time -= execution_time

        execution_timeline.append(
            (
                process.process_id,
                start_time,
                current_time
            )
        )

        if process.remaining_time > 0:

            # Process is not finished.
            # Put it back at the rear of the Queue.
            queue.append(process)

        else:

            # Process has completed.
            process.completion_time = current_time

    # Calculate Turnaround and Waiting Time.
    for process in processes:

        process.turnaround_time = (
            process.completion_time
        )

        process.waiting_time = (
            process.turnaround_time
            - process.burst_time
        )

    return execution_timeline


def display_results(processes: list[Process]) -> None:
    """
    Displays scheduling results.
    """

    print("\nScheduling Results")
    print("-" * 65)

    print(
        f"{'Process':<10}"
        f"{'Burst':<10}"
        f"{'Completion':<15}"
        f"{'Turnaround':<15}"
        f"{'Waiting':<10}"
    )

    print("-" * 65)

    total_waiting_time = 0
    total_turnaround_time = 0

    for process in processes:

        print(
            f"{process.process_id:<10}"
            f"{process.burst_time:<10}"
            f"{process.completion_time:<15}"
            f"{process.turnaround_time:<15}"
            f"{process.waiting_time:<10}"
        )

        total_waiting_time += process.waiting_time
        total_turnaround_time += process.turnaround_time

    number_of_processes = len(processes)

    average_waiting_time = (
        total_waiting_time / number_of_processes
    )

    average_turnaround_time = (
        total_turnaround_time / number_of_processes
    )

    print("-" * 65)

    print(
        f"Average Waiting Time: "
        f"{average_waiting_time:.2f}"
    )

    print(
        f"Average Turnaround Time: "
        f"{average_turnaround_time:.2f}"
    )


def display_gantt_chart(
    execution_timeline: list[tuple[str, int, int]]
) -> None:
    """
    Displays a simple Gantt Chart.
    """

    print("\nGantt Chart")
    print("-" * 65)

    for process_id, start_time, end_time in execution_timeline:

        print(
            f"| {process_id} ",
            end=" "
        )

    print("|")

    for _, start_time, _ in execution_timeline:

        print(
            f"{start_time:<6}",
            end=""
        )

    if execution_timeline:
        print(execution_timeline[-1][2])


if __name__ == "__main__":

    processes = [
        Process("P1", 5),
        Process("P2", 4),
        Process("P3", 2)
    ]

    time_quantum = 2

    print("Round Robin CPU Scheduling")
    print("=" * 65)

    print(f"Time Quantum: {time_quantum} ms")

    print("\nProcesses:")

    for process in processes:
        print(
            f"{process.process_id} "
            f"-> Burst Time: {process.burst_time} ms"
        )

    timeline = round_robin_scheduling(
        processes,
        time_quantum
    )

    display_gantt_chart(timeline)

    display_results(processes)


# Key Takeaways:
# • Round Robin is a preemptive CPU scheduling algorithm.
# • Every process receives a fixed Time Quantum.
# • An unfinished process goes back to the rear of the Queue.
# • Queue follows FIFO ordering.
# • Round Robin provides fair CPU time to processes.
# • It is commonly used in time-sharing systems.
