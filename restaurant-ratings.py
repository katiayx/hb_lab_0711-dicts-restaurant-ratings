# your code goes here
# Open the file
the_file = open("scores.txt")
# Create an empty dictionary
restaurant_ratings = {}
# Add each line from the file into the dictionary
for line in the_file:
    line = line.rstrip()
    line = line.split(":")
    restaurant = line[0]
    rating = line[1]
    restaurant_ratings[restaurant] = rating
    print "{} is rated at {}".format(restaurant,rating)

new_restaurant = raw_input("What's your favorite restaurant?")
new_rating = int(raw_input("How would you rate it on a scale of 1-5?"))
restaurant_ratings[new_restaurant] = new_rating
# sorted(restaurant_ratings.items())
# print restaurant_ratings.items()


# print sorted(restaurant_ratings)
# for restaurant in sorted(restaurant_ratings):
#     print restaurant, restaurant_ratings[restaurant]

for restaurant, rating in restaurant_ratings.items():
    print sorted(restaurant_ratings.items())

