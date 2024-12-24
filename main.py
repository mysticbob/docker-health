# main.py
import time
import random
import os

STATUS_FILE = os.getenv('STATUS_FILE', 'status.txt')

def set_status():
    status = random.choice(['good', 'bad'])
    with open(STATUS_FILE, 'w') as f:
        f.write(status)
    print(f"Set status to: {status}")

def main():
    print("Starting main application...")
    while True:
        set_status()
        time.sleep(10)  # Wait for 10 seconds before next status change

if __name__ == "__main__":
    main()
