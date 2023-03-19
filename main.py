from player import Player, roll_dice


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    player1 = Player("Warrior", roll_dice(2)+6, roll_dice(3), roll_dice(2)+6, roll_dice(2)+3, roll_dice(2)+3)
    player2 = Player("Rogue", roll_dice(2)+3, roll_dice(2)+6, roll_dice(2)+6, roll_dice(3), roll_dice(2)+3)

    for p in [player1, player2]:
        print(f"{p.name} \n\
         STR = {p.strength} \n\
         DEX = {p.dexterity} \n\
         CON = {p.constitution} \n\
         INT = {p.intelligence} \n\
         WIS = {p.wisdom} \n\
         ")


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