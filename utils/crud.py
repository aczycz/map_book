        def show_users(user_list: list[dict]) -> None:
            for user in user_list:
                print(f"Twoj znajomy {user["name"]} opublikowal: {user["posts"]}")


        def add_new_user(users: list) -> None:
            new_name: str = input("Enter your name: ")
            new_surname: str = input("Enter your surname: ")
            new_posts: int = int(input("Enter your posts: "))
            new_user: dict = {"name": new_name, "surname": new_surname, "posts": new_posts}
            users.append(new_user)

        def search_user(users: list) -> None:
            kogo_szukasz = input("kogo szukasz: ")
            for user in users:
                 if user["name"]==kogo_szukasz:
                     print(user)

        def remove_user(users)-> None:
            kogo_szukasz=input("kogo szukasz: ")
            for user in users:
                if user["name"]==kogo_szukasz:
                   users.remove(user)

        def update_user(users)-> None:
        kogo_szukasz=input("kogo szukasz: ")
        for user in users:
            if user["name"]==kogo_szukasz:
                user["name"]=input("Podaj nowe imie: ")
                user["surname"]=input("podaj nowe nazwisko: ")
                user["posts"]=input("podaj liczbe postow: ")