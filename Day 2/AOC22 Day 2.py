f = open('C:\\Users\\Jj Kwan\\Documents\\Advent of Code 2022\\Day 2\\AOC22 Day 2 Input.txt')
sum = 0

'''
for line in f.readlines():
    line = line.rstrip('\n')
    match line:
        #Play A = Rock
        case 'A X':
            sum += 1 + 3
        case 'A Y':
            sum += 2 + 6
        case 'A Z':
            sum += 3 + 0
        #Play B = Paper
        case 'B X':
            sum += 1 + 0
        case 'B Y':
            sum += 2 + 3
        case 'B Z':
            sum += 3 + 6
        #Play C = Scissors
        case 'C X':
            sum += 1 + 6
        case 'C Y':
            sum += 2 + 0
        case 'C Z':
            sum += 3 + 3
        case other:
            print('error')
            break

f.close()
print(sum)
'''

'''
A = Rock
B = Paper
C = Scissors
X = Rock
Y = Paper
Z = Scissors

A X Tie
A Y Win
A Z Lose
B X Lose
B Y Tie
B Z Win
C X Win
C Y Lose
C Z Tie
'''
#Part 1 Answer = 12535

#Part 2
'''
A = Rock
B = Paper
C = Scissors
X = Lose
Y = Draw
Z = Win

A C X Lose
A A Y Draw
A B Z Win
B A X Lose
B B Y Draw
B C Z Win
C B X Lose
C C Y Draw
C A Z Win
'''
for line in f.readlines():
    line = line.rstrip('\n')
    match line:
        #Play A = Rock
        case 'A X':
            sum += 3 + 0
        case 'A Y':
            sum += 1 + 3
        case 'A Z':
            sum += 2 + 6
        #Play B = Paper
        case 'B X':
            sum += 1 + 0
        case 'B Y':
            sum += 2 + 3
        case 'B Z':
            sum += 3 + 6
        #Play C = Scissors
        case 'C X':
            sum += 2 + 0
        case 'C Y':
            sum += 3 + 3
        case 'C Z':
            sum += 1 + 6
        case other:
            print('error')
            break

f.close()
print(sum)
#Part 2 Answer = 15457