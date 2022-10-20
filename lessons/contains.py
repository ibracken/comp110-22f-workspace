"""Example implementing a list utility function"""

# Function name: contains 
# We will have 2 parameters: needle(str), haystack (list[str])
# Return type will be Bool



def contains(needle: str, haystack: str) -> bool:
    # Gameplan:
# 1. Start with first index
    i = 0
    # 2. Loop through every index
    while i <= len(haystack):
        # 2.A Test if item at index equal to needle
        if needle[i] == haystack:      
        # 2.A. True Return True ! We found it!
            return True
        else:
            i += 1
    #3 Return False
    return False

print (contains)