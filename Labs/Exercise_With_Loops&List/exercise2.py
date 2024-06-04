def how_many(lst, what):
    count = 0

    for element in lst:
        if element == what:
            count += 1

    return count

if __name__=='__main__':
   
   # Test cases
   print(how_many([], 13))                                      # Output: 0
   print(how_many([1, 234, 123, 23, 1, 234, 1, -43], 1))        # Output: 3
   print(how_many(["Mary", "Jenny", "Mary", "Susan"], "Mary"))  # Output: 2
   print(how_many(["Mary", "Jenny", "Mary", "Susan"], "Emily")) # Output: 0
   print(how_many("Mary has a little lamb", "a"))               # Output: 4


