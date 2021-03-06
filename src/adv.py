from room import Room
from player import Player
from item import Item 

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player("Ruby", room['outside'])

rock = Item("Rock", "Just a rock.")
sword = Item("Sword", "A magical sword.")
potion = Item("Potion", "Restore's health.")
rubies = Item("Rubies", "Not gold but still worth keeping.")
scroll = Item("Scroll", "Left over by the previous adventurers.")

room["outside"].items.append(rock) 
room["outside"].items.append(potion)
room["foyer"].items.append(sword)
room["overlook"].items.append(potion)
room["overlook"].items.append(rock) 
room["narrow"].items.append(rubies)
room["treasure"].items.append(scroll)

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

directions = ['n', 's', 'e', 'w']

print(player.room)

while True:
    cmd = input("Please enter a valid input : ")
    if cmd in directions:
        player.move(cmd)
    
    elif cmd == 'i': 
        player.display_inventory()  

    elif cmd == 'take rock': 
        player.add_item(rock) 
        player.room.take_item(rock)

    elif cmd == 'drop rock': 
        player.drop_item(rock) 
        player.room.add_items(rock)
    
    elif cmd == 'take sword': 
        player.add_item(sword) 
        player.room.take_item(sword)

    elif cmd == 'drop sword': 
        player.drop_item(sword)
        player.room.add_items(sword)
    
    elif cmd == 'take potion': 
        player.add_item(potion) 
        player.room.take_item(potion)
    
    elif cmd == 'drop potion': 
        player.drop_item(potion) 
        player.room.add_items(potion)
    
    elif cmd == 'take rubies': 
        player.add_item(rubies) 
        player.room.take_item(rubies)
    
    elif cmd == 'drop rubies': 
        player.drop_item(rubies) 
        player.room.add_items(rubies)
    
    elif cmd == 'take scroll': 
        player.add_item(scroll)
        player.room.take_item(scroll)

    elif cmd == 'drop scroll': 
        player.drop_item(scroll) 
        player.room.add_items(scroll)

    elif cmd == 'q':
        print("Thanks for Playing! :)")
        break
    else:
        print("Oops! Choose a valid input.") 
    