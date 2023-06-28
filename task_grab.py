import os
from time import sleep


# Get a snapshot of system processes
# interval is how often to get a snapshot
# time is how many intervals to iterate
def get_tasks(interval, time):

	for i in range(time):
		print(os.system('ps -ejH'))
		sleep(interval)


# Initial ps command to create hash table
def get_tasks_init():
	proc = os.popen('ps -ejH').read()
	return proc


# Create a hash table of tasks to update
# live view every n seconds (determined by user)
def create_hash_table():
	proc = get_tasks_init()
	pids = proc.splitlines()

	for i in pids:
		hashed = hash(pids[i])

