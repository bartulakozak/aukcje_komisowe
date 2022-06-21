import sqlite3
from tabulate import tabulate

class Car():

    def __init__(self):
        self.connect()
        self.cur.execute("""CREATE TABLE IF NOT EXISTS samochody(
            id INTEGER PRIMARY KEY,
            marka text,
            model text,
            paliwo text,
            przebieg INTEGER,
            cena INTEGER,
            user_id  INTEGER,
            FOREIGN KEY(user_id) REFERENCES user(id)
            )""")
        self.close()
        
    
    def connect(self):
        # łączenie się z bazą danych
        self.con = sqlite3.connect("komis.db")
        self.cur = self.con.cursor()

    def close(self):
        # zamykanie połączenia z bazą
        self.con.close()

    def dodaj(self):
        # dodanie samochodu do bazy

        marka = str(input("Podaj markę: "))

        try:
            model = str(input("Podaj model: "))
            paliwo = str(input("Podaj rodzaj paliwa: "))
            przebieg = int(input("Podaj przebieg: "))
            cena = int(input("Podaj cenę: "))

        except Exception:
            print("Niewłaściwe dane")
            self.close()
            return 1
            
        self.connect()
        self.cur.execute(f"""INSERT INTO samochody(marka,model,paliwo, przebieg, cena) VALUES(
                                                                    '{marka}','{model}','{paliwo}', {przebieg}, {cena})""")


        self.con.commit()
        self.close()
        print("Pomyslnie dodano aukcje...")

    def usun(self):
        # usuwanie danych z bazy

        self.pokaz()
        print("\n--- PODAJ ID SAMOCHODU DO USUNIĘCIA ---")
        try:
            id_do_usuniecia = int(input("ID: "))
        except ValueError:
            print("Podaj liczbę")
            return 1
            
        self.connect()

        # sprawdzenie czy aukcja o takim id znajduje się w bazie
        self.cur.execute(f"""SELECT * FROM samochody WHERE id={id_do_usuniecia}""")

        if self.cur.fetchall():
            self.cur.execute(f"""DELETE FROM samochody WHERE id={id_do_usuniecia}""")
            self.con.commit()
            self.close()
            print(f"""SAMOCHOD O ID {id_do_usuniecia} został usunięty""")
        else:
            print("Aukcja o takim ID nie istnieje")
            return 1


    def pokaz(self):
        # wyświetlanie danych z bazy

        self.connect()
        
        self.cur.execute("""SELECT * FROM samochody""")
        rows = self.cur.fetchall()
        header = ['ID','MARKA','MODEL','PALIWO','PRZEBIEG','CENA','OSTATNI LICYTUJACY']
        print(tabulate(rows,header,tablefmt="grid"))


        self.close()


    def licytuj(self):
        self.pokaz()
        print("\n --- Podaj ID licytowanego pojazdu i nową cenę --- ")
        try:
            id_licytacji = int(input("ID POJAZDU: "))
            cena_licyt = int(input("PODAJ CENE: "))
        except ValueError:
            print("NIEPRAWIDŁOWY FORMAT DANYCH")
            return 1
        
        # wyszukiwanie w bazie samochodu o podanym id i sprawdzanie ceny -> aktualizacja ceny
        self.connect()

        # sprawdzenie czy aukcja o podanym id znajduje się w bazie
        self.cur.execute(f"""SELECT id FROM samochody WHERE id={id_licytacji}""")
        if self.cur.fetchall()[0][0] == id_licytacji:

            self.cur.execute(f"""SELECT cena FROM samochody WHERE id={id_licytacji}""")
            cena_do_sprawdzenia = self.cur.fetchone()
            
            if cena_do_sprawdzenia[0] < cena_licyt:
                self.cur.execute(f"""UPDATE samochody set cena = {cena_licyt} WHERE id={id_licytacji}""")
                self.con.commit()
                self.close()
            else:
                print("Podana cena jest mniejsza lub równa aktualnej")
                self.close()
        else:
            print("Aukcja o podanym id nie istnieje")
            return 1


class User(Car):
    def __init__(self):
        self.connect()
        self.cur.execute("""CREATE TABLE IF NOT EXISTS user(
            id INTEGER PRIMARY KEY,
            login text UNIQUE,
            password text
            )""")
        self.close()

        # dodanie usera do bazy
    def dodaj(self):

        login = str(input("Podaj login: "))
        password = str(input("Podaj haslo: "))
        self.connect()
        self.cur.execute(f"""INSERT INTO user(login, password) VALUES('{login}', '{password}')""")
        self.con.commit()
        print("Dodano pomyslnie")
        self.close()

    # sprawdzanie czy w bazie jest juz taki uzytkownik
    def sprawdz(self,login,password):

        query = 'SELECT * FROM user WHERE login = ? AND password = ?'
        self.connect()
        self.cur.execute(query, (login, password))
        result = self.cur.fetchone()
        self.con.commit()
        #print('Sprawdzam w bazie ', result)
        return result
        self.close()

    def logwanie(self):
        while True:
            login = str(input("Login: "))
            password = str(input("Haslo: "))
            if self.sprawdz(login,password):
                print("Logowanie...")
                break
            else:
                print("Cos poszlo nie tak...")
                print("Sprobuj ponownie....")
                continue








