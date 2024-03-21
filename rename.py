import os

# Define a counter to keep track of the image number
counter = 1

# Get the current working directory (change this to your desired folder path)
folder_path = r"C:\Users\bruth\Downloads\Photos-001"  # Replace with your actual folder path (use raw string)

# Loop through all the files in the folder
for filename in os.listdir(folder_path):
  # Check if the file is an image file (modify extensions as needed)
  if filename.endswith((".jpg", ".jpeg", ".png")):
    # Construct the new filename
    new_filename = f"{counter}.{filename.split('.')[-1]}"

    # Rename the file
    os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))

    # Increment the counter
    counter += 1

print("Images renamed successfully!")
