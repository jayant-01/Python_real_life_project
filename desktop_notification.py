import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title="alert",
            message="hello there",
            timeout=10
        )
        time.sleep(15)
