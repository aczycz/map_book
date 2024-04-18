users: list[dict] = [
    {"name": "Dawid", "surname": "Bałuka", "posts": 6000},
    {"name": "Kewin", "surname": "Czajkowski", "posts": 6002},
    {"name": "Kamil", "surname": "Gil", "posts": 1_000_000},
    {"name": "Daniel", "surname": "Blaszczyk", "posts": 6}
]

for user in users:
    print(f"Twoj znajomy {user["name"]} opublikowal: {user["posts"]}")





