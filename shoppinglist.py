def add_item():
    print(f"Bitte gib den Artikel ein, der zur Einkaufsliste hinzugefügt werden soll")
    item=input("")
    print(f"Der Artikel {item} wurde der Einkaufsliste hinzugefügt")

def show_shoppinglist():
    if shoppinglist:
        print(f"Deine Einkaufsliste:")
        for item in shoppinglist:
            print(f"{item}")
            else print(f"Deine Einkaufsliste ist leer.")