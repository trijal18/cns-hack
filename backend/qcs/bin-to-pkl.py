import pickle
import os

# Define file paths
bin_file_path = r"D:\projects\cns\backend\qcs\encrypted_model.bin"  # Path to the binary file
pkl_file_path = "output_file.pkl"  # Path to the output pickle file

try:
    # Read the binary data from the .bin file
    with open(bin_file_path, "rb") as bin_file:
        binary_data = bin_file.read()

    # Serialize the binary data into a .pkl file
    with open(pkl_file_path, "wb") as pkl_file:
        pickle.dump(binary_data, pkl_file)

    print(f"Successfully converted {bin_file_path} to {pkl_file_path}")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    os.remove(pkl_file_path)