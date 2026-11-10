import datetime
import time
import sys

print("Press Ctrl+C to stop the clock.\n")

try:
    while True:
        # Get the current precise time
        now = datetime.datetime.now()
        
        # Format the time string including microseconds
        time_str = now.strftime("%H:%M:%S.%f")
        
        # Print to the same line continuously
        sys.stdout.write(f"\rCurrent Time: {time_str}")
        sys.stdout.flush()
        
        # Small pause to reduce CPU usage while maintaining high precision
        time.sleep(0.0001)
except KeyboardInterrupt:
    print("\nClock stopped.")
