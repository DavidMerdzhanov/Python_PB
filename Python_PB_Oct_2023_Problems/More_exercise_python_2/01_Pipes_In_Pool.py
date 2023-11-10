

volume_of_pool_in_liters = int(input())
pipe_1_flow = int(input())
pipe_2_flow = int(input())
hours_the_worker_absent = float(input())


pipe_1_total = pipe_1_flow * hours_the_worker_absent
pipe_2_total = pipe_2_flow * hours_the_worker_absent

both_pipes_total = pipe_1_total + pipe_2_total

percent_filled = both_pipes_total / volume_of_pool_in_liters * 100

pipe_1_percentage = pipe_1_total / both_pipes_total * 100
pipe_2_percentage = pipe_2_total / both_pipes_total * 100

if both_pipes_total <= volume_of_pool_in_liters:
    print(f"The pool is {percent_filled}% full.\
     Pipe 1: {pipe_1_percentage:.2f}%. Pipe 2: {pipe_2_percentage:.2f}%.")
else:
    print(f"For {hours_the_worker_absent} hours\
     the pool overflows with {both_pipes_total - volume_of_pool_in_liters} liters.")

