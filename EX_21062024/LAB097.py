import  time
def my_logs_decorator(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print("Time Taken"+str(end_time-start_time))
    return wrapper()

@my_logs_decorator
def logs_function():
    time.sleep(5)
    print("The time taken to run the log is")