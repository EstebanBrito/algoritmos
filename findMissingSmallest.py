foo = [1, 3, 6, 4, 1, 2]
bar = [-1, -3]

def find_missing_smallest(orig_array):
  array = sorted(orig_array)
  TOP = 100000
  smallest = 1
  for i in array:
    if smallest == i:
      if i == TOP:
        return None
      else:
        smallest = smallest + 1
  print(smallest)
  return smallest

find_missing_smallest(foo) # -> 5
find_missing_smallest(bar) # -> 1