import sys

from player import Player
from character_base import roll_dice, Attributes

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # player1 = Player("Warrior", Attributes(roll_dice(2) + 6,
    #                                        roll_dice(3), roll_dice(2) + 6, roll_dice(2) + 3, roll_dice(2) + 3))
    # player2 = Player("Rogue", Attributes(roll_dice(2) + 3, roll_dice(2) + 6,
    #                                      roll_dice(2) + 6, roll_dice(3), roll_dice(2) + 3))

    player: Player

    while True:
        print(f"ROGUE 3D6\n"
              f"\nChoose your character:\n"
              f" 1 Warrior\n"
              f" 2 Rogue\n"
              f" 3 Wizard\n"
              f" E exit\n")

        match str(input()).upper():
            case '1':
                print(f"You have chosen Warrior")
                break

            case '2':
                print(f"You have chosen Rogue")
                break

            case '3':
                print(f"You have chosen Wizard")
                break

            case 'E':
                print(f"Exiting")
                sys.exit()

            case _:
                print(f"Wrong input")



    # Game Loop
    # while player1.is_alive() and player2.is_alive():
    #     player1.attack(player2)
    #     if not player2.is_alive():
    #         print(f"\n{player1.name} wins!")
    #         break
    #
    #     player2.attack(player1)
    #     if not player1.is_alive():
    #         print(f"\n{player2.name} wins!")
    #         break
