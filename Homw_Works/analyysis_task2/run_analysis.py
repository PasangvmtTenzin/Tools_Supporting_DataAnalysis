# run_analysis.py

import sys
from iris_analysis.io.load import load_data
from iris_analysis.io.save import save_result
from iris_analysis.calculate import calculate_statistics

def main(input_filepath, output_filepath):
    # Load data
    data = load_data(input_filepath)
    
    # Calculate statistics
    result = calculate_statistics(data)
    
    # Save result
    save_result(output_filepath, result)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python run_analysis.py <input_filepath> <output_filepath>")
        sys.exit(1)
    input_filepath = sys.argv[1]
    output_filepath = sys.argv[2]
    main(input_filepath, output_filepath)
