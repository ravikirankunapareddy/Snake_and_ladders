import random
no_of_players=random.randint(2,5)
snakes=[0]*100
ladder=[0]*100
current=0
start=list(range(2,100))
end=list(range(1,100))
random.shuffle(start)
for i in range(0,10):
    start_index=start.pop()
    while(True):
        random.shuffle(end)
        end_index=end.pop()
        if(end_index>start_index):
            break
        else:
            end.append(end_index)
    ladder[start_index-1]=end_index
start=list(range(2,100))
end=list(range(1,100))
random.shuffle(start)
for i in range(0,10):
    start_index=start.pop()
    while(True):
        random.shuffle(end)
        end_index=end.pop()
        if(end_index<start_index):
            break
        else:
            end.append(end_index)
    snakes[start_index-1]=end_index
print(snakes)
print(ladder)
player_position=[1]*no_of_players
no_of_players_finished=0
can_roll=[1]*no_of_players
win_pos=[0]*no_of_players
while(no_of_players_finished<no_of_players):
    player=0
    while(player<no_of_players):
        if(can_roll[player]==0):
            player+=1
            continue
        die=random.randint(1,6)
        print(f"Player {player + 1} rolled {die}")
        current=player_position[player]+die
        if(current==100):
            no_of_players_finished+=1
            player_position[player]=100
            can_roll[player]=0
            win_pos[player]=no_of_players_finished
        elif(current>100):
            player+=1
            continue
        else:
            if(ladder[current-1]>0):
                player_position[player]=ladder[current-1]
                current=ladder[current-1]
                print("####")
                if(ladder[current-1]==100):
                    no_of_players_finished+=1
                    can_roll[player]=0
                    win_pos[player]=no_of_players_finished
                    continue
            elif(snakes[current-1]>0):
                player_position[player]=snakes[current-1]
                current=snakes[current-1]
                print("~~~~~~")
            else:
                player_position[player]=current
            print(f"{player+1}-->{current}")
            if(die!=6):
                player+=1

for i in range(no_of_players):
    print(f"player{i+1},{win_pos[i]}")
