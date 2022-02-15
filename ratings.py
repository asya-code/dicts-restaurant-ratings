"""Restaurant rating lister."""


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
    #declare blank list
    #rest_names = []
    '''
    for restorant in rating_dict.keys():
        #append the list with each rest name
        rest_names.append(restorant)
    
    #sort this list
    rest_names.sort()
    '''
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


#creates a usable dictionary from the original file
current_ratings_dict = create_rating_dictionary('scores.txt')

#sorts and prints the ratings
print_ratings(current_ratings_dict)

#reassigns current_ratings_dict to whatever results from the prompts to add new restaurants
current_ratings_dict = new_restorant(current_ratings_dict)

#sorts prints again with the new restaurants added
print_ratings(current_ratings_dict)


