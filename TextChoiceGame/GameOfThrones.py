
import pygame

class GameOfThrones:

    #Dict which holds the possible next states
    all_possible_moves = {
        "Start" : ["Go to Winterfell", "Go to Casterly Rock", "Go to Iron Island", "Go to North of the Wall", "Go to Dragon Stone"],
        "Go to Winterfell" : ["Kill Jon Snow", "Pick up the Sword", "Go to Casterly Rock", "Play with Direwolves","Go Back"],
        "Go to Casterly Rock" : ["Pick up the Wildfire", "Go to Dragon Stone", "Eat a lamb", "Go to River Run", "Go Back"],
        "Go to River Run" : ["Kill Ramsey Bolton", "Pick up the needle", "Sit by the River", "Go to Iron Island", "Go Back"],
        "Go to North of the Wall" : ["Catch a Dragon","Kill the Night King","Go to Kings Landing","Meet the wildlings","Go Back"],
        "Go to Iron Island" : ["Pick up the Cross-Bow","Seek advice from Theon Greyjoy" , "Kill Petyr Baelish", "Go to Kings Landing","Go back"],
        "Go to Kings Landing" : ["Kill Cersei Lannister", "Go to Winterfell","Vist all the museums", "Meet Jamie Lannister","Go Back"],
        "Go to Dragon Stone" : ["Play with Dragons", "Go to North of the Wall",  "Pray for your victory","Pick up the Dragon glass","Go Back"]
    }

    #Dict which the Character to weapon mapping(E.g.: Cersei Lannister can be killed only with a Cross-Bow
    kill_moves_dict = {
        "Kill Cersei Lannister" : "Pick up the Cross-Bow",
        "Kill Jon Snow" : "Pick up the Sword",
        "Kill Ramsey Bolton" : "Pick up the Wildfire",
        "Kill Petyr Baelish" : "Catch a Dragons",
        "Kill the Night King" : "Pick up the Dragon glass"
    }

    # Game begins here. This function is a main function, it calls all other functions
    def start_game(self):

        #Calling function which plays the GOT theme tune in the background
        self.play_got_music()

        option, sel_option, game_finished_flg, options_selected, places_visited, kills_made = "Start", "Start", False, ["Start"], ["Start"], []
        enemy_killed_count, wrong_kill_count, wrong_input_count, num_of_moves, prev = 0, 0, 0, 0, 0

        #calling function to display the background story of the game
        self.disp_background_story()

        player_name = input("Enter your Name : ")
        print("Starting...")
        i = 1
        if self.all_possible_moves.get(option) is not None:
            for nxt_option in self.all_possible_moves.get(option):
                print(str(i) + ". " + nxt_option)
                i += 1

        prev_option = option

        while(~game_finished_flg): #While Winning condition is met or the User decides to Exit
            num_of_moves += 1
            print("Number of moves : " + str(num_of_moves))
            if option == "Go Back":
                #option = prev_option
                option = places_visited.__getitem__(prev)
            else :
                prev_option = option
                sel_option = input("Choose your option(1,2,3,4 or 5) : ")
                option = self.decode_options(sel_option, prev_option)


            # Increment the number of Moves. This will be used in determining the final points earned


            if option is None:
                option = prev_option
                wrong_input_count+= 1
                continue
            elif option is not None and option.startswith('Kill'):

                ##Check whether the required weapon has been collected. Otherwise, take back to the previous step
                #print(options_selected.__contains__(self.kill_moves_dict.get(option) and ~kills_made.__contains__(option)))
                if options_selected.__contains__(self.kill_moves_dict.get(option)) and option not in kills_made:
                    kills_made.append(option)
                    enemy_killed_count += 1

                    print("Awesome you killed an Enemy!!!!!!!!!!!!!!!!!!! Bravo!!!!!")
                    #It is a valid kill, so we will append this option into the list
                    options_selected.append(option)
                    #prev+=1
                    #If the player has killed Cersie and killed 2 or more other enemies, he can be declared a Winner and the game can be brought to an end
                    if kills_made.__contains__("Kill Cersei Lannister") and enemy_killed_count >= 3:
                        ##Mission Accomplished. Won the Game. Break the loop and set the game_finished_flg == True
                        game_finished_flg = True
                        break
                else:
                    #Incorrect kill.
                    wrong_kill_count += 1
                    print(
                        "Error!!! You dont possess the required weapon to perform the Kill. "
                        "\nOr You have already Killed the enemy you just tried to kill. So much hate ain't good :P"
                        "\nYou lose points for this. Taking you back to the previous position.")
                    option = places_visited.__getitem__(prev)
            elif option == 'Go Back':
                #The user has selected to Go Back
                #Setting the previous option as current option and progressing further
                #option = prev_option
                option = places_visited.__getitem__(prev-1)

            else :
                #Selected a valid option but not a Kill option. Appending it to the options_selected list
                options_selected.append(option)
                #prev += 1
            #print("List values ")
            #for str1 in options_selected:
                #print(str1)
            i = 1
            # Checking whether the selected option has other options.
            if self.all_possible_moves.get(option) is not None :
                if places_visited.__getitem__(prev) != option:
                    places_visited.append(option)
                    prev += 1

                for nxt_option in self.all_possible_moves.get(option):
                    print(str(i) + ". " + nxt_option)
                    i += 1
            else:
                #options_selected.append(option)
                go_back_or_no = input("You need to Go Back or End Game. Please decide :(Press 1 to Exit or Any other key to Go Back)")
                #num_of_moves += 1
                if go_back_or_no != "1":
                    option = "Go Back"
                else:
                    # User decided to quit game. Exiting...
                    break

            #Saving the option selected in the List of Selected Options
            #options_selected.append(option)

        #Out of the while loop
        if game_finished_flg :
            #Player has won the Game
            print("Congratulations", player_name ,"!!! You have won the game!!!. See how you performed in comparison to other players")

        else :
            #Player has either quit or lost!
            print("Oh no!!! You Loose. Never mind. You can try again. Check out how other players faired at this game.")

        #Game completed. Calculating score and storing stats to a file and storing the states to another file.
        score = self.calcuate_score(game_finished_flg, num_of_moves, wrong_input_count, wrong_kill_count, enemy_killed_count)
        print("Your score is  : " + str(score))
        #Saving the stats
        self.save_stats_to_file(player_name, game_finished_flg, num_of_moves, wrong_input_count, wrong_kill_count, enemy_killed_count, score)

        #Saving the states through which the player passed.
        self.save_states(player_name, options_selected)

        #Saving all stats in a file in the following format
        #player_name, game_finished_flg, num_of_moves,wrong_input_count, wrong_kill_count,enemy_killed_count


    #This function determines whether the input is in correct format(int).
    # If yes, it tries to determine whether the option selected has further states to go to or no
    # by looking up in the all_possible_moves dict
    # If no, then it returns None and we keep calling this function till a vaild input is made by the user
    def decode_options(self, option, prev_option):

        try:
            int_option = int(option)
        except ValueError:
            print("Invalid entry. Please try again.")
            return None

        if 1 <= int(option) <= 5 :
            print("Option selected " + option)
            list_of_options = self.all_possible_moves.get(prev_option)
            print(list_of_options[int(option) - 1])
            return list_of_options[int(option) - 1]
        else :
            print("Invalid entry. Please try again.")
            return None


    #This function is for playing background music while the user is enjoying the game.
    #Input : None
    #Output : None
    def play_got_music(self):
        #Using the pygame lib to achieve this functionality
        #Playing music in background
        pygame.mixer.init()
        pygame.mixer.music.load("../Resources/games_of_thrones.mp3")
        pygame.mixer.music.play(loops = 10) #Song will be repeated 11 times


    #This function is for calculating the score of the user. We use all the stats captured while playing the game
    #Inputs :
    #   game_finished_flg : True/False
    #   num_of_moves : Total number of moves
    #   wrong_input_count : Count of Incorrect or garbage input values
    #   wrong_kill_count : Count of incorrect kills. E.g.: Trying to kill an enemy without possessing the required weapon
    #   enemy_killed_count : Number of enemies killed during the game
    #Output :
    #   score : The final score of the user
    #All the values passed to this function are from within the code. So, there cannot be a chance of None values
    def calcuate_score(self, game_finished_flg, num_of_moves, wrong_input_count, wrong_kill_count, enemy_killed_count):

        score = 0
        #Score calculation logic:
        #num_of_moves
        if num_of_moves <= 20 :
            score+= 500
        elif 21 <= num_of_moves <= 30 :
            score+= 300
        elif 31 <= num_of_moves <= 40 :
            score+= 200
        else :
            score-=100

         #Wrong Kill count
        if wrong_kill_count == 0 :
            score += 300
        else :
            score -= wrong_kill_count * 100

        #Wrong Input count
        if wrong_input_count == 0 :
            score+= 100
        else :
            score-= wrong_input_count * 20

        #enemy_kill_count
        if enemy_killed_count > 3 :
            score-= (enemy_killed_count - 3) * 100
        elif enemy_killed_count == 3 :
            score+= 500
        else :
            score-= (3 - enemy_killed_count) * 100

        #game_finished_flg
        if game_finished_flg :
            score+=1000
        else :
            score = 0

        return score

    #This function saves the statistics collected during the game in a txt as comma seperated values
    # Inputs :
    #   player_name : Name of the player
    #   game_finished_flg : True/False
    #   num_of_moves : Total number of moves
    #   wrong_input_count : Count of Incorrect or garbage input values
    #   wrong_kill_count : Count of incorrect kills. E.g.: Trying to kill an enemy without possessing the required weapon
    #   enemy_killed_count : Number of enemies killed during the game
    #   score : The final score of the user
    #Output : None
    def save_stats_to_file(self, player_name, game_finished_flg, num_of_moves, wrong_input_count, wrong_kill_count, enemy_killed_count, score):
        f = open("../Statistics/stats.txt", "a")
        f.write(player_name + "," + str(game_finished_flg) + "," + str(num_of_moves) + "," + str(
            wrong_input_count) + "," + str(wrong_kill_count) + "," + str(enemy_killed_count) + "," + str(score) + "\n")


    #This function saves the states which the user has passed through during the game in a txt file as comma seperated values
    # Input :
    #   player_name : Name of the player
    #   options_selected : List of options/states selected by the user in the game
    # Output : None
    def save_states(self, player_name, options_selected):
        f = open("../Statistics/states-passed.txt", "a")
        f.write(player_name)
        for str in options_selected:
            f.write(",")
            f.write(str)
        f.write("\n")

    #This function displays the initial story of the game on the console
    # Input : None
    # Output : None
    def disp_background_story(self):
        print("Welcome to the Game of Thrones!!!")
        print("This is a fun game where the aim is to Win the Iron Throne!")
        print("Winter has come and its waiting for you to jump into the Royal and fierce Battle")
        print("Are you excited to play?")
        print("Let's begin!")

        print(
            "A bit background of the tasks you need to perform in order to Win this game.\nThere are 5 enemies in the game"
            "\n1. Cersei Lannister\n2. Ramsay Bolton\n3. Petyr Baelish\n4. Jon Snow\n5. Night King"
            "\n\nThe following is a list of places which you will visit. few of the places hav a specilaity weapon and a eneny present. Make a note of this."
            "\n1. Winterfell\n2. Casterly Rock\n3. King's Landing\n4. Iron Islands\n5. Dragon Stone\n6. Riverrun\n7. North of the Wall"
            "\n\nThe following weapons will be available to fight your enemies"
            "\n1. Sword\n2. Arya's Needle\n3.Dragons\n4.Wildfire\n5. Dragon glass\n6. Cross Bow\n7. Knife"
            "\n\n\n"
            "Each enemy can be killed with a specific weapon and at a specific place. Below are the details:"
            "\n1. Jon Snow > Sword > Winterfell\n2. Cersei Lannister > Cross Bow > King’s Landing\n3. Ramsay Bolton > Wildfire > Riverrun\n4. Petyr Baelish > Dragons > The Iron Islands"
            "\n5. Night King > Dragon glass > North of the Wall"
            "\nIn order to Win and cherish the Iron Throne, you need to achieve the following tasks as optimally (minimum number of moves) as possible"
            "\n1. Collect weapons and go to places strategically"
            "\n2. You need to kill Cersei Lannister and 2 other enemies with the weapons which are their weaknesses"
            "\n3. You need to complete the task in minimum number of moves"
            "\n4. There are many distractions in the game which may lead to dead-ends. So BEWARE!!!")
        print("Enough of the talk. Let the Game Begin!")




#Creating instance of the GameOfThrones class and starting the game!
got = GameOfThrones()

#This function encapsulates the entire game experience
got.start_game()

##End of Code
