
import pygame

#adjacency_list
#             0        1       2       3            4        5       6            7         8        9             10           11          12         13        14        15          16          17        18          19        20     
vir_map = [[1, 3], [0, 2, 4], [1], [0, 4, 6], [1, 3, 5, 7], [4], [3, 7, 9], [4, 6, 8, 10], [7], [6, 10, 12], [7, 9, 11, 13], [10, 14], [9, 13, 15], [10, 12], [11, 17], [12, 18], [15, 17, 19], [14, 16], [15, 19], [16, 18, 20], [19]]

#list of places on the map
a = ['FISHMANDILL', 'ONAGI TRAIL', 'YNOT KWAH PARK', 'GNOME FEST', 'ANIME HAVEN', 'SANJIRAMA', 'ANDREW TATE', 'KING', 'PEASANT', 'POISON IVY', 'GOLD DIGGER', 'DEEP', 'KOBE', 'SANDY CHEEKS', 'FRESH PRINCE', 'HARAMBE', 'TWITTER', 'RICK SANCHEZ', 'SWING & SLIDE', 'BREAKING BAD', 'GOTHAM']

#list of descriptions according to the place on the map
b = ['Fishmandill contains one of biggest piranhas in the world. Try to avoid the pond at all cost!. You have 2 exits, the ONAGI TRAIL to the EAST, or the GNOME FEST to the SOUTH of you', 'Onagi Trail is one of the most beautiful trails in the world! It is mostly covered by pink blossom trees. You have 3 exits, the FISHMANDILL to the WEST, the ANIME HAVEN to the SOUTH, or the YNOT KWAH to the EAST of you', 
     'Ynot Kwah Park has had the most famous skateboarders skate on it. Such as the internet sensation Tony Hawk! You have 1 exit, the ONAGI TRAIL to the WEST of you', 'GNOME FEST is a lawn filled with all kinds of gnomes. Beware of the gnomes with chainsaws, they tend to be carrying real ones! You have 3 exits, the FISHMANDILL to the NORTH, the ANIME HAVEN to the east, or the ANDREW TATE to the SOUTH of you', 
     'Anime Haven is where you watch your favourite anime. Here the creator of the show ONE PIECE, Eiichiro Oda, watches over you. You have 4 exits, the ONAGI TRAIL to the NORTH, the GNOME FEST to the WEST, the SANJIRAMA to the EAST, or the KING to SOUTH of you', 'Sanjirama is the kitchen where the magic happens. Legendary cooks such as Gordon Ramsey have cooked here. You have 1 exit, the ANIME HAVEN to the WEST of you', 
     'Andrew Tate is the garage where the hard work is done! What colour is your Buggati? You have 3 exits, the GNOME FEST to the NORTH, the KING to the EAST, or the POISON IVY to the SOUTH of you', 'King is the master bedroom where you rest with a glass of wine. NO SLEPPING allowed here! You have 4 exits, the ANIME HAVEN to the NORTH, the ANDREW TATE to the WEST, the PEASANT to the EAST, or the GOLD DIGGER to the SOUTH of you',
     'Peasant is the bedroom of your dreams. It is equipped with LED lightings and gaming accessories. You have 1 exit, the KING to the WEST of you', 'This garden contains many dandelions. The dandelions have actual lion faces. You have 3 exits, the ANDREW TATE to the NORTH, the GOLD DIGGER to the EAST, or the KOBE to the SOUTH of you',
     'This outdoor porch is made of gold. All the gold has been acquired by gold diggers. You have 4 exits, the KING to the NORTH, the GARDEN to the WEST, THE DEEP to the EAST, or the SANDY CHEEKS to the SOUTH of you', 'This pool is deeper than the Mariana Trench. Beware of the unknown creatures that lurk within! You have 2 exits, the GOLD DIGGER to the WEST, or the FRESH PRINCE to the SOUTH of you', 
     'This court is where Kobe Bryant had his last practise. This court is now used to train young Kobes. You have 3 exits, the POISON IVY to the NORTH, the SANDY CHEEKS to the EAST, or the HARAMBE to the SOUTH of you', 'This treehouse has monkeys swinging around everywhere. Hide your food and do not look them in the eye! You have 2 exits, the GOLD DIGGER to the NORTH, or the KOBE to the WEST of you',
     'This is the pool house where the Fresh Prince of Bel Air spent most of his days. The luxury present in here is unmatched! You have 2 exits, THE DEEP to the NORTH, or the RICK SANCHEZ to the SOUTH of you', 'A calistenics park where you can find many fitness influencers. Even Chis Heria was spotted working out here! You have 3 exits, the KOBE to the NORTH, the TWITTER to the EAST, or the SWING & SLIDE to the SOUTH of you',
     'An outhouse which smells like a shithole. Here you can empty out all your pyhsical and mental toxic waste. You have 3 exits, the HARAMBE to the WEST, the RICK SANCHEZ to the EAST, or the BREAKING BAD to the SOUTH of you', 'This equipment room is full of mysteries. Beware of the old man with blue frizzy hair and a lab coat. You have 2 exits, the FRESH PRINCE to the NORTH, or the TWITTER to the WEST of you',
     'This is a playground where you can become a kid again. All rides are engineered to be safe for all ages. You have 2 exits, the HARAMBE to the NORTH, or the BREAKING BAD to the EAST of you', 'A parking lot that is prone to car theft. If your park you car here, then you better chain up the doors. You have 3 exits, the TWITTER to the NORTH, the SWING & SLIDE to the WEST, or the GOTHAM to the EAST of you',
     'This abandoned warehouse is full of bats. Beware of the hidden traps and most importantly the JOKER! You have 1 exit, the BREAKING BAD to the WEST of you']

#uploading image to pygame window
src_img = pygame.image.load('Asg_10_Map.jpg') #loading the image file 
(w,h) = src_img.get_size() #finding the dimensions of the image
window = pygame.display.set_mode((w,h)) #setting the pygame window = dimensions of image
window.blit(src_img, (0,0)) #blit the image
pygame.display.update() #updating the pygame window

def valuables(x):
        #making it global so the changes will be recognized outside the function
        global items
        items = [] #valuable counter
        
        #if user is at the Garage/Gym
        if x == 6:
                print(end='\n')
                item = str(input('You have found a box of PRE-WORKOUT! Enter "take" if you would like add the item to your inventory(take) : ')) #Take input from the user
                
                #if user takes the valuable
                if item == 'take':
                        items.append('(PRE-WORKOUT) ') #add 1 to the valuable counter
                        print(end = '\n')
                        print('PRE-WORKOUT has been added to your invertory!')
        
        #if user is at the Treehouse
        if x == 13:
                print(end='\n')
                item = str(input('You have found a BASKETBALL! Enter "take" if you would like add the item to your inventory(take) : ')) #Take input from the user
                
                #if user takes the valuable
                if item == 'take':
                        items.append('(BASKETBALL) ') #add 1 to the valuable counter
                        print(end = '\n')
                        print('BASKETBALL has been added to your inventory!')
        
        #if user is at the Abandoned Warehouse
        if x == 20:
                print(end='\n')
                item = str(input('You have found a TITANIUM ROLEX! Enter "take" if you would like add the item to your inventory(take) : ')) #Take input from the user
                
                #if user takes the valuable
                if item == 'take':
                        items.append('(TITANIUM ROLEX) ') #add 1 to the valuable counter
                        print(end = '\n')
                        print('TITANIUM ROLEX has been added to your invertory!')

def main():
        x = 1 #node or index counter
        global items_found
        items_found = [] #valuables counter
        u = a[x] #place variable
        v = b[x] #place description variable

        print(end='\n')
        print('WELCOME! In order to win, you have to collect all 3 of the valuables located at random locations on the map. To pick up valuables enter "take".')
        print(end='\n')
        print('Once you pick up(take) a valuable, it is added to your inventory. Which can be called forth anytime by entering "inventory".')
        print(end='\n')
        direct = str(input('You are at the ' +u+ '. ' +v+ '. Pick an exit by typing a direction (north, south, east, west), or call for "inventory" : ')) #direction input from the user to iniate the loop below

        #if user asks for inventory
        if direct == 'inventory':
                print(end='\n')
                print('Here is your inventory : ' +''.join(items_found))
                print(end='\n')
                direct = str(input('You are at the ' +u+ '. ' +v+ '. Pick an exit by typing a direction (north, south, east, west), or call for "inventory" : '))

        #post-codition loop set to repeat until all valuables have been found
        while ('(PRE-WORKOUT) ' and '(BASKETBALL) ' and '(TITANIUM ROLEX) ') not in items_found:
                
                #if the user inputs 'north'
                if direct == 'north':
                        
                        #checking to see if the exit chosen by the user exists on the map; just in case the user inputs a direction where no exit exists.
                        if (x-3) in vir_map[x]:
                                x -= 3 #moving the player to the exitted place
                                u = a[x] #changing place variable according to the new place
                                v = b[x] #changing place description variable according to the new place
                                valuables(x) #checking for valuables in the new place
                                
                                #if valuable found
                                if items != []:
                                        items_found.append(items[0]) #add valuable to list
                                
                                #if all valuables are not found
                                if ('(PRE-WORKOUT) ' and '(BASKETBALL) ' and '(TITANIUM ROLEX) ') not in items_found:
                                        print(end='\n')
                                        direct = str(input('You are at the ' +u+ '. ' +v+ '. Pick an exit by typing a direction (north, south, east, west), or call for "inventory" : ')) #ask the user for direction input again
                                        
                                        #if user asks for inventory
                                        if direct == 'inventory':
                                                print(end='\n')
                                                print('Here is your inventory : ' +''.join(items_found))
                                                print(end='\n')
                                                direct = str(input('You are at the ' +u+ '. ' +v+ '. Pick an exit by typing a direction (north, south, east, west), or call for "inventory" : '))
                
                #if the user inputs 'south'                
                elif direct == 'south':
                        #checking to see if the exit chosen by the user exists on the map; just in case the user inputs a direction where no exit exists.
                        if (x+3) in vir_map[x]:
                                x += 3 #moving the player to the exitted place
                                u = a[x] #changing place variable according to the new place
                                v = b[x] #changing place description variable according to the new place
                                valuables(x) #checking for valuables in the new place
                                
                                #if valuable found
                                if items != []:
                                        items_found.append(items[0]) #add valuable to list
                                
                                #if all valuables are not found
                                if ('(PRE-WORKOUT) ' and '(BASKETBALL) ' and '(TITANIUM ROLEX) ') not in items_found:
                                        print(end='\n')
                                        direct = str(input('You are at the ' +u+ '. ' +v+ '. Pick an exit by typing a direction (north, south, east, west), or call for "inventory" : ')) #ask the user for direction input again
                                        
                                        #if user asks for inventory
                                        if direct == 'inventory':
                                                print(end='\n')
                                                print('Here is your inventory : ' +''.join(items_found))
                                                print(end='\n')
                                                direct = str(input('You are at the ' +u+ '. ' +v+ '. Pick an exit by typing a direction (north, south, east, west), or call for "inventory" : '))
                
                #if the user inputs 'east'                
                elif direct == 'east':
                        #checking to see if the exit chosen by the user exists on the map; just in case the user inputs a direction where no exit exists.
                        if (x+1) in vir_map[x]:
                                x += 1 #moving the player to the exitted place
                                u = a[x] #changing place variable according to the new place
                                v = b[x] #changing place description variable according to the new place
                                valuables(x) #checking for valuables in the new place
                                
                                #if valuable found
                                if items != []:
                                        items_found.append(items[0]) #add valuable to list
                                
                                #if all valuables are not found
                                if ('(PRE-WORKOUT) ' and '(BASKETBALL) ' and '(TITANIUM ROLEX) ') not in items_found:
                                        print(end='\n')
                                        direct = str(input('You are at the ' +u+ '. ' +v+ '. Pick an exit by typing a direction (north, south, east, west), or call for "inventory" : ')) #ask the user for direction input again
                                        
                                        #if user asks for inventory
                                        if direct == 'inventory':
                                                print(end='\n')
                                                print('Here is your inventory : ' +''.join(items_found))
                                                print(end='\n')
                                                direct = str(input('You are at the ' +u+ '. ' +v+ '. Pick an exit by typing a direction (north, south, east, west), or call for "inventory" : '))
                
                #if the user inputs 'west'                
                elif direct == 'west':
                        #checking to see if the exit chosen by the user exists on the map; just in case the user inputs a direction where no exit exists.
                        if (x-1) in vir_map[x]:
                                x -= 1 #moving the player to the exitted place
                                u = a[x] #changing place variable according to the new place
                                v = b[x] #changing place description variable according to the new place
                                valuables(x) #checking for valuables in the new place
                                
                                #if valuable found
                                if items != []:
                                        items_found.append(items[0]) #add valuable to list
                                
                                #if all valuables are not found
                                if ('(PRE-WORKOUT) ' and '(BASKETBALL) ' and '(TITANIUM ROLEX) ') not in items_found:
                                        print(end='\n')
                                        direct = str(input('You are at the ' +u+ '. ' +v+ '. Pick an exit by typing a direction (north, south, east, west), or call for "inventory" : ')) #ask the user for direction input again
                                        
                                        #if user asks for inventory
                                        if direct == 'inventory':
                                                print(end='\n')
                                                print('Here is your inventory : ' +''.join(items_found))
                                                print(end='\n')
                                                direct = str(input('You are at the ' +u+ '. ' +v+ '. Pick an exit by typing a direction (north, south, east, west), or call for "inventory" : '))
                
                #if the user mispells the direction
                elif direct != 'north' or 'south' or 'east' or 'west':
                        print(end='\n')
                        print('You entered the WRONG DIRECTION!')
                        print(end='\n')
                        direct = str(input('You are at the ' +u+ '. ' +v+ '. Pick an exit by typing a direction (north, south, east, west), or call for "inventory" : '))

main()
    
#Winning outro
print(end='\n')
print(end='\n')        
print('CONGRATULATIONS! You have found all the Valuables!')
print(end='\n')
print(end='\n')
print('Here is your inventory : ' +''.join(items_found))
print(end='\n')
print(end='\n')
print('GAME OVER')
print(end='\n')


        


