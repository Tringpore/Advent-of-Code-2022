f = open('C:\\Users\\Jj Kwan\\Documents\\Advent of Code 2022\\Day 3\\AOC22 Day 3 Input.txt')
comp1 = ''
comp2 = ''
sum = 0

'''
for line in f.readlines():
    line = line.rstrip('\n')
    half = int(len(line)/2)
    comp1 = line[:half]
    comp2 = line[half:]
    common_char = ''.join(set(comp1).intersection(comp2))
    if ord(common_char) < 95:
        #Capital
        sum += ord(common_char) - 38
    else:
        #Small
        sum += ord(common_char) - 96

print(sum)
'''
#Part 1 Answer = 7701

n = 0
elf1 = ''
elf2 = ''
elf3 = ''

for line in f.readlines():
    line = line.rstrip('\n')
    if n == 0:
        elf1 = line
        n += 1
    elif n ==1:
        elf2 = line
        n += 1
    else:
        elf3 = line
        common_char = ''.join(set(elf1).intersection(elf2).intersection(elf3))
        if ord(common_char) < 95:
            #Capital
            sum += ord(common_char) - 38
        else:
            #Small
            sum += ord(common_char) - 96
        n = 0

print(sum)
#Part 2 Answer = 2644