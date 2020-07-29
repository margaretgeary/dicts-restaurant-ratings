"""Restaurant rating lister."""

def restaurant_ratings(ratings_file):
    """Sort alphabetically a list of restaurants and ratings, with user option to add ratings
    
    Arguments:
    ratings_file (.txt file): text file containing restaurants and corresponding ratings
    
    Returns:
    (dict) Dictionary of restaurants and corresponding ratings"""

    restaurant_dict = {}
    restaurant_file = open(ratings_file)

    for line in restaurant_file:
        rating_line = line.rstrip().split(":")
        restaurant = rating_line[0]
        rating = rating_line[1]

        restaurant_dict[restaurant] = rating

    print("Would you like to add a restaurant and rating?")
    wants_to_add = input("Please enter Y or N:  ")

    if wants_to_add in ("Y", "y"):
        new_restaurant = input("Please add a restaurant: ")
        new_rating = input("How would you rate that restaurant on a scale from 1 to 5: ")
    
        restaurant_dict[new_restaurant] = new_rating

    for restaurant in sorted(restaurant_dict):
        print(f'{restaurant}: {restaurant_dict[restaurant]}')

    return restaurant_dict
    
restaurant_ratings("scores.txt")