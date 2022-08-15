jobs_int = [int(j) for j in input().split(", ")]
job_index = int(input())

job_counter = 0
cycle = []
for idx, job in enumerate(jobs_int):
    cycle.append((job, idx))

cycle = sorted(cycle)
for job, idx in cycle:
    job_counter += job
    if idx == job_index:
        break

print(job_counter)


