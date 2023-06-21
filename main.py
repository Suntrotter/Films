from funcs import *

films = [
    {"author": "John Silver",
     "rating": "100",
     "title": "Walking on the Moon",
     "id": "adventure"
     },
    {"author": "Mary Golden",
     "rating": "80",
     "title": "Fields of Love",
     "id": "love drama"
     },
    {"author": "Steven Spielberg",
     "rating": "70",
     "title": "Your Inner Psycho",
     "id": "horror"
     },
    {"author": "Jack Mittens",
     "rating": "60",
     "title": "Journey with the Wolves",
     "id": "mystic thriller"
     },
    {"author": "Larry Smith",
     "rating": "50",
     "title": "Dangerous City",
     "id": "action"
     }
]


def main():
    choice = input("Hello, user! 1 for menu, 2 for film by name, 3 for sorted list: ")
    if choice == "1":
        menu(films)
    elif choice == "2":
        film_by_name(films)
    elif choice == "3":
        sorted_list(films)
    else:
        print("Wrong choice, buddy")
        main()


if __name__ == "__main__":
    main()




