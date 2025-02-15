# 📂 File Organizer

File Organizer is a Python script that automatically sorts files into categorized folders based on their extensions. It helps keep your directories clean and structured by moving files into predefined categories such as Images, Documents, Videos, and more.

## 🚀 Features

✅ Automatically categorizes files into folders (Images, Documents, Videos, Audio, etc.)  
✅ Handles unknown file types by placing them in an "Others" folder  
✅ Prevents duplicate organization by checking existing folders  
✅ Lightweight and easy to use – just run the script and let it organize!  
✅ Works with multiple file formats  

## 🛠 Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/file_organizer.git
   cd file_organizer
   ```

2. **Run the Script**
   ```bash
   python file_organizer.py
   ```

## 📌 Usage

1. Run the script and provide the directory path when prompted:
   ```bash
   Enter the directory path to organize: /path/to/directory
   ```
2. The script will automatically sort files into categorized folders.

## 📂 Categorized File Types
The script sorts files into the following categories:

| Category     | File Extensions |
|-------------|----------------|
| Images      | .jpg, .jpeg, .png, .gif, .bmp, .svg |
| Documents   | .pdf, .doc, .docx, .txt, .xls, .xlsx, .ppt, .pptx |
| Videos      | .mp4, .mkv, .avi, .mov |
| Audio       | .mp3, .wav, .aac |
| Archives    | .zip, .rar, .tar, .gz |
| Scripts     | .py, .js, .sh, .bat |
| Executables | .exe, .msi |
| Others      | Any other file types |

## 🛠 Dependencies

- Python 3.x
- `os` and `shutil` (built-in Python libraries)

## 📌 Future Enhancements

🔹 Add logging for tracking file movements  
🔹 Implement an "Undo" feature to revert file moves  
🔹 Create a GUI interface for easier usage  

## 🤝 Contributing

Contributions are welcome! If you have ideas or improvements, feel free to fork the repository and submit a pull request.

## 📜 License

This project is licensed under the MIT License. Feel free to use and modify it.

---

⭐ **Star this repository** if you found it useful! 😊

