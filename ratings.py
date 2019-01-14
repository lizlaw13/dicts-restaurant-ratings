def restaurant_ratings(filename):
    file = open(filename)
    ratings = {}
    for line in file:
        line = line.rstrip()
        restaurant_info = line.split(':')
        for rating in restaurant_info:
            ratings[restaurant_info[0]] = restaurant_info[1]
           
    new_restaurant = input('Please add a new restaurant:')
    new_rating = input('Please add a rating for the restaurant:')
    if int(new_rating) <= 0 or int(new_rating) >= 5:
        print('Please provide a valid number for ratings(1-5)')
        new_rating = input('Please add a rating for the restaurant again:')



    else:
        ratings[new_restaurant] = new_rating

        sorted_restaurant_ratings = sorted(ratings.items())
        for restaurant, restaurant_ratings in sorted_restaurant_ratings:
            print(f'{restaurant} is rated at {restaurant_ratings}.')



restaurant_ratings('scores.txt')