# HEADER:
#-------------------------------------------------------------------------------------------------------------------------------------#

#   Program : Mini-Baseball Game Simulation
#   Programmer    : Sushrut Dhakal
#   Date    : September 25, 2022
#   Description : Simulates a mini one-sided baseball game with 5 innings using real player statistics

#   Statistics: File Read
#   Numbers of Players: 9
#   Numbers of Innings: 5

#   Data Structures:
#       Queue:
#           ⊛ bat_queue
#               Contains The list of players in the correct batting order
#
#       Dictionary:
#           ⊛ 2D Dictionary
#               ⊛ player_stats
#                   The value of the player name and the key of each of their statistic percentages
#           ⊛ 1D Dictionary
#                   Holds which player is at what base
#
#       Lists:
#           ⊛ ab_preview, hits_preview, doubles_preview, triples_preview, home_preview
#               Used to temporarily hold the stats from the file before converted to a dictorinary
#           ⊛ bases, new_bases
#               Holds the value of who is on what base


import random  # random used for visting team score and base percentage calculations

# INTIAL SETUP FUNCTION
def intial_setup():

    bat_queue = []  # intial bat queue

    # intial lists that will store strings of each column number
    ab_preview, hits_preview, doubles_preview, triples_preview, home_preview = ([],
        [],
        [],
        [],
        [],
    )

    STAT_FILE = open("player_statistics.txt", "r")  # opening stats file and reading

    lines = STAT_FILE.readlines() #read each line from the file

    for line in lines:  # split each line up and add the columns to their correct list
        words = line.split()

        if words:
            bat_queue.append(words[0])  # add coresponding column to a list

            ab_preview.append(words[1])
            ab = [int(x) for x in ab_preview]  # str list to int list for calculations

            hits_preview.append(words[2])
            hits = [int(x) for x in hits_preview]

            doubles_preview.append(words[3])
            doubles = [int(x) for x in doubles_preview]

            triples_preview.append(words[4])
            triples = [int(x) for x in triples_preview]

            home_preview.append(words[5])
            home = [int(x) for x in home_preview]

    STAT_FILE.close()  # close stats fine

    player_stats = {}  # intial empty dictionary

    # iterate through each element in the indivisual lists, do calculations and store in a dictionary
    for i in range(len(lines)):
        player_stats[bat_queue[i]] = {
            "Hits": round((hits[i] / ab[i]) * 100, 1),
            "Single": round(
                ((hits[i] - doubles[i] - triples[i] - home[i]) / hits[i]) * 100, 1
            ),
            "Doubles": round((doubles[i] / hits[i]) * 100, 1),
            "Triples": round((triples[i] / hits[i]) * 100, 1),
            "Homerun": round((home[i] / hits[i]) * 100, 1),
        }
    return player_stats, bat_queue #returns stats list and queue for later use

 #batting person made in ASCII / pixel art
def batting_person_ascii(): 
    print("    _--_     _")
    print(" __(._  )   //")
    print("  ~ \ / ```//")
    print(" ~        //  |")
    print("|               |")
    print("(              /")
    print(" ~._________.}")
    print(" /       )")
    print(" /         )")
    print(" |    /\   |")
    print(" /   /  \   )")
    print("/   /    \   )")
    print("\__/      \__/")
    print("| |       | |")
    print("+-+        +-+")

 #batter up text made in ASCII
def batter_up_ascii ():
    print("  ___     _     _____   _____   ___   ___        _   _   ___  ")
    print(" | _ )   /_\   |_   _| |_   _| | __| | _ \      | | | | | _ \ ")
    print(" | _ \  / _ \    | |     | |   | _|  |   /      | |_| | |  _/ ")
    print(" |___/ /_/ \_\   |_|     |_|   |___| |_|_\       \___/  |_|  ")

#home run text made in ASCII 
def homerun_ascii (): 
    print ("  _  _    ___    __  __   ___        ___   _   _   _  _   _ ")
    print (" | || |  / _ \  |  \/  | | __|      | _ \ | | | | | \| | | |")
    print (" | __ | | (_) | | |\/| | | _|       |   / | |_| | | .` | |_|")
    print (" |_||_|  \___/  |_|  |_| |___|      |_|_\  \___/  |_|\_| (_)")

#strike out text made in ASCII
def strike_out ():
    print ("  ___   _____   ___   ___   _  __  ___         ___    _   _   _____   _ ")
    print (" / __| |_   _| | _ \ |_ _| | |/ / | __|       / _ \  | | | | |_   _| | |")
    print (" \__ \   | |   |   /  | |  | ' <  | _|       | (_) | | |_| |   | |   |_|")
    print (" |___/   |_|   |_|_\ |___| |_|\_\ |___|       \___/   \___/    |_|   (_)")

# Main game function
def play_game ():
    player_stats, bat_queue = intial_setup () #calls the variables from setup function

    base_pos = 0 #intial player to base position 
    visting_score = random.randint (0, 20)  # the visting team score
    home_score, outs, inning, max_inning = 0, 0, 0, 5  # intialized variables

    bases = ['', '', '', ''] #intial empty base list

    while (inning != max_inning):  # until inning hits max inning

        batter = 0 #current batter (used to loop through queue)

        if (inning != max_inning):  # iterate until inning equals max inning
            batter_up_ascii () #UNCOMMENT LATER

            batting_person_ascii () #UNCOMMENT LATER
            print (f"\nBatter: {bat_queue[batter]}")  # print current batter
            print (f"{bat_queue[batter]}'s Stats: {player_stats[bat_queue[batter]]}")  # print current batters stats

            print (f"\nOn Deck: {bat_queue[batter+1]}")  # print next batter
            print (f"{bat_queue[batter+1]}'s Stats: {player_stats[bat_queue[batter+1]]}")  # print next batters stats
    
             # print out field 
            print ("-------------------------------------------")
            print (f"                      {bases[1]}          ")
            print ("                         /\               ")
            print ("                        /  \              ")
            print ("                       /    \             ")
            print ("                      /      \            ")
            print ("                     /        \           ")
            print ("                    /          \          ")
            print (f"             {bases[2]}                    {bases[0]}    ")
            print ("                    \          /          ")
            print ("                     \        /           ")
            print ("                      \      /            ")
            print ("                       \    /             ")
            print ("                        \  /              ")
            print ("                         \/               ")
            print ("                     Home Plate          ")
            print ("\n-------------------------------------------")

            enter = input ("Press ENTER to Bat") # Simulates a "bat" by pressing enter

            # removes decimal by multipling to ten thousand for random
            hits_ten_thous = ((player_stats[bat_queue[batter]]["Hits"]) * 100)

            # removes decimal by multipling to thousand for random
            single_thous = ((player_stats[bat_queue[batter]]["Single"]) * 10)
            double_thous = ((player_stats[bat_queue[batter]]["Doubles"]) * 10)
            triples_thous = ((player_stats[bat_queue[batter]]["Triples"]) * 10)
            homerun_thous = ((player_stats[bat_queue[batter]]["Homerun"]) * 10)

            # range for the chance of getting to each base (low - high)
            double_low = single_thous + 1
            double_high = single_thous + double_thous

            triple_low = double_high + 1
            triple_high = single_thous + double_thous + triples_thous

            homerun_low = triple_high + 1
            homerun_high = single_thous + double_thous + triples_thous + homerun_thous

            if (random.randint(1, 10000)) < hits_ten_thous:  # if they hit

                if (0 < random.randint(1, 1000)) < single_thous:  # 1B chance
                    print("-------------------SINGLE HIT-------------------")
                    base_pos = 1
                    base_calculation = shifting_bases (bases, bat_queue[batter], base_pos) #calls shifting base function
                    bases = base_calculation[0] #changes list to the right player on base       
                    home_score += base_calculation[1] #adds to score when homerun   
            
                elif (double_low < random.randint(1, 1000) < double_high):  # 2B chance
                    print("-------------------DOUBLE HIT-------------------")
                    base_pos = 2
                    base_calculation = shifting_bases (bases, bat_queue[batter], base_pos)
                    bases = base_calculation[0]
                    home_score += base_calculation[1]
                    
                elif (triple_low < random.randint(1, 1000) < triple_high):  # 3B chance
                    print("-------------------TRIPLE HIT-------------------")
                    base_pos = 3
                    base_calculation = shifting_bases (bases, bat_queue[batter], base_pos)     
                    bases = base_calculation[0]
                    home_score += base_calculation[1]
                    
                # homerun chance
                elif (homerun_low < random.randint(1, 1000) < homerun_high):
                    homerun_ascii ()
                    base_calculation = shifting_bases (bases, bat_queue[batter], base_pos)
                    bases = base_calculation[0]                   
                    home_score += base_calculation[1] 

            else:  # batter misses ball
                print ("-----------------MISSSED BAT----------------")
                outs = outs + 1  # adds one to out

            if (outs == 3):  # every 3 outs is one inning
                strike_out ()
                inning = inning + 1
                outs = 0

            print (f"\nOuts: {outs}\nInnings: {inning}\nRuns: {home_score}" )  # running stats

        bat_queue.append (bat_queue[batter])  # add first batter to back of queue
        bat_queue.pop (batter)  # remove the old first batter (who missed or hit)
    return home_score, visting_score #returns both times scores


 #function to shift player in bases
def shifting_bases (bases, batter_up, base_position):

    moved_bases = ['', '', ''] #empty list of bases to change
    score = 0 #score variable for when
    moved_bases = bases
    runs = [] #empty list used for score

    for i in range (0, base_position):
        if (i == 0):
            moved_bases.insert (0, batter_up) #gets base pos of batter

        else:
            moved_bases.insert (0, "") #if no batter, make the base empty

        if (moved_bases[3]) != '': #moves player when homeplate is not empty
            runs.append (bases[3])

    for run in runs: #adds a score when homeplate is not empty
        if (run != ''):
            score = score + 1

    return [moved_bases[0:3], score] #returns all base values


# End of game results display
def gameover ():

    home_score, visting_score = play_game() #calls both teams scores from game function

    if (home_score > visting_score):  # if home team wins
        print(
            f"The game ended in {home_score} - {visting_score}. The winner is the HOME TEAM"
        )

    elif (home_score < visting_score):  # if visting team wins
        print(
            f"The game ended in {visting_score} - {home_score}. The winner is the AWAY TEAM"
        )

    else:  # if its a tie
        print(f"The game ended in {visting_score} - {home_score}. It was a DRAW")

gameover()