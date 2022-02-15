"""Restaurant rating lister."""
import random

def create_rating_dictionary(filename):
    """reads a file of restaurant ratings and returns a dictionary with the info inside"""

    rating_dictionary = {}

    for line in open(filename):
        line = line.rstrip()
        res_info = line.split(":")

        rating_dictionary[res_info[0]] = res_info[1]
    
    return rating_dictionary


def print_ratings(rating_dict):

    """takes in a dictionary of restaurant ratings and prints them in alphabetical order by restaurant"""

    #for each item in restaurant list, retrieve the corresponding value in the dictionary to print the rating
    for restorant in sorted(rating_dict.keys()):
        print(f"{restorant} is rated at {rating_dict[restorant]}")


def new_restorant(restorant_ratings):
    while True:
        answer = input("Do you want to add a restorant review? Y/N ")
        if answer.upper() == "Y":
            restorant_name = input("What is the name of the restorant? ")
            restorant_rating = input("What is the rating? Number out of 5 ")
            restorant_ratings[restorant_name] = restorant_rating
        else:
            break
    return restorant_ratings

def change_random_rating(restorant_ratings):
    """takes in current ratings, prompts user to update a random restaurant's rating, returns updated rating"""
    answer = input("Do you want to change a random restorant's rating? Press Y for Yes. ")

    if answer.upper() == "Y":
        #convert restorant_ratings keys into a list
        names_list = list(restorant_ratings.keys())
        
        #random choice from the list
        random_rest = random.choice(names_list)

        #print the current rating from the dictionary of that item
        print(f"The current rating of {random_rest} is {restorant_ratings[random_rest]}.")

        #ask for a new rating
        new_rating = input("The new rating please ")
        
        #update the dictionary
        restorant_ratings[random_rest] = new_rating
    
    return restorant_ratings


def custom_restaurant_rating_change(restorant_ratings):
    answer = input("Do you want to change a specific restorant's rating? Press Y for Yes. ")

    if answer.upper() == "Y":    
        rest_name = input("Name of the restaurant you want to change? ")
        #check if the name they provided is in the dict already.
        if rest_name in restorant_ratings:
            #ask for the new rating and update dictionary
            rest_rating = input("What is the new rating? ")
        else:

            print("We don't have this restaurant in our list.")
            answer = input("Do you want to add a rating for this restaurant? Y/N ")
            if answer.upper() != "Y":
                return restorant_ratings
            else:
                rest_rating = input("What is the rating? ")

        restorant_ratings[rest_name] = rest_rating
        

    return restorant_ratings

#creates a usable dictionary from the original file
current_ratings_dict = create_rating_dictionary('scores.txt')

#sorts and prints the ratings
print_ratings(current_ratings_dict)

#reassigns current_ratings_dict to whatever results from the prompts to add new restaurants
#current_ratings_dict = new_restorant(current_ratings_dict)

#sorts prints again with the new restaurants added
#print_ratings(current_ratings_dict)

#prompts user to change a random restaurant's rating
#current_ratings_dict = change_random_rating(current_ratings_dict)

#sorts prints again with the restaurant's rating updated
#print_ratings(current_ratings_dict)

#prompts user to change a selected restaurant's rating
current_ratings_dict = custom_restaurant_rating_change(current_ratings_dict)

##sorts and prints the ratings
print_ratings(current_ratings_dict)
