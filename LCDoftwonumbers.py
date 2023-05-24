ch = input('LCD OF TWO NUMBERS')

n1 = int(input('enter your number: '))
n2 = int(input('enter another number: '))


if n1<n2:
    small = n1
else:
    small = n2

d = 2

while d<=small:
    if n1%d == 0 and n2%d == 0:
        print('LCD is',d)
        break

    d = d+1

else:
    print('No LCD')
