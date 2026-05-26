# The Monty Hall Problem

from random import randint, choice

stay_wins = 0
switch_wins = 0

for _ in range(10000):
    car = randint(1, 3)
    player_pick = randint(1, 3)

    possible_doors_to_open = []

    for door in [1, 2, 3]:
        if door != player_pick and door != car:
            possible_doors_to_open.append(door)

    host_opens = choice(possible_doors_to_open)

    for door in [1, 2, 3]:
        if door != player_pick and door != host_opens:
            switch_pick = door

    if player_pick == car:
        stay_wins += 1

    if switch_pick == car:
        switch_wins += 1

print(f"After 10000 simulations:")
print(f"Staying won: {stay_wins} times")
print(f"Switching won: {switch_wins} times")

if switch_wins > stay_wins:
    print("\nConclusion: Switching doors is statistically better.")