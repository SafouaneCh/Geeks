import random

# 1. Simulates rolling a single 6-sided die
def throw_dice():
    return random.randint(1, 6)

# 2-5. Keeps throwing 2 dice until doubles are rolled, returning total count
def throw_until_doubles():
    count = 0
    while True:
        count += 1
        dice1 = throw_dice()
        dice2 = throw_dice()
        if dice1 == dice2:
            break
    return count

# 6-8. Main function running the simulation 100 times
def main():
    results = []
    
    for _ in range(100):
        throws_needed = throw_until_doubles()
        results.append(throws_needed)
    
    total_throws = sum(results)
    average_throws = total_throws / len(results)
    
    print(f"Total throws: {total_throws}")
    print(f"Average throws to reach doubles: {average_throws:.2f}")

