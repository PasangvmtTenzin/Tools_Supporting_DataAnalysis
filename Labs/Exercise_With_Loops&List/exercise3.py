def copy(lst):
   copy2 = []
   for copy1 in lst:
       copy2.append(copy1)

   return (copy2)

if __name__=='__main__':
   print(copy([]))
   print(copy([1, 2, 3]))