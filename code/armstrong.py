def armstrong():
  armstrong_list = []
  print("Enter the range :")
  n = int(input())

  for num in range(1, n+1):

    order = 3
    sum = 0

    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10

    if num == sum:
        armstrong_list.append(num)
  return armstrong_list
