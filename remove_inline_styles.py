import os
import re

# Directory containing your game HTML files
directory = r"C:\Users\Passionet\New folder\braingames"

# Regex pattern to match the .game-header .title inline styles
pattern = r'\.game-header \.title \{\s*font-size: 28px;\s*font-weight: 700;\s*\}'

# Process each HTML file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".html"):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()

        # Remove the inline styles
        new_content = re.sub(pattern, '', content, flags=re.DOTALL)

        # Write the updated content back to the file
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(new_content)

        print(f"Updated {filename}")