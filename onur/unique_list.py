"""This program filters all the unique(unrepeated) elements of a given list."""

#Function definitions
def unique_list(list_in):
    uniq_ls = []
    for i in list_in:
        if i not in uniq_ls:
            uniq_ls.append(i)
    return uniq_ls


#Program starts from here

print("Uniqu List : ",unique_list([1,2,3,4,3,3,5,9,8,7,5,7]))


