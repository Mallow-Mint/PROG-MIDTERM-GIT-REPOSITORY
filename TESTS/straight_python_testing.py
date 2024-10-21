enemy_hp_list = [15, 20, 20, 10]
enemy_count = len(enemy_hp_list)

total_enemy_hp = 0
for x in range(enemy_count):
    total_enemy_hp += enemy_hp_list[x]

print(total_enemy_hp)


enemy_hp_list = [0, 0, 0, 0]
total_enemy_hp = 0
for x in range(enemy_count):
    total_enemy_hp += enemy_hp_list[x]

print(total_enemy_hp)