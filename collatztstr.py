def collatz_sequence(n):
   
    sequence = [n]
    while n != 1:
        if n % 2 == 0:  
            n //= 2
        else: 
            n = 3 * n + 1
        sequence.append(n)
    return sequence

def test_collatz(limit, max_iterations=1000):

    for i in range(1, limit + 1):
        n = i
        iterations = 0
        while n != 1 and iterations < max_iterations:
            if n % 2 == 0:
                n //= 2
            else:
                n = 3 * n + 1
            iterations += 1

        if iterations == max_iterations:
            print(f"The loop for number {i} did not terminate (possibly not reaching 1)")
            return i  
    print(f"All numbers between 1 and {limit} confirm the hypothesis.")
    return None


limit = int(input("up to which number do you want to test? "))
result = test_collatz(limit)

if result:
    print(f"Number found not to satisfy Collatz hypothesis: {result}")
else:
    print("All tested numbers confirm the hypothesis.")
