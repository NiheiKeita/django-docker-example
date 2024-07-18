
from apscheduler.schedulers.background import BackgroundScheduler

def example():
    print("Hello, World!")

def start():
    print("Hello, World!")
    scheduler = BackgroundScheduler()
    scheduler.add_job(example, 'interval', seconds=5)
    scheduler.start()