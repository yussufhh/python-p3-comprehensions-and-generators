#!/usr/bin/env python3

def return_evens(num_list):
    """Return a list of even numbers from the input list."""
    return [num for num in num_list if num % 2 == 0]
print(return_evens)




def make_exclamation(sentence_list):
    """Return a list of sentences with an exclamation mark at the end."""
    return [sentence + '!' for sentence in sentence_list]
print(make_exclamation)
    