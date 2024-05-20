# Custom Sorting of Integers

This project demonstrates how to process a file containing integers, remove duplicates, and sort them without using standard built-in libraries for sorting. It provides a solution in Python that implements a custom sorting algorithm (bubble sort) instead of relying on standard sorting functions.

## Usage

1. **Clone the Repository:**

    ```
    git clone https://github.com/Pnayiturik/DSA-HW01.git
    cd DSA-HW01
    ```

2. **Run the Script:**

    Execute the Python script `UniqueInt.py` with the following command:

   

    by replacing `input_file_path` with the path to your input file and `output_file_path` with the desired path for the output file.
    you can check for other samples

    For example:

    ```
    python process_file.py results_for_sample_inputs/small_sample_input_01.txt_result.txt sample_input_for_students/small_sample_input_01.txt
    ```

4. **Output:**

    The script will process the input file, remove duplicate integers, and sort the unique integers in ascending order. The sorted integers will be written to the specified output file.

    You will see a message indicating that the unique integers have been written to the output file.
   ```
    in case you want to write them to the output file
    ```

## Implementation Details

- The script reads integers from the input file and stores them in a list.
- Duplicates are removed by converting the list to a set and then back to a list.
- A custom sorting algorithm (bubble sort) is implemented to sort the list of unique integers.
- The sorted integers are written to the output file.

## Limitations

- This project is designed to handle small to moderate-sized input files containing integers within the range [-1023, 1023].
- The custom sorting algorithm (bubble sort) used in this project may not be efficient for large datasets.


