class Process:
    def __init__(self, pid, burst_time):
        self.pid = pid
        self.burst_time = burst_time
        self.waiting_time = 0
        self.turnaround_time = 0

def find_waiting_time(processes):
    processes[0].waiting_time = 0

    for i in range(1, len(processes)):
        processes[i].waiting_time = processes[i - 1].waiting_time + processes[i - 1].burst_time

def find_turnaround_time(processes):
    for process in processes:
        process.turnaround_time = process.burst_time + process.waiting_time

def calculate_average_times(processes):
    total_waiting_time = 0
    total_turnaround_time = 0

    find_waiting_time(processes)
    find_turnaround_time(processes)

    for process in processes:
        total_waiting_time += process.waiting_time
        total_turnaround_time += process.turnaround_time

    average_waiting_time = total_waiting_time / len(processes)
    average_turnaround_time = total_turnaround_time / len(processes)

    return average_waiting_time, average_turnaround_time

def main():
    processes = [
        Process(1, 10),
        Process(2, 5),
        Process(3, 8)
    ]

    avg_waiting_time, avg_turnaround_time = calculate_average_times(processes)

    print(f"Average Waiting Time: {avg_waiting_time:.2f}")
    print(f"Average Turnaround Time: {avg_turnaround_time:.2f}")

if __name__ == "__main__":
    main()
