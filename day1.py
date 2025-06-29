
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

# Comment: This code defines a function that greets the user based on the current time of day.
# It uses the datetime module to get the current time and prints a greeting accordingly.
# The function is called when the script is run directly.
# The greeting changes based on the hour of the day, providing a personalized message.
# The code is structured to be run as a script, and it will greet the user based on the time of day.
# The greeting is printed in a user-friendly format, including the current time.
