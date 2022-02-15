"""Restaurant rating lister."""


# put your code here

#declare a blank dictionary


#either use sys.argv or open(filename)
import re


def restorant_rating(filename):
    
    working_file = open(filename)

    #for each line in the file:
        #rstrip the line
        #separate them out into usable pieces of information by "splitting" with character ":"
        #insert the pair into a dictionary with the two pieces of information
    restorant_rating = {}

    for line in working_file:
        line = line.rstrip()
        res_info = line.split(":")
        name = res_info[0]
        rating = res_info[1]
        restorant_rating[name] = rating
    
    return restorant_rating


def rating_ordered(restorant_ratings):
    
    #declare blank list
    rest_names = []

    
    for restorant in restorant_ratings.keys():
        #append the list with each rest name
        rest_names.append(restorant)
    
    #sort this list
    rest_names.sort()

    #for each item in restaurant list, retrieve the corresponding value in the dictionary to print the rating
    for restorant in rest_names:
        print(f"{restorant} is rated at {restorant_ratings[restorant]}")







