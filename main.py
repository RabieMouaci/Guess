import random

def method1(target):
    low = 1
    high = 100
    t = 0
    
    while True:
        guess = (low + high) // 2
        t += 1
        print(f"auto guess: {guess}")
        
        if guess == target:
            print(f"Bingo found the number {target} in the try number: {t}")
            return t
        elif guess < target:
            print("higher")
            low = guess + 1
        else:
            print("lower!")
            high = guess - 1

def method2(target):
    low = 1
    high = 100
    t = 0
    
    while True:
        guess = random.randint(low, high)
        t += 1
        print(f"Auto guess: {guess}")
        
        if guess == target:
            print(f"Bingo found the number {target} in the try number: {t}")
            return t
        elif guess < target:
            print("Higher!")
            low = guess + 1
        else:
            print("Lower!")
            high = guess - 1

def method3(target):
    guess = target  # Simplified version since it's just returning the number directly
    print(f"Bingo found the number {guess} in the try number: 1")
    return 1

def main():
    sehih = random.randint(1, 100)
    j = 1
    
    print("try to guess a number (between 1 and 100)\n")
    
    while True:
        try:
            k = int(input("guess: "))
            j += 1
            
            if k < sehih:
                print("higher")
            elif k > sehih:
                print("lower")
            else:
                print(f"bingo u got it in try number {j}")
                break
        except ValueError:
            print("Please enter a valid number")
            continue
    
    a1 = j
    
    print("--- auto search with method 1 ---")
    a2 = method1(sehih)
    print("--- auto search with method 2 ---")
    a3 = method2(sehih)
    print("--- auto search with method 3 ---")
    a4 = method3(sehih)
    
    print(f"\nhuman: {a1}\nbinaire: {a2}\nrandom: {a3}\nquantum computer: {a4}")

if __name__ == "__main__":
    main()
