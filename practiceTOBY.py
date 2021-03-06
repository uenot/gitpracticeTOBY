# Partner 1: Toby Ueno
# Partner 2: Justin Dao
#######################
# Assignment Name: GitHub Practice- 20 points- 2/25/20

def getNRandom(n):
    '''takes in an integer and returns a list of n random integers between 1 and 10, inclusive'''
    nums = []
    import random as rand
    for i in range(n):
        nums.append(rand.randint(1, 10))
    return nums

def multiplyRandom(numbers):
    '''takes in a list of n numbers and returns the product of the numbers'''
    product = 1
    for number in numbers:
        product = product*int(number)
    return product

def main():
    print(multiplyRandom(getNRandom(10)))

if __name__ == "__main__":
    main()
