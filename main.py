from models.data import users
from utils.crud import show_users,add_new_user,search_user,remove_user,update_user
from utils.crud_db import show_users, remove_users,update_users, add_new_user_to_table, db_params, get_user_id
if __name__ == "__main__":
    print("Witaj uzytkowniku")

    while True:

        print("Menu:")
        print("0. Zakoncz program")
        print("1. Wyswietl co u znajomych")
        print("2. Dodaj uzytkownika")
        print("3. Znajdz uzytkownika")
        print("4. Usun uzytkownika")
        print("5. Modyfikuj uzytkownika")
        menu_option: str = input("Dokonaj wyboru:")
        if menu_option == "0":
            print("Program konczy prace")
            break
        if menu_option == "1":
            show_users(db_params)
        if menu_option == "2":
            add_new_user_to_table(db_params)
        if menu_option == "3":
            get_user_id(db_params)
        if menu_option == "4":
            remove_users(db_params)
        if menu_option == "5":
            update_users(db_params)





