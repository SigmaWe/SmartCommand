import pickle

# Replace 'file_path.pickle' with the path to your pickle file
pickle_file_path = 'PickleFile'

def read_pickle_file(file_path):
    with open(file_path, 'rb') as file:
        data = pickle.load(file)
    return data

if __name__ == "__main__":
    loaded_data = read_pickle_file(pickle_file_path)
    print("Data loaded from pickle file:")
    print(loaded_data)
