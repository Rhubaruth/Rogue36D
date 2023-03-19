from player import Player


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    player1 = Player("TheChosenOne", 20, 5)
    player2 = Player("TheDestroyer", 6, 6, attack_power=6, defense_power=12)

    # Game Loop
    while player1.is_alive() and player2.is_alive():
        player1.attack(player2)
        if not player2.is_alive():
            print(f"\n{player1.name} wins!")
            break

        player2.attack(player1)
        if not player1.is_alive():
            print(f"\n{player2.name} wins!")
            break
