# example solution
dictionary = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
print(dictionary["c"])
print("a" in dictionary)
print("b" not in dictionary)

# EXAMPLE 2
famous_songs = {"Queen": "Bohemian Rhapsody",
                "Bee Gees": "Stayin' Alive",
                "U2": "One",
                "Michael Jackson": "Billie Jean",
                "The Beatles": "Hey Jude",
                "Bob Dylan": "Like A Rolling Stone"}  # 1 and 2
print(len(famous_songs))  # 3
for key in famous_songs.keys():  # 4
    print(key)
print(famous_songs.values())  # 5
for key, value in famous_songs.items():  # 6
    print(key, value)
print(famous_songs.get("Promise of the Real", "That is not a key that appears in the dictionary."))  # 7


#dictionary methods 2 exercises solution
for key, value in {}.fromkeys("bcdfghjklmnpqrstvwxyz", "consonant").items():
    print(key, value)
 
fast_food_items = {"McDonald's": "Big Mac", "Burger King": "Whopper", "Chick-fil-A": "Original Chicken Sandwich"}
print(fast_food_items.pop("McDonald's"))
 
fast_food_items.popitem()
print(fast_food_items)

#exercise 3
internet_celebrities = {"DrDisrespect": "YouTube", "ZLaner": "Facebook", "Ninja": "Mixer"}
another_one = {"shroud": "Twitch"}
internet_celebrities.update(another_one)  # 2
gamers = internet_celebrities.copy()  # 3
internet_celebrities.clear()  # 4
print(internet_celebrities)  # 5
print(gamers)  # 6