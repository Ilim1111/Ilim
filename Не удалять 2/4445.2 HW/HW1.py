import time

class Timer:
    def __init__(self, initial_time):
        self.initial_time = initial_time   
        self.time_remaining = initial_time
        self.is_running = False

    def get_time(self):
        return self.time_remaining

    def start(self):
        if self.is_running:
            return 
        self.is_running = True
        while self.time_remaining > 0:
            print(self.time_remaining)
            time.sleep(1)
            self.time_remaining -= 1

        self.is_running = False
        print("Таймер 0.")

    def reset(self):
        self.time_remaining = self.initial_time

timer = Timer(10)

print(timer.get_time())  

timer.start()

print(timer.get_time())

timer.reset()

print(timer.get_time())  
