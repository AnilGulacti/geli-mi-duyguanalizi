
import sys

def check_file_type(filepath):
    try:
        with open(filepath, 'rb') as f:
            header = f.read(10)
            print(f"Header: {header}")
            if b'Keras' in header or b'HDF' in header:
                print("Type: Keras/H5")
            elif b'\x80\x03' in header or b'\x80\x04' in header:
                print("Type: Pickle")
            elif b'PK' in header:
                print("Type: Zip/SavedModel/Joblib")
            else:
                print("Type: Unknown")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    check_file_type('analysis/ml_models/model.file')
