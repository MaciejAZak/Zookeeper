# put your python code here
duration = input()
food = input()
flight = input()
night = input()

money = int(duration) * int(food) + int(flight) * 2 + (int(duration) - 1) * int(night)
print(money)
