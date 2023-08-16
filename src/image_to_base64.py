import re
import os
import sys
import shutil
from base64 import b64encode

# Ensure README file exists; copy from original if not
def ensure_readme_exists(output_folder, readme_path):
    if not os.path.exists(readme_path):
        original_readme_path = "README.md"
        os.makedirs(output_folder, exist_ok=True)
        shutil.copy(original_readme_path, readme_path)
        print(f"README file {readme_path} not found. Copied from {original_readme_path}.")

# Read the content of the README.md file
def read_readme_content(readme_path):
    with open(readme_path, 'r') as file:
        return file.read()

# Convert the image to Base64
def convert_image_to_base64(image_path, input_folder):
    image_file_path = os.path.join(input_folder, image_path.split("/")[-1])
    if os.path.exists(image_file_path):
        with open(image_file_path, "rb") as image_file:
            return b64encode(image_file.read()).decode('utf-8')
    else:
        print(f"Warning: Image file {image_file_path} not found.")
        return None

# Main function to convert images to Base64 and update README
def convert_images_to_base64(input_folder, output_folder, readme_path):
    ensure_readme_exists(output_folder, readme_path)
    readme_content = read_readme_content(readme_path)
    image_paths = re.findall(r'<img src="(.*?)"', readme_content)
    os.makedirs(output_folder, exist_ok=True)

    for image_path in image_paths:
        if not image_path.startswith("http"):
            base64_image = convert_image_to_base64(image_path, input_folder)
            if base64_image:
                readme_content = readme_content.replace(image_path, f"data:image/png;base64,{base64_image}")

    with open(readme_path, 'w') as file:
        file.write(readme_content)

    print(f"Conversion complete! Output saved in {readme_path}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <input_folder> <output_folder> <readme_path>")
    else:
        input_folder = sys.argv[1]
        output_folder = sys.argv[2]
        readme_path = sys.argv[3]
        convert_images_to_base64(input_folder, output_folder, readme_path)
