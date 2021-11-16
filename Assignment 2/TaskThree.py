from TaskTwo import getUnique
def get_unique_dict():
    pairs = getUnique()
    this_dict = {}
    for elem in pairs:
        try:
            this_dict[elem[0]].append(elem[1])
        except KeyError:
            this_dict[elem[0]] = [elem[1]]

    return this_dict



