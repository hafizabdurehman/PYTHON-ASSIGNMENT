import time

def countdown_timer(seconds):

    while seconds >= 0:

        mins, secs = divmod(seconds, 60)  # Convert seconds to MM:SS format

        timer = f"{mins:02}:{secs:02}"

        print(timer, end="\r")  # Overwrites the previous output

        time.sleep(1)  # Pause for 1 second

        seconds -= 1

    print("\n⏰ Time's up! 🚀")

# Get input from user

try:
    total_time = int(input("⏳ Enter the countdown time in seconds: "))

    countdown_timer(total_time)
    
except ValueError:
    print("⚠️ Please enter a valid number.")