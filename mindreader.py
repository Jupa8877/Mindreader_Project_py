import random

COLOR = ["G", "W", "R", "B", "Y", "S"]

TRY = 10

CODE_LENGTH = 4


def code_gen():
    code = []
    for _ in range(CODE_LENGTH):
        color = random.choice(COLOR)
        code += color
    return code


def code_chk_letters(playercode):
    while not all(code in COLOR for code in playercode):
        playerschoice = input(
            "\nYou must choose 4 letters from only "
            + str(COLOR)
            + ".\nExamples: gggg, GRSW, GYsi\n"
        )
        playercode = list(playerschoice.upper())
        if all(code in COLOR for code in playercode):
            return playercode


def code_chk_lenth(playercode):
    while len(playercode) > CODE_LENGTH or len(playercode) < CODE_LENGTH:
        playerschoice = input(
            "\nYou must choose 4 letters from only "
            + str(COLOR)
            + ".\nExamples: gggg, GRSW, GYsi\n Your code has more or less than 4\n"
        )
        playercode = list(playerschoice.upper())
        if len(playercode) == CODE_LENGTH:
            return playercode
            break


def code_input():
    playercode = []
    playerschoice = input(
        "\nPlease guess what 4 letters by choosing 4 letters from "
        + str(COLOR)
        + ".\nExamples: gggg, GRSW, GYsi\n"
    )
    playercode = list(playerschoice.upper())

    if len(playercode) > CODE_LENGTH or len(playercode) < CODE_LENGTH:
        playercode = code_chk_lenth(playercode)
        playercode = code_chk_letters(playercode)
        return playercode
    if all(code in COLOR for code in playercode):
        return playercode

    else:
        playercode = code_chk_letters(playercode)
        return playercode


def comparer(computer_code, player_code):
    
    
    correct_ltr_pst_count = 0 # Correct letter in a correct position counter
    correct_letter_count = 0 # Correct letter counter  
    # Setting options to win the game.

    if player_code == computer_code:
        print("Congratulations!! You found out what the code is!! \nComputer: " + str(computer_code) + "\nPlayer: " + str(player_code))
    
    else:
        
        for i in range(CODE_LENGTH):
            if player_code[i] in computer_code:
                if player_code[i] == computer_code[i]:
                        correct_ltr_pst_count += 1
                else:
                    correct_letter_count += 1

        
        print("You have " + str(correct_ltr_pst_count) + " letters in right position(s)")
        print("Also you have " + str(correct_letter_count) + " letters in different position(s)")
        

def game():
    computer_code = code_gen()
    player_code = code_input()
    turns = TRY
    print("Computer: " + str(computer_code))
    print("Player: " + str(player_code))

    for i in range(TRY):
        turns -= 1
        comparer(computer_code, player_code)
        print("You have " + str(turns) + " more turns.")
        player_code = code_input()


if __name__ == "__main__":
    game()
