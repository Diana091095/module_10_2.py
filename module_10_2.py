import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        self.left = 100
        self.days = 0
        print(f'{self.name}, на нас напали!')
        while self.left:
            self.days += 1
            self.left -= self.power
            print(f"{self.name} сражается {self.days} день(дня), осталось {self.left} воинов.")
            time.sleep(1)
        print(f"{self.name} одержал победу спустя {self.days} дней(дня)!")


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print(f'Все битвы закончились')
