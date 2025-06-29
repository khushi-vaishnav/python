
import datetime

def time_based_greeter():
    now = datetime.datetime.now()
    hour = now.hour
    if 5 <= hour < 12:
        greeting = "Good morning!"
    elif 12 <= hour < 18:
        greeting = "Good afternoon!"
    elif 18 <= hour < 22:
        greeting = "Good evening!"
    else:
        greeting = "Good night!"
    print(f"{greeting} The current time is {now.strftime('%H:%M:%S')}.")

if __name__ == "__main__":
    time_based_greeter()
