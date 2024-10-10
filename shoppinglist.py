# Dies ist ein Programm das als Shopping Liste funktionieren soll
import sqlite3

# Verbindung zur SQLite-Datenbank herstellen (Datei wird erstellt, falls nicht vorhanden)
conn = sqlite3.connect('shoppinglist.db')

# Cursor-Objekt zum Ausführen von SQL-Befehlen
cursor = conn.cursor()

# Erstellung der Datenbank
cursor.execute('''
    CREATE TABLE IF NOT EXISTS shoppinglist(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               item VARCHAR(64) NOT NULL,
               amount INTEGER NOT NULL,
               price FLOAT NOT NULL
               )
''')

# Funktion um ein Item der Einkaufsliste hinzuzufügen
def add_item():
    artikel = input("Bitte gib ein Welcher Artikel, zur Einkaufsliste hinzugefügt werden soll.")
    preis = int(input(f"Wie oft möchten Sie {artikel} kaufen?\n"))
    anzahl = float(input(f"Wie teuer ist {artikel}? Bitte mit mindestens einer Nachkomma Stelle angeben."))
    if artikel:
        cursor.execute('''
            INSERT INTO shoppinglist (item, amount, price)
            VALUES (?, ?, ?)
        ''', (artikel, preis, anzahl))
        conn.commit()
        print(f"Der Artikel {artikel} wurde {anzahl} mal der Einkaufsliste mit dem Preis {preis}€ hinzugefügt.")
    else:
        print("Die Eingabe war ungültig.")

# Funktion um die EInkaufsliste anzuzeigen
def show_shoppinglist():
    id = 0
    print("Deine Einkaufsliste:")
    print("Nummer | Artikel | Anzahl | Preis")
    cursor.execute('SELECT * FROM shoppinglist')
    shoppinglist = cursor.fetchall()
    if len(shoppinglist) != 0:
        for i in shoppinglist:
            print(f"Nummer: {shoppinglist[id][0]}, Artikel: {shoppinglist[id][1]}, Anzahl: {shoppinglist[id][2]}, Preis: {shoppinglist[id][3]}")
            id = id + 1
    else:
        print("Deine Einkaufliste ist leer")

def update_shoppinglist():
    id = input("Welchen Artikel möchten Sie verändern? Bitte geben Sie die Nummer in der Einkauflist an.\n")
    cursor.execute('SELECT * FROM shoppinglist WHERE id = ?', (id))
    print("Sie können den")
    print("1. Namen")
    print("2. Menge")
    print("3. Preis")
    print("4. Alles ändern")
    print("verändern.")
    print("-----")
    choice = input("Was möchten Sie gerne verändern?\n")

    if choice == "1":
        artikelname = input("Wie soll der Artikel nun heißen?\n")
        cursor.execute('''
            UPDATE shoppinglist SET item = ? WHERE id = ?
        ''', (name, id))
        conn.commit()
        print(f"Sie haben Erfolgreich den Artikel mit der Nummer {id} umbenannt in {artikelname}.")

    elif choice == "2":
        anzahl = int(input("Wie viel wollen Sie nun kaufen?\n"))
        cursor.execute('''
            UPDATE shoppinglist SET amount = ? WHERE id = ?
            ''', (anzahl, id))
        conn.commit()
        print(f"Sie haben Erfolgreich die Menge vom Artikel mit der Nummer {id} geändert in {anzahl}.")
        
    elif choice == "3":
        preis = float(input("Wie hoch ist der neue Preis?\n"))
        cursor.execute('''
            UPDATE shoppinglist SET price = ? WHERE id = ?
        ''', (preis, id))
        conn.commit()
        print(f"Sie haben Erfolgreich den Preis vom Artikel mit der Nummer {id} geändert in {preis}€.")

    elif choice == "4":
        artikelname = input("Wie soll der Artikel nun heißen?\n")
        preis = float(input("Wie hoch ist der neue Preis?\n"))
        cursor.execute('''
            UPDATE shoppinglist SET item = ?, amount = ?, price = ? WHERE id = ?
        ''', (artikelname, anzahl, preis, id))
        conn.commit()

    else:
        print("Bitte wählen Sie nur zwischen 1, 2, 3 oder 4 aus.")

def delete_item_shoppinglist():
    artikelname = input("Welchen Artikel möchten Sie von ihrer Einkaufsliste löschen? Bitte geben Sie den Namen an.\n")
    cursor.execute('''
    DELETE FROM students WHERE name = ?
    ''', (artikelname)
    )
    conn.commit()
    print(f"Student mit der ID: {artikelname} wurde entfernt.")

# Main Function
def main():
    while 1 == 1:
        print("\n----- Einkaufsliste -----")
        print("1. Artikel zur Einkaufsliste hinzufügen")
        print("2. Einkaufsliste anzeigen")
        print("3. Einen Artikel aktualisieren")
        print("4. Einen Artikel von der Einkaufsliste löschen")
        print("5. Programm beenden")
        print("-----")
        choice = input("Bitte wähle aus was du machen möchtest: ")

        if choice == "1":
            add_item()

        elif choice == "2":
            show_shoppinglist()

        elif choice == "3":
            update_shoppinglist()

        elif choice == "4":
            delete_item_shoppinglist()

        elif choice == "5":
            print("Programm wird beendet! Auf Wiedersehen.")
            break

        else:
            print("Ungültige Auswahl. Bitte wähle 1, 2, 3, 4 oder 5")

if __name__ == "__main__":
    main()