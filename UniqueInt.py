def custom_sort(unique_integers):
    # Custom sorting algorithm
    # Bubble sort implementation
    n = len(unique_integers)
    for i in range(n):
        for j in range(0, n-i-1):
            if unique_integers[j] > unique_integers[j+1]:
                unique_integers[j], unique_integers[j+1] = unique_integers[j+1], unique_integers[j]

def process_file(input_file_path, output_file_path):
    # Dictionary to store unique integers
    unique_integers = []

    # Read input file
    with open(input_file_path, 'r') as input_file:
        for line in input_file:
            try:
                number = int(line.strip())
                if -1023 <= number <= 1023:
                    unique_integers.append(number)
            except ValueError:
                # Skip non-integer lines
                pass

    # Remove duplicates by converting to set
    unique_integers = list(set(unique_integers))
    
    # Sort using custom sort
    custom_sort(unique_integers)
    print(unique_integers)
    # Write to output file
    # with open(output_file_path, 'w') as output_file:
    #     for number in unique_integers:
    #         output_file.write(str(number) + '\n')

    # print("Unique integers written to", output_file_path)

# Example usage
process_file("results_for_sample_inputs/small_sample_input_04.txt_result.txt", "sample_input_for_students/small_sample_input_04.txt")
