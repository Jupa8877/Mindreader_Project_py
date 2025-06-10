Rock Paper Scissors Game
1. Very simple game that you can play by simply comparing values. 
2. There are only 3 choices for the game Rock, Paper and Scissors. 
3. Once you enter your choice, such as rock = 1, paper = 2 and scissors = 3, the code is going to randomly pick a number then compares the game player's choices and computer's choices by if and elif statements. 
4. The if and elif statements determines only the options for the player's win and draw. Other options will be determined plays loses with the else statement.

Mindreader Game
1. Practiced to code a game with multiple functions.
2. I got the idea of this project from https://www.youtube.com/watch?v=sP-gFDreaQ4&t=436s but I didn't see how the person coded it.
3. Tried to devide whole game into each function, such as code_gen(), code_input(), comparer(computer_code, player_code) and game()
4. Added player inputer cheker functions to check length of codes and inputs are from the 6 letters
5. It took longer than my thought because I couldn't find a bug that was in the comparer function as follow. Rubberducking actually helps a lot.

if player_code == computer_code:
        print("Congratulations!! You found out what the code is!! \nComputer: " + str(computer_code) + "\nPlayer: " + str(player_code))
    
    else:
        
        for i in range(CODE_LENGTH):
            if player_code[i] in computer_code:
                if player_code[i] == computer_code[i]: <== the variable i was the variable correct_ltr_pst_count in computer_code
                        correct_ltr_pst_count += 1
                else:
                    correct_letter_count += 1

                    