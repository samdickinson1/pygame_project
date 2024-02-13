import random
#defining variables
full_map = []
def room_map():
    room_added = 0
    last_room_added_x = 0
    last_room_added_y = 0
    current_point_x = 0
    current_point_y = 0
    start_point_x = 0
    start_point_y = 0
    total_room = 0
    generation = True
    
    #creates an empty map
    map_length = 5
    map_height = 5
    big_map = []
    big_map = [[] for _ in range(map_height)]
    print(big_map)
    for j in range(map_length):
        for i in range(map_height):
            big_map[i-1].append(0)
        
    
    print(big_map)
            

    print(current_point_x,current_point_y)
    for i in range(map_height):
        print(big_map[i])

        

    #chooses a random start point on that map
    start_point_x = random.randint(1,map_length-2)
    start_point_y = random.randint(1,map_height-2)
    big_map[start_point_y][start_point_x] = 2


    print(big_map,start_point_x,start_point_y)
    current_point_x = start_point_x
    current_point_y = start_point_y
    print(current_point_x,current_point_y)
    #generates the rest of the rooms
    while generation == True:
        #checks that it isn't out of range
        if not current_point_y -1 < 0:
            #checks if there is a room up
            if big_map[current_point_y-1][current_point_x]  == 0:
                #randomly chooses to put a room there or not currently a 60% chance
                if random.randint(1,6) >= 5:
                    #adds that room to the map array
                    big_map[current_point_y-1][current_point_x] = 1
                    #adds a room to the room counter so you can see if a room has been added that cycle
                    room_added += 1
                    #saves the coordinates for the added room
                    last_room_added_x = current_point_x
                    last_room_added_y = current_point_y-1
                    #adds to the total room count so we can assure a certain amount of rooms
                    total_room +=1
        if not current_point_x + 1 > map_length-1:
            #right
            if big_map[current_point_y][current_point_x+1] == 0:
                if random.randint(1,6) >= 5:
                    big_map[current_point_y][current_point_x+1] = 1
                    room_added +=1
                    last_room_added_x = current_point_x+1
                    last_room_added_y = current_point_y
                    total_room +=1
        if not current_point_y + 1 > map_height-1:
            #down
            if big_map[current_point_y+1][current_point_x] == 0:
                if random.randint(1,6) >= 5:
                    big_map[current_point_y+1][current_point_x] = 1
                    room_added += 1
                    last_room_added_x = current_point_x
                    last_room_added_y = current_point_y+1
                    total_room +=1
        if not current_point_x -1 < 0:
            #left
            if big_map[current_point_y][current_point_x-1] == 0:
                if random.randint(1,6) >= 5:
                    big_map[current_point_y][current_point_x-1] = 1 
                    room_added +=1
                    last_room_added_x = current_point_x-1
                    last_room_added_y = current_point_y
                    total_room +=1
        #checks if any rooms were added 
        
        if room_added == 0:
            #checks if the map has enough rooms and that the start and end are far enough away
            if total_room >= 10 and abs(abs(last_room_added_x)-abs(start_point_x))+abs(abs(last_room_added_y)-abs(start_point_y)) >= 4:
                generation = False 
                #adds the end room
                big_map[last_room_added_y][last_room_added_x] = 3
            #if the conditions are not fuffilled this resets the process by putting the variables back to their original values
            else:
                print("aaaaaa")
                big_map = []
                big_map = [[] for _ in range(map_height)]
                for j in range(map_length):
                    for i in range(map_height):
                        big_map[i].append(0)
                start_point_x = random.randint(1,map_length-2)
                start_point_y = random.randint(1,map_height-2)
                current_point_x = start_point_x
                current_point_y = start_point_y
                last_room_added_x = current_point_x
                last_room_added_y = current_point_y
                print(start_point_x,start_point_y)
                big_map[start_point_y][start_point_x] = 2     
                total_room = 0    
        #if rooms were added it tries to add rooms again now from the last added room  
        else:
            current_point_x = last_room_added_x
            current_point_y = last_room_added_y
        #resets the room added counter as it is a new cycle 
        room_added = 0

    print(current_point_x,current_point_y)
    for i in range(map_height):
        print(big_map[i])
    return big_map,map_length,map_height

#takes the room map and fills each room
def fill_map(big_map,map_length,map_height):
    room_length = 8
    room_height = 8
    full_map = []
    #constructs the full map array
    full_map = [[] for _ in range(map_height * (room_height - 1) + 1)]
    for j in range(map_length * (room_length - 1) + 1):
        for i in range(map_height * (room_height - 1) + 1):
            full_map[i - 1].append(0)
    #walls
    for i in range(map_height):
        for j in range(map_length):
            #checks if there is a room at the current i and j values 
            if big_map[i][j] == 1 or big_map[i][j] == 2 or big_map[i][j] == 3:
                #creates the walls for each room
                for k in range(room_length):
                    full_map[(room_height - 1) * i][(room_length - 1) * j + k ] = 1
                    full_map[(room_height - 1)* (i+1)][(room_length - 1) * j + k] = 1
                for k in range(room_height):
                    full_map[(room_height - 1) * i + k][(room_length - 1) * j ] = 1
                    full_map[(room_height - 1)* i + k][(room_length - 1) * (j+1)] = 1
    #doorways
    for i in range(map_height):
        for j in range(map_length):
            if big_map[i][j] == 1 or big_map[i][j] == 2 or big_map[i][j] == 3:
                #this part checks if there are two rooms next to each other and generates a doorway between them
                #right
                #checks if it isnt out of index
                if not j + 1 > map_length - 1:
                    #check if there is a room to the right
                    if big_map[i][j + 1] == 1 or big_map[i][j + 1] == 2 or big_map[i][j + 1] == 3:
                        #randomly creates a doorway along the shared wall
                        full_map[(room_height - 1) * i + random.randint(1,room_height - 2)][(room_length - 1) * (j+1)] = 0
                #only two directions are needed as it is between two rooms so if all four directions were checked it would create two doorways between each room
                #down
                if not i + 1 > map_height - 1:
                    if big_map[i + 1][j] == 1 or big_map[i + 1][j] == 2 or big_map[i + 1][j] == 3:
                        full_map[(room_height - 1) * (i+1)][(room_length - 1) * j + random.randint(1,room_length - 2)] = 0
    #spawn and endpoint 
    for i in range(map_height):
        for j in range(map_length):
            if big_map[i][j] == 2:
                full_map[(room_height - 1) * i + random.randint(1,room_height - 2)][(room_length - 1) * j + random.randint(1,room_length - 2)] = 2
            if big_map[i][j] == 3:
                full_map[(room_height - 1) * i + random.randint(1,room_height - 2)][(room_length - 1) * j + random.randint(1,room_length - 2)] = 3
                
        
    for i in range(map_height * (room_height - 1) + 1):
        print(full_map[i])
    return full_map




big_map,map_length,map_height = room_map()
full_map = fill_map(big_map,map_length,map_height)


    
