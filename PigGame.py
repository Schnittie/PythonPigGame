import random
import re

WIN_SCORE = 50


class Player:
    score = 0

    def __init__(self):
        self.score = 0

    def increase_score(self, number):
        self.score += number
        return self.score >= WIN_SCORE


def dice():
    return random.randint(1, 6)


def extract_numbers(txt):
    list_of_numbers = [int(s) for s in txt.split() if s.isdigit()]
    return list_of_numbers[0]


def main():
    inputtext = input("Wie viele Spleieler?")
    numb_players = extract_numbers(inputtext)
    player_list = list()
    x=0
    while x <= numb_players:
        player_list.append(Player)
        x += 1
    win = False
    current_player = 0
    while not win:
        print("spieler " + str(current_player) + " ist dran" + "dein insgesamter score ist " + str(player_list[current_player].score))
        turn_score = 0
        while True:
            player_decision = input("Willst du würfeln, dein turn score ist " + str(turn_score))
            if player_decision == "ja":
                dice_roll = dice()
                if dice_roll == 1:
                    print("doof gelaufen das war ne eins")
                    turn_score = 0
                    break
                else:
                    print("du hast " + str(dice_roll) + "gewürfelt")
                    turn_score += dice_roll
            else:
                print("dein zug ist vorbeit")
                break
        if Player.increase_score(player_list[current_player], turn_score):
            break
        print("spieler "+ str(current_player) + " dein Score ist " + str(player_list[current_player].score) )
        current_player += 1
        if current_player > numb_players:
            current_player = 0

    print("player" + str(current_player) + "hat gewonnen")


if __name__ == "__main__":
    main()
