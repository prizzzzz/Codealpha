"""
================================================================================
TASK 3: TASK AUTOMATION
================================================================================
A collection of automation tools for file management and data extraction.
================================================================================
"""

import re
import os
import shutil
from pathlib import Path
from datetime import datetime

def extract_emails_from_file():
    """Extract email addresses from a text file and save to another file"""
    
    print("=" * 70)
    print("EMAIL EXTRACTOR - Task Automation")
    print("=" * 70)
    
    # Get input file
    while True:
        input_file = input("\nEnter the input file path: ").strip()
        
        if not input_file:
            print("❌ Please enter a file path!")
            continue
        
        if not os.path.exists(input_file):
            print("❌ File not found! Please check the path.")
            continue
        
        break
    
    # Enhanced email regex pattern
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    
    try:
        # Read input file with multiple encoding attempts
        content = ""
        encodings = ['utf-8', 'latin-1', 'cp1252']
        for encoding in encodings:
            try:
                with open(input_file, 'r', encoding=encoding) as file:
                    content = file.read()
                break
            except UnicodeDecodeError:
                continue
        
        if not content:
            print("❌ Could not read file with supported encodings!")
            return
        
        # Extract emails
        emails = re.findall(email_pattern, content, re.IGNORECASE)
        
        if not emails:
            print("\n⚠️  No email addresses found in the file!")
            return
        
        # Remove duplicates and sort
        unique_emails = sorted(list(set(email.lower() for email in emails)))
        
        print(f"\n✅ Found {len(emails)} email(s) ({len(unique_emails)} unique)")
        print(f"\nFirst 10 emails found:")
        for email in unique_emails[:10]:
            print(f"  - {email}")
        if len(unique_emails) > 10:
            print(f"  ... and {len(unique_emails) - 10} more")
        
        # Save to output file
        output_file = input("\nEnter output file name (without extension, or press Enter for 'extracted_emails'): ").strip()
        if not output_file:
            output_file = "extracted_emails"
        output_file += ".txt"
        
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write("EXTRACTED EMAIL ADDRESSES\n")
            file.write("=" * 70 + "\n")
            file.write(f"Source file: {input_file}\n")
            file.write(f"Extraction date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            file.write(f"Total emails found: {len(emails)}\n")
            file.write(f"Unique emails: {len(unique_emails)}\n")
            file.write("=" * 70 + "\n\n")
            
            for email in unique_emails:
                file.write(email + "\n")
        
        print(f"✅ Emails saved to {output_file}")
    
    except Exception as e:
        print(f"❌ Error processing file: {e}")

def move_jpg_files():
    """Move all .jpg files from one folder to another with options"""
    
    print("\n" + "=" * 70)
    print("IMAGE FILE MOVER - Task Automation")
    print("=" * 70)
    
    source_folder = input("\nEnter source folder path: ").strip()
    
    if not os.path.exists(source_folder):
        print("❌ Source folder not found!")
        return
    
    if not os.path.isdir(source_folder):
        print("❌ Source path is not a directory!")
        return
    
    destination_folder = input("Enter destination folder path: ").strip()
    
    if not destination_folder:
        print("❌ Please enter a destination folder!")
        return
    
    # Create destination folder if it doesn't exist
    if not os.path.exists(destination_folder):
        try:
            os.makedirs(destination_folder)
            print(f"✅ Created destination folder: {destination_folder}")
        except Exception as e:
            print(f"❌ Error creating destination folder: {e}")
            return
    
    # Ask for file types
    print("\nSelect file types to move:")
    print("1. .jpg files only")
    print("2. .jpg and .jpeg files")
    print("3. All image files (.jpg, .jpeg, .png, .gif)")
    
    choice = input("Enter choice (1-3): ").strip()
    
    if choice == "1":
        extensions = ['.jpg']
    elif choice == "2":
        extensions = ['.jpg', '.jpeg']
    elif choice == "3":
        extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp']
    else:
        print("⚠️  Invalid choice. Using .jpg files only.")
        extensions = ['.jpg']
    
    try:
        # Find all matching image files
        image_files = []
        for file in os.listdir(source_folder):
            file_lower = file.lower()
            if any(file_lower.endswith(ext) for ext in extensions):
                image_files.append(file)
        
        if not image_files:
            print(f"\n⚠️  No matching image files found in the source folder!")
            return
        
        print(f"\n✅ Found {len(image_files)} image file(s)")
        print("\nFiles to move:")
        for i, file in enumerate(image_files[:10], 1):
            print(f"  {i}. {file}")
        if len(image_files) > 10:
            print(f"  ... and {len(image_files) - 10} more")
        
        confirm = input(f"\nMove {len(image_files)} file(s)? (yes/no): ").lower().strip()
        if confirm not in ['yes', 'y']:
            print("Operation cancelled.")
            return
        
        # Move files
        moved_count = 0
        failed_count = 0
        for file in image_files:
            source_path = os.path.join(source_folder, file)
            destination_path = os.path.join(destination_folder, file)
            
            # Handle duplicate files
            if os.path.exists(destination_path):
                base, ext = os.path.splitext(file)
                counter = 1
                while os.path.exists(destination_path):
                    new_name = f"{base}_{counter}{ext}"
                    destination_path = os.path.join(destination_folder, new_name)
                    counter += 1
            
            try:
                shutil.move(source_path, destination_path)
                print(f"  ✓ Moved: {file}")
                moved_count += 1
            except Exception as e:
                print(f"  ✗ Failed to move {file}: {e}")
                failed_count += 1
        
        print(f"\n✅ Successfully moved {moved_count} file(s)!")
        if failed_count > 0:
            print(f"⚠️  Failed to move {failed_count} file(s)")
    
    except Exception as e:
        print(f"❌ Error: {e}")

def organize_files_by_extension():
    """Organize files in a folder by their extensions"""
    
    print("\n" + "=" * 70)
    print("FILE ORGANIZER - Task Automation")
    print("=" * 70)
    
    folder_path = input("\nEnter folder path to organize: ").strip()
    
    if not os.path.exists(folder_path):
        print("❌ Folder not found!")
        return
    
    if not os.path.isdir(folder_path):
        print("❌ Path is not a directory!")
        return
    
    try:
        files = [f for f in os.listdir(folder_path) 
                if os.path.isfile(os.path.join(folder_path, f))]
        
        if not files:
            print("\n⚠️  No files found in the folder!")
            return
        
        # Organize by extension
        organized = {}
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if not ext:
                ext = "no_extension"
            if ext not in organized:
                organized[ext] = []
            organized[ext].append(file)
        
        print(f"\n✅ Found {len(files)} file(s) with {len(organized)} different extension(s)")
        
        confirm = input("\nOrganize files into subfolders? (yes/no): ").lower().strip()
        if confirm not in ['yes', 'y']:
            print("Operation cancelled.")
            return
        
        moved_count = 0
        for ext, file_list in organized.items():
            # Create subfolder for extension
            ext_folder = os.path.join(folder_path, ext[1:] if ext != "no_extension" else "no_extension")
            if not os.path.exists(ext_folder):
                os.makedirs(ext_folder)
            
            # Move files
            for file in file_list:
                source = os.path.join(folder_path, file)
                destination = os.path.join(ext_folder, file)
                try:
                    shutil.move(source, destination)
                    moved_count += 1
                except Exception as e:
                    print(f"  ✗ Failed to move {file}: {e}")
        
        print(f"\n✅ Successfully organized {moved_count} file(s)!")
    
    except Exception as e:
        print(f"❌ Error: {e}")

def main():
    """Main menu for task automation tools"""
    while True:
        print("\n" + "=" * 70)
        print("TASK AUTOMATION - Choose an operation")
        print("=" * 70)
        print("\n1. Extract emails from text file")
        print("2. Move image files to another folder")
        print("3. Organize files by extension")
        print("4. Exit")
        
        try:
            choice = input("\nEnter your choice (1-4): ").strip()
        except KeyboardInterrupt:
            print("\n\nExiting...")
            break
        
        if choice == "1":
            extract_emails_from_file()
        elif choice == "2":
            move_jpg_files()
        elif choice == "3":
            organize_files_by_extension()
        elif choice == "4":
            print("\nThanks for using Task Automation tools! Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please select 1-4.")

if __name__ == "__main__":
    main()
