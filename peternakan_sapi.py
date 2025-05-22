import time

class Cow:
    def __init__(self):
        self.hungry = True
        self.sick = False
    
    def feed(self):
        self.hungry = False
    
    def pass_day(self):
        # Jika tidak diberi makan, sapi jadi lapar lagi dan bisa sakit
        if self.hungry:
            self.sick = True
        else:
            self.sick = False
        self.hungry = True

    def produce_milk(self):
        if not self.hungry and not self.sick:
            return 1  # liter susu
        else:
            return 0

class Farm:
    def __init__(self):
        self.cows = [Cow()]
        self.milk = 0
        self.money = 10
        self.feed_stock = 5

    def feed_cows(self):
        if self.feed_stock >= len(self.cows):
            for cow in self.cows:
                cow.feed()
            self.feed_stock -= len(self.cows)
            print("Sapi sudah diberi makan.")
        else:
            print("Pakan tidak cukup!")

    def sell_milk(self):
        price_per_liter = 5
        total_milk = sum(cow.produce_milk() for cow in self.cows)
        self.money += total_milk * price_per_liter
        print(f"Menjual {total_milk} liter susu, dapat {total_milk * price_per_liter} uang.")
        self.milk = 0  # setelah jual, susu habis

    def buy_feed(self, amount):
        cost_per_feed = 2
        total_cost = amount * cost_per_feed
        if self.money >= total_cost:
            self.feed_stock += amount
            self.money -= total_cost
            print(f"Berhasil beli {amount} pakan.")
        else:
            print("Uang tidak cukup untuk beli pakan!")

    def buy_cow(self):
        cost_cow = 20
        if self.money >= cost_cow:
            self.cows.append(Cow())
            self.money -= cost_cow
            print("Beli sapi baru!")
        else:
            print("Uang tidak cukup untuk beli sapi!")

    def next_day(self):
        for cow in self.cows:
            cow.pass_day()
        print(f"Hari berikutnya... Kamu punya {len(self.cows)} sapi, {self.feed_stock} pakan, uang {self.money}.")

def main():
    farm = Farm()
    day = 1
    while True:
        print(f"\n=== Hari ke-{day} ===")
        print(f"Uang: {farm.money}, Pakan: {farm.feed_stock}, Jumlah sapi: {len(farm.cows)}")
        print("Pilihan:")
        print("1. Beri makan sapi")
        print("2. Jual susu")
        print("3. Beli pakan")
        print("4. Beli sapi")
        print("5. Lewatkan hari")
        print("6. Keluar")

        choice = input("Pilihanmu: ")
        if choice == "1":
            farm.feed_cows()
        elif choice == "2":
            farm.sell_milk()
        elif choice == "3":
            amount = int(input("Beli berapa pakan? "))
            farm.buy_feed(amount)
        elif choice == "4":
            farm.buy_cow()
        elif choice == "5":
            farm.next_day()
            day += 1
        elif choice == "6":
            print("Game selesai.")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
