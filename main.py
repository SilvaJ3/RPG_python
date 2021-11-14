# import
import random
import sys

# Stats joueurs

health_player = 50
potion = 3 # permet de récupérer random.randint(15,50) + fait passer un tour
inaction = False

# Stats Boss

health_boss = 50


while health_player > 0 or health_boss > 0:
    if inaction:
        print("Vous passez votre tour")
        inaction = False
    else:
        action = input("Souhaitez-vous attaquer (1) ou utilisez une potion (2) ? ")

        if action == "1" or action == "2":
            if action == "1": # Attaque
                degat = random.randint(5, 10)
                print(f"Vous avez infligé {degat} de dégâts ! ⚔️")
                health_boss -= degat
                if health_boss <= 0:
                    print("Tu as gagné")
                    print("Fin du jeu")
                    sys.exit()
            elif action == "2": # Potion
                if potion > 0:
                    soin = random.randint(15,50)
                    potion -= 1
                    health_player += soin
                    print(f"Vous récupérez {soin} points de vie ❤️ ({potion} 🧪 restantes)")
                    inaction = True
                else:
                    print("Le joueur ne dispose plus d'aucune potion")
                    continue

    degat_boss = random.randint(5,15)
    health_player -= degat_boss
    print(f"L'ennemi vous a infligé {degat_boss} de dégats ! ⚔️")
    if health_player <= 0:
        print("La partie est terminée")
        sys.exit()
    else:
        print(f"Il vous reste {health_player} points de vie.")
        print(f"Il reste {health_boss} points de vie à l'ennemi.")

    print("-" * 50)