import os

# Function to get file details in the current directory
def get_file_details():
    # Get current working directory
    current_directory = os.getcwd()
    
    # List to store file information
    file_info_list = []
    
    # Loop through files in the current directory
    for file_name in os.listdir(current_directory):
        file_path = os.path.join(current_directory, file_name)
        
        # Check if it's a file
        if os.path.isfile(file_path):
            file_info = {
                'file_name': file_name,
                'file_size': os.path.getsize(file_path)
            }
            file_info_list.append(file_info)
    
    return file_info_list

# Get the list of file details and print it
file_details = get_file_details()
print(file_details)
