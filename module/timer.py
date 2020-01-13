from datetime import datetime


def timer_main():
    now = datetime.now()
    if now.minute == 22 or now.minute == 23:
        return 1
    else:
        return 0