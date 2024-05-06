from datetime import datetime

def get_current_time():
	return datetime.now()

def time_to_timestamp(time):
	return time.strftime("%Y-%m-%d %H:%M:%S")

def get_current_timestamp():
	return time_to_timestamp(get_current_time())

def timestamp_to_time(timestamp):
	return datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
