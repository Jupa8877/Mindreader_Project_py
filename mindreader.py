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
    double_correct_count = 0
    single_correct_count = 0
    for code in player_code:
        if code in computer_code:
            if code == computer_code[count]:
                double_correct_count += 1
            else:
                single_correct_count += 1
        else:
                        





def game():
    computer_code = code_gen()
    player_code = code_input()
    print("Computer: " + str(computer_code))
    print("Player: " + str(player_code))


if __name__ == "__main__":
    game()
