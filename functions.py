from datetime import datetime

# time
def time_now():
    i = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    return i
