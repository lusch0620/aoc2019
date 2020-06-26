import math

def findFuel(mass: int) -> int:
    ans = math.floor(mass/3) - 2
    return ans

def actualFuel(mass: int) -> int:
    ans = 0
    while mass > 0:
        temp = findFuel(mass)
        if temp < 0:
            break
        else:
            mass = temp
        ans += temp
    return ans

assert actualFuel(1969) == 966
assert actualFuel(14) == 2
assert actualFuel(100756) == 50346 

def main():
    with open('input.txt') as file:
        masses = [int(line.strip())for line in file]
    part1Ans = sum(findFuel(mass) for mass in masses)
    print(part1Ans)
    part2Ans = sum(actualFuel(mass) for mass in masses)
    print(part2Ans)
    
if __name__ == "__main__":
    main()