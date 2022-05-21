def remove_chars(base, chars):
  new_string = base
  for char in chars:
    new_string = new_string.replace(char, "")

  return new_string

result = remove_chars("hello worlds", " ")

print(result)


def compare_lists(lst1=[], lst2=[]):
  # Write your code here.

  unique_elements = 0
  unique_array = []

  for num in lst1:
    if num in lst2 and num not in unique_array:
      unique_elements += 1
      unique_array.append(num)

  return unique_elements

  def running_sums(numbers):
    # Write your code here.
    # if len(numbers) == 0:
    # return []

    for i in range(1, len(numbers)):
      sum = numbers[i] + numbers[i - 1]
      numbers.pop(i)
      numbers.insert(i, sum)

    return numbers


























