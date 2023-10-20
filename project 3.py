start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
if start > end:
    print("Invalid range. Starting number should be less than or equal to the ending number.")
else:
    print("Positive numbers in the range from", start, "to", end, "are:")
    for number in range(start, end + 1):
        if number > 0:
            print(number)
