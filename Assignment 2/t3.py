from t2 import getUnique
def get_unique_dict():
    '''creates a dictionary of all unique questions and answers'''
    text = open("QA_Dictionary.txt", "w")
    pairs = getUnique()
    this_dict = {}
    for elem in pairs:
        try:
            this_dict[elem[0]].append(elem[1])
        except KeyError:
            this_dict[elem[0]] = [elem[1]]
    text.write(str(this_dict))
    text.close()
    return this_dict



