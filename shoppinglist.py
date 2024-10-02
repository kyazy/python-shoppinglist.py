def main():
    while True:
        print("-----Einkaufsliste-----")
        print("1. Artikel zur Einkaufsliste hinzufügen")
        print("2. Einkaufsliste anzeigen")
        print("3. Programm beenden")

   choice = input("Bitte wähle 1, 2 oder 3")

if choice == "1":
    add_item()
elif choice == "2":
    show_shoppinglist()
elif choice == "3":
    print("Programm wird beendet! Auf Wiedersehen.")
    break
else:
    print("Ungültige Auswahl.Bitte wähle 1, 2 oder 3.")