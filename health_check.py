# health_check.py
import sys
import os

STATUS_FILE = os.getenv('STATUS_FILE', 'status.txt')

def check_health():
    if not os.path.exists(STATUS_FILE):
        print("Status file does not exist.")
        sys.exit(1)

    with open(STATUS_FILE, 'r') as f:
        status = f.read().strip()

    if status == 'good':
        print("Status is GOOD.")
        sys.exit(0)
    else:
        print("Status is BAD.")
        sys.exit(1)

if __name__ == "__main__":
    check_health()
