lost_fights = int(input())
price_helmet_repair = float(input())
price_sword_repair = float(input())
price_shield_repair = float(input())
price_armor_repair = float(input())

sum_for_repair = 0
counter_shield_brakes = 0
counter_helmet = 0
counter_shield = 0
counter_corner = 0
counter_sward = 0
counter_armor = 0

for n_fight in range(1, lost_fights +1):
    if n_fight % 2 == 0:
        sum_for_repair += price_helmet_repair
        counter_helmet += 1

    if n_fight % 3 == 0:
        sum_for_repair += price_sword_repair
        counter_sward += 1

    if n_fight % 2 ==0 and n_fight %3 ==0:
        sum_for_repair += price_shield_repair
        counter_shield_brakes += 1
        counter_shield += 1

    if counter_shield_brakes != 0 and counter_shield_brakes % 2 == 0:
        sum_for_repair += price_armor_repair
        counter_armor += 1

print(f'Gladiator expenses: {sum_for_repair} aureus')