from dbase import Car
from dbase import User
import sys

def main():
    car = Car()
    user = User()
    run = True





    while run:
        print()
        print('======Menu główne======')
        print("1. Zaloguj sie")
        print("2. Zarejestruj się")
        print()

        try:
            menu = int(input("1-2: "))
            if menu not in range(1, 3):
                print("\nPodaj poprawny number")

        except ValueError:
            print("\nPodaj poprawny number")

        if menu == 1:
            user.logwanie()

        elif menu == 2:
            user.dodaj()
            continue



        while run:
            print("\n -- PORTAL AUKCYJNY -- ")
            print("1. Pokaż wszystkie aukcje")
            print("2. Dodaj aukcje")
            print("3. Usuń aukcje")
            print("4. Licytuj")
            print("5. Zakończ")

            try:
                wybor = int(input("1-5: "))
                if wybor not in range(1, 6):
                    print("\nPodaj poprawny number")
                    continue
            except ValueError:
                print("\nPodaj poprawny number")
                continue

            if wybor == 6:
                run = False

            elif wybor == 1:
                car.pokaz()

            elif wybor == 2:
                dodawanie = car.dodaj()
                if dodawanie == 1:
                    continue

            elif wybor == 3:
                usuwanie = car.usun()
                if usuwanie == 1:
                    continue

            elif wybor == 4:
                licytacja = car.licytuj()
                if licytacja == 1:
                    continue
            elif wybor == 5:
                #run = False
                sys.exit(0)




if __name__ == "__main__":
    main()