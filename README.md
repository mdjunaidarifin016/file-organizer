# Python File Organizer

A Python command-line application that automatically organizes files into folders based on their file extensions.

## Features

- Organizes files according to their extensions.
- Automatically creates category folders.
- Supports files inside subfolders and nested folders.
- Handles duplicate filenames without overwriting existing files.
- Places unknown file types into an `Others` folder.
- Includes error handling for file and directory operations.
- Uses a separate Python module for extension mappings.
- Interactive command-line interface.

## Technologies Used

- Python
- `os`
- `shutil`

## Project Structure

```text
file-organizer/
├── main.py
└── directory_find.py
```

### `main.py`

Contains the main file-organizing logic, file movement, duplicate handling, error handling, and user interface.

### `directory_find.py`

Contains the mapping between file extensions and their corresponding folders.

## How It Works

The program asks the user for a directory path and scans the directory for files.

For example:

```text
.jpg  → Photos
.png  → Photos
.mp4  → Videos
.mp3  → Audio
.pdf  → Documents
.py   → Codes
.zip  → Archives
```

Files found inside subfolders are also detected and organized.

## Example

### Before

```text
Downloads/
├── photo.jpg
├── song.mp3
├── document.pdf
└── Projects/
    ├── program.py
    └── image.png
```

### After

```text
Downloads/
├── Photos/
│   ├── photo.jpg
│   └── image.png
├── Audio/
│   └── song.mp3
├── Documents/
│   └── document.pdf
└── Codes/
    └── program.py
```

## Duplicate File Handling

If a file with the same name already exists, the program does not overwrite it.

For example:

```text
photo.jpg
photo_1.jpg
photo_2.jpg
```

## How to Run

Make sure Python is installed on your system.

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
```

### 2. Navigate to the project directory

```bash
cd file-organizer
```

### 3. Run the program

```bash
python main.py
```

Enter the directory path you want to organize when prompted.

## What I Learned

While building this project, I practiced:

- File and directory handling with Python
- Using the `os` module
- Using the `shutil` module
- Working with file extensions
- Exception handling
- Creating and importing Python modules
- Using `os.walk()` for recursive directory traversal
- Handling duplicate filenames
- Git and GitHub

## Future Improvements

- Add a graphical user interface
- Allow users to customize folder categories
- Add a preview mode before moving files
- Improve logging and reporting
- Add automated tests

---

Built as a hands-on Python project to improve my programming and problem-solving skills.
