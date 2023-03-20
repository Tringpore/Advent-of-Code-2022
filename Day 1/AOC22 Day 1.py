ind = []
ovr = []
space = '\n'
f = open('C:\\Users\\Jj Kwan\\Documents\\Advent of Code 2022\\Day 1\\AOC22 Day 1 Input.pl')

for line in f.readlines():
    if line != space:
        ind.append(int(line))
    else:
        ovr.append(sum(ind))
        ind = []
f.close()

ovr.append(sum(ind))
ind = []
#Part 1 Answer = 74394

#Part 2
n = 0
x = 0

while n < 3:
    x += max(ovr)
    ovr.remove(max(ovr))
    n += 1

print(x)
#Part 2 Answer = 212836