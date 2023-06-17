import datetime

def intersect_two_arrays_On2(arr1, arr2):
  """Find an intersect array from 2 input arrays."""
  start = datetime.datetime.now()
  result = []
  for item1 in arr1:
    for item2 in arr2:
      if item1 == item2:
        result.append(item2)

  end = datetime.datetime.now()
  difference = end - start
  return [result, difference.total_seconds()]
  
def intersect_two_arrays_On(arr1, arr2):
  """Find an intersect array from 2 input arrays."""
  start = datetime.datetime.now()
  result = []
  dict1 = {}
  for item1 in arr1:
    dict1[item1] = item1
  
  for item2 in arr2:
    if item2 in dict1:
      result.append(item2)

  end = datetime.datetime.now()
  difference = end - start

  return [result, difference.total_seconds()]

def read_data_from_file(path):
  """Read data from file and return array of int"""
  with open(path, 'r') as file:
    data = file.read()
    list_of_strings = data.split('\n')
    arr1 = [int(x.split('\t')[0]) for x in list_of_strings]
    arr2 = [int(x.split('\t')[1]) for x in list_of_strings]
    
  return [arr1, arr2]


def main():
  """Main function to run the program."""
  [arr1, arr2] = read_data_from_file('data/arrays.txt')
  
  print("Start to get intersect of two arrays...")
  intersect = intersect_two_arrays_On(arr1, arr2)
  print("Intersect is: ", intersect[0], "got for", intersect[1], "s")

if __name__ == '__main__':
  main()
