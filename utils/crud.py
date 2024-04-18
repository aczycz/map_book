def show_users(user_list: list[dict]) -> None:
    for user in user_list:
        print(f"Twoj znajomy {user["name"]} opublikowal: {user["posts"]}")



