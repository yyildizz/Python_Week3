"""This program  takes an input of different words with hyphen (-) in between them and
sorts the words in alphabetical order, adds hyphen icon (-) between them,
gives the output of the sorted words"""

#Function Definitions
def input_function(str_in):
    my_list = str_in.split("-")
    print("\n","Original Order :",str_in)

    my_list.sort()

    joined_again = ('-'.join(x for x in my_list))
    print(" Sorted   Order :", joined_again)


#Program starts from here

input_function(input("Write words separated with - : "))