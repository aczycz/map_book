users: list[dict] = [
    {"name": "Dawid", "surname": "Bałuka", "posts": 6000},
    {"name": "Kewin", "surname": "Czajkowski", "posts": 6002},
    {"name": "Kamil", "surname": "Gil", "posts": 1_000_000},
    {"name": "Daniel", "surname": "Blaszczyk", "posts": 6}

]


def show_users(user_list: list[dict]) -> None:
    for user in user_list:
        print(f"Twoj znajomy {user["name"]} opublikowal: {user["posts"]}")

show_users(users)