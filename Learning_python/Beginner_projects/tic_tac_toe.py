GAME_TABLE = "- - -\n- - -\n- - -"

the_turn = 1


#def draw_game_table():x
    #print(GAME_TABLE)


def user_input():
    global the_turn
    global GAME_TABLE
    the_turn += 1
    if the_turn % 2 == 0:
        player_input = int(input("Mängija 1 kirjuta oma valik (1-9): ")) * 2
        GAME_TABLE = GAME_TABLE[:player_input] + "x" + GAME_TABLE[player_input + 1:]

    if the_turn % 2 == 1:
        player_input = int(input("Mängija 2 kirjuta oma valik (1-9): ")) * 2
        GAME_TABLE = GAME_TABLE[:player_input] + "o" + GAME_TABLE[player_input + 1:]


draw_game_table()

working = True
while working:
    try:
        user_input()
        draw_game_table()
    except ValueError:
        print("Invalid input")
        draw_game_table()
        the_turn -= 1
