def number_operations():
    numbers = []
    # Get 10 numbers from user
    print("Enter 10 numbers:")
    for i in range(10):
        # Your code here
        number = int(input("Insert number [" + i + "]: "))
        numbers.append(number)
    # Display original list
    print(f"Original numbers: {numbers}")
    # Create filtered lists
    even_numbers = [] # Your code here
    odd_numbers = [] # Your code here
    # Calculate average
    average = sum(numbers) / 10.0 # Your code here
    # Numbers greater than average
    above_average = [] # Your code here
    for i in range(10):
        if numbers[i] % 2 == 0:
            even_numbers.append(numbers[i])
        else:
            odd_numbers.append(numbers[i])

        if numbers[i] > average:
            above_average.append(numbers[i])

    # Display results
    # Your code here
    print("Even Number List: ", even_numbers)
    print("Odd Number List: ", odd_numbers)
    print("Above Average List: ", above_average)
    print("Sum: ", sum(numbers))
    print("Averge: ", average)
    print("Min: ", min(numbers))
    print("Max: ", max(numbers))

if __name__ == "__main__":
    number_operations()