
from threading import Thread, Lock
from random import randint
from time import sleep
class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for i in range(100):
            r = randint(50, 500)
            self.balance += r
            if (self.balance >= 500 and self.lock == self.lock.locked()):
                self.lock.release()
            print(f'Пополнение: {r}. Баланс: {self.balance}')
            sleep(0.001)


    def take(self):
        for i in range(100):
            r = randint(50, 500)
            if (r<=self.balance):
                self.balance -= r
                print(f'Снятие: {r}. Баланс: {self.balance}')
            else:
                print("Запрос отклонён, недостаточно средств")
                self.lock.acquire()


bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')