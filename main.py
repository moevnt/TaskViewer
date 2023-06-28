import os
from time import sleep
import psutil


def get_tasks(interval, time):

	for i in range(time):
		print(os.system('ps -ejH'))
		sleep(interval)


if __name__ == '__main__':
	get_tasks()
