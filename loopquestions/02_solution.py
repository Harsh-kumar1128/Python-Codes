number = int(input('Enter the n number for even : '))
even_count = 0
for i in range(1, number+1):
    if i % 2 == 0:
       # even_count = i + even_count
       even_count += 1

print('Even number total',even_count)