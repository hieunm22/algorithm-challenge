def intersect_two_arrays_On2(arr1, arr2):
  """Find an intersect array from 2 input arrays."""
  result = []
  for item1 in arr1:
    for item2 in arr2:
      if item2 in arr1:
        result.append(item2)

  return result
  
def intersect_two_arrays_On(arr1, arr2):
  """Find an intersect array from 2 input arrays."""
  result = []
  dict1 = {}
  for item1 in arr1:
    dict1[item1] = item1
  
  for item2 in arr2:
    if item2 in dict1:
      result.append(item2)

  return result

def read_data_from_file(path):
  """Read data from file and return array of int"""
  with open(path, 'r') as file:
    data = file.read()
    list_of_strings = data.split(',')
    list_of_intergers = [int(x) for x in list_of_strings]
    
  return list_of_intergers


def main():
  """Main function to run the program."""
  arr1 = read_data_from_file('data/1.txt')
  arr2 = read_data_from_file('data/2.txt')
  print("Start to get intersect of two arrays...")
  intersect = intersect_two_arrays_On(arr1, arr2)
  print("Intersect is: ", intersect)

if __name__ == '__main__':
  main()
