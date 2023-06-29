import os

def rename_files(folder_path):
    # Iterate over all the files in the specified directory
    for filename in os.listdir(folder_path):
        # Check if the file is a .flac file
        if filename.endswith('.flac'):
            # Split the filename into song_name and artist_name
            song_name, artist_name = filename[:-5].split(' - ')
            # Create a new filename with the format 'artist_name - song_name.flac'
            new_filename = f'{artist_name} - {song_name}.flac'
            # Get the absolute paths of the old and new filenames
            old_file_path = os.path.join(folder_path, filename)
            new_file_path = os.path.join(folder_path, new_filename)
            # Rename the file
            os.rename(old_file_path, new_file_path)

def main():
    # Get the current working directory
    folder_path = os.getcwd()
    # Rename the files
    rename_files(folder_path)

if __name__ == '__main__':
    main()
