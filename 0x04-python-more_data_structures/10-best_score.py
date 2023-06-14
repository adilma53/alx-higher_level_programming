#!/usr/bin/python3

def best_score(a_dictionary):

    if a_dictionary is None:
        return None

    for key in a_dictionary:
        max_n = a_dictionary[key]
        break

    key = ""

    for i, j in a_dictionary.items():
        if j > max_n:
            max_n = j
            key = i

    return key

a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
best_key = best_score(a_dictionary)
print("Best score: {}".format(best_key))

best_key = best_score(None)
print("Best score: {}".format(best_key))
