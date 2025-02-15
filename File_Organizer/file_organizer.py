import os
import shutil

# Define file categories and their extensions
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Scripts": [".py", ".js", ".sh", ".bat"],
    "Executables": [".exe", ".msi"],
    "Others": []
}


def organize_files(directory):
    """Organizes files in the specified directory based on their extensions."""
    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' does not exist.")
        return

    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)

        if os.path.isfile(file_path):  # Check if it's a file
            file_ext = os.path.splitext(file)[1].lower()  # Get file extension

            # Find the category
            folder_name = "Others"
            for category, extensions in FILE_CATEGORIES.items():
                if file_ext in extensions:
                    folder_name = category
                    break

            # Create category folder if it doesn’t exist
            folder_path = os.path.join(directory, folder_name)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            # Move file to respective folder
            shutil.move(file_path, os.path.join(folder_path, file))
            print(f"Moved: {file} → {folder_name}/")


if __name__ == "__main__":
    directory = input("Enter the directory path to organize: ").strip()
    organize_files(directory)
    print("✅ File organization completed!")
