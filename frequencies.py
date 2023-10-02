"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    freq = {}
    for item in items:
        item = str(item)
        if item not in freq:
            freq.update({item : 1})
        else:
            freq[item]+=1

    # Your code goes here
    return freq
