# Task 3: Task Automation

A collection of automation tools for file management and data extraction.

## 🛠️ Features

### 1. Email Extractor
- Extract email addresses from text files
- Support for multiple file encodings (UTF-8, Latin-1, CP1252)
- Remove duplicates and sort alphabetically
- Save results to a formatted text file with metadata

### 2. Image File Mover
- Move image files (.jpg, .jpeg, .png, .gif, .bmp, .webp) between folders
- Options to select specific file types
- Handle duplicate files automatically (renames if needed)
- Create destination folders if they don't exist

### 3. File Organizer
- Organize files by their extensions
- Create subfolders for each file type
- Move files into appropriate folders automatically
- Handles files without extensions

## 🚀 How to Run

```bash
cd Task3_Automation
python automation.py
```

## 📋 Menu Options

1. **Extract emails from text file** - Extract and save email addresses
2. **Move image files to another folder** - Organize image files
3. **Organize files by extension** - Sort files into folders by type
4. **Exit** - Close the application

## 💡 Usage Examples

### Email Extractor
```
Enter the input file path: data.txt
✅ Found 25 email(s) (20 unique)

First 10 emails found:
  - user1@example.com
  - user2@example.com
  ...

Enter output file name: extracted_emails
✅ Emails saved to extracted_emails.txt
```

### Image File Mover
```
Enter source folder path: C:\Photos
Enter destination folder path: C:\Organized\Images

Select file types to move:
1. .jpg files only
2. .jpg and .jpeg files
3. All image files (.jpg, .jpeg, .png, .gif)
Enter choice (1-3): 3

✅ Found 15 image file(s)
Move 15 file(s)? (yes/no): yes
✅ Successfully moved 15 file(s)!
```

### File Organizer
```
Enter folder path to organize: C:\Downloads
✅ Found 50 file(s) with 8 different extension(s)

Organize files into subfolders? (yes/no): yes
✅ Successfully organized 50 file(s)!
```

## 🔧 Requirements

- Python 3.6+
- Standard library only (uses `re`, `os`, `shutil`, `datetime`)

## 📦 Files

- `automation.py` - Main application file
- `README.md` - This documentation

## ⚠️ Important Notes

- **File Operations**: The mover and organizer functions physically move files (not copy)
- **Backup**: Always backup important files before using automation tools
- **Permissions**: Ensure you have read/write permissions for the folders
- **Path Format**: Use forward slashes (/) or double backslashes (\\) in Windows paths

## 💡 Code Features

- Clean, well-documented code
- Error handling for file operations
- Multiple encoding support for text files
- User-friendly interface with confirmations
- Follows Python PEP 8 style guidelines
