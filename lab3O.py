import heapq

# Function to find the makespan (total time for all jobs)
def get_makespan(machines):
    return max(machines)

# Function to schedule jobs using branch and bound
def job_scheduling(jobs, num_machines):
    jobs.sort(reverse=True)  # Sort jobs by descending order of processing time
    machines = [0] * num_machines  # Initialize machine times
    heapq.heapify(machines)  # Convert to a min-heap to get the machine with the least load
    
    for job in jobs:
        # Assign the job to the machine with the least load
        min_machine = heapq.heappop(machines)
        min_machine += job
        heapq.heappush(machines, min_machine)
    
    return get_makespan(machines)

# Example usage
jobs = [4, 3, 2, 7, 5]  # Processing times for jobs
num_machines = 3  # Number of machines
makespan = job_scheduling(jobs, num_machines)
print("Minimum Makespan:", makespan)
