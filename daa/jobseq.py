
def job_sequencing_with_deadline(jobs):
    # Sort jobs based on their profits in descending order
    jobs.sort(key=lambda x: x[2], reverse=True)

    # Initialize variables to store the result
    result = []
    total_profit = 0

    # Iterate through each job and schedule it in the earliest available slot
    for job in jobs:
        deadline = job[1]

        while deadline > 0 and result.count(None) < deadline:
            result.append(job[0])
            total_profit += job[2]
            break

    return result, total_profit

# Example usage
jobs = [('J1', 2, 60), ('J2', 1, 100), ('J3', 3, 20), ('J4', 2, 40)]
schedule, profit = job_sequencing_with_deadline(jobs)

print("Job Sequence:", schedule)
print("Total Profit:", profit)
