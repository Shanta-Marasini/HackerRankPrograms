import string
print('Hello my world')

size = int(input(''))
# a = { 1:'a', 2:'b', 3:'c', 4:'d', 5:'e',
#       6:'f', 7:'g', 8:'h', 9:'i', 10:'j',
#       11:'k', 12:'l', 13:'m', 14:'n', 15:'o',
#       16:'p', 17:'q', 18:'r', 19:'s', 20:'t',
#       21:'u', 22:'v', 23:'w', 24:'x', 25:'y', 26:'z'}

a = string.ascii_lowercase

width = (size - 1) * 4 + 1
lines = (size * 2) - 1
identical_lines = (lines-1)//2
end = size-1

for i in range(identical_lines+1):
    main= ''
    side = ''
    next_side = ''
    side_end = size-1

    for j in range(i):
        side += a[side_end]+'-'
        next_side = '-' + a[side_end]+next_side
        side_end -= 1
    main = side + a[end] + next_side
    end -=1
    print(main.center(width, '-'))

end += 2
for i in range(identical_lines-1,-1,-1):
    main= ''
    side = ''
    next_side = ''
    side_end = size-1

    for j in range(i):
        side += a[side_end]+'-'
        next_side = '-' + a[side_end]+next_side
        side_end -= 1
    main = side + a[end] + next_side
    end +=1
    print(main.center(width, '-'))


