"""Restaurant rating lister."""

def restaurant_ratings(ratings_file):

    restaurant_dict = {}
    restaurant_file = open(ratings_file)

    for line in restaurant_file:
        rating_line = line.rstrip().split(":")
        restaurant = rating_line[0]
        rating = rating_line[1]

        restaurant_dict[restaurant] = rating

    for restaurant in sorted(restaurant_dict):
        print(f'{restaurant}: {restaurant_dict[restaurant]}')

restaurant_ratings("scores.txt")
