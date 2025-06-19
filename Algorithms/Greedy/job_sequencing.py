input_array = [(5, 2, "J1"), (12, 1, "J2"), (30, 4, "J3"), (35, 3, "J4"), (25, 4, "J5"), (15, 3, "J6"), (20, 2, "J7")]

def job_sequence(array: list): 
  jobs = sorted(array, key=lambda x: x[0], reverse=True)
  maximum_deadline = max(array, key=lambda x: x[1])
  job_slot = [0] * maximum_deadline[1]

  for job in jobs:
    n = job[2]
    i = job[1] - 1
    if (job_slot[i] == 0):
      job_slot[i] = n
    else:
      while True:
        if (i < 0):
          break 
        if (job_slot[i] == 0):
          job_slot[i] = n 
          break
        i -= 1
  
job_sequence(input_array)