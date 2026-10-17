from video_game import VideoGame
from game_manager import GameManager

manager = GameManager()
manager.load_games()

while True:
    print("Video Game Collection Manager")
    print("1. Add game")
    print("2. View games")
    print("3. Search game")
    print("4. Remove game")
    print("5. Mark game as finished")
    print("6. Rate game")
    print("7. View games by platform")
    print("8. View finished games")
    print("9. View unfinished games")
    print("10. Sort games by name")
    print("11. Exit")
    choice = input("Choice: ")

    if choice == "1":
        name = input("Enter game name: ").strip()
        if not name:
            print("Invalid, can't be empty.\n")
            continue

        try:
            release_year = int(input("Enter release year: ").strip())
        except ValueError:
            print("Invalid year.\n")
            continue

        developer = input("Enter developer: ").strip()
        if not developer:
            print("Invalid, can't be empty.\n")
            continue

        platform = input("Enter platform: ").strip()
        if not platform:
            print("Invalid, can't be empty.\n")
            continue

        game = VideoGame(name, release_year, developer, platform)

        if manager.add_game(game):
            manager.save_games()
            print("Game added successfully.\n")
        else:
            print("Game is already in the collection.\n")

    elif choice == "2":
        games = manager.view_all_games()

        if not games:
            print("Games not found.\n")
        else:
            for game in games:
                print(game)
            print()

    elif choice == "3":
        name = input("Enter name: ").strip()
        if not name:
            print("Invalid, can't be empty.\n")
            continue

        game = manager.search_game(name)

        if game is None:
            print("Game not found.\n")
        else:
            print(game)
            print()

    elif choice == "4":
        name = input("Enter name: ").strip()
        if not name:
            print("Invalid, can't be empty.\n")
            continue

        game = manager.search_game(name)

        if game is None:
            print("Game not found.\n")

        else:
            confirmation = input("Are you sure?(y/n): ").strip().lower()

            if confirmation == "y" or confirmation == "yes":
                manager.remove_game(name)
                manager.save_games()
                print("Game removed successfully.\n")

            elif confirmation == "n" or confirmation == "no":
                print("Removal canceled.\n")

            else:
                print("Invalid choice.\n")

    elif choice == "5":
        name = input("Enter game name: ").strip()
        if not name:
            print("Invalid, can't be empty.\n")
            continue

        game = manager.search_game(name)

        if game is None:
            print("Game not found.\n")

        elif game.finished:
            print("Game already marked finished.\n")

        else:
            manager.mark_game_finished(name)
            manager.save_games()
            print("Game marked finished.\n")

    elif choice == "6":
        name = input("Enter game name: ").strip()
        if not name:
            print("Invalid, can't be empty.\n")
            continue

        game = manager.search_game(name)

        if game is None:
            print("Game not found.\n")

        else:
            try:
                rating = int(input("Enter rating 1-10: "))
            except ValueError:
                print("Invalid rating.\n")
                continue

            if manager.rate_game(name, rating):
                manager.save_games()
                print("Rating added.\n")
            else:
                print("Invalid rating.\n")

    elif choice == "7":
        platform = input("Enter platform name: ").strip()
        if not platform:
            print("Invalid, can't be empty.\n")
            continue
        
        games = manager.get_games_by_platform(platform)

        if not games:
            print("There are no games found.\n")
        else:
            for game in games:
                print(game)
            print()

    elif choice == "8":
        games = manager.get_finished_games()

        if not games:
            print("There are no games found.\n")
        else:
            for game in games:
                print(game)
            print()

    elif choice == "9":
        games = manager.get_unfinished_games()

        if not games:
            print("There are no games found.\n")
        else:
            for game in games:
                print(game)
            print()

    elif choice == "10":
        games = manager.get_games_sorted_by_name()

        if not games:
            print("There are no games found.\n")
        else:   
            for game in games:
                print(game)
            print()

    elif choice == "11":
        print("Exiting...")
        break

    else:
        print("Invalid choice.\n")