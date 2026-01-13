nums = [10,15,20,25,30,35,40]

even_num = [num for num in nums if num%2==0]
even_num1 = list(filter(lambda n :n%2==0,nums))
squared_num = list(map(lambda n : n*n,nums))
print(even_num)
print(even_num1)
print(squared_num)

