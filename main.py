import PyPDF2
import os

def find_pdf_in_directory():
    for filename in os.listdir('.'):
        if filename.endswith('.pdf'):
            return filename
    raise ValueError("No .pdf file found in the current directory.")

def extract_text_from_pdf(pdf_filename):
    with open(pdf_filename, 'rb') as file:
        # Initialize PDF reader
        pdf_reader = PyPDF2.PdfReader(file)
        
        # Check if the PDF has any pages
        if len(pdf_reader.pages) == 0:
            return "The PDF is empty."
        
        # Extract text from each page
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
    
    return text

def divide_text(text, num_parts):
    # Calculate the length of each part
    part_length = len(text) // num_parts
    
    parts = []
    for i in range(num_parts):
        start_index = i * part_length
        
        # For the last part, ensure it includes any remaining text
        if i == num_parts - 1:
            parts.append(text[start_index:])
        else:
            end_index = start_index + part_length
            parts.append(text[start_index:end_index])
    
    return parts

def save_parts_to_files(parts):
    for index, part in enumerate(parts, 1):
        with open(f"part_{index}.txt", 'w', encoding="utf-8") as file:
            file.write(part)

# Look for the .pdf file in the current directory
pdf_filename = find_pdf_in_directory()

content = extract_text_from_pdf(pdf_filename)

num_parts = int(input("Into how many parts do you want to divide the content? "))
divided_content = divide_text(content, num_parts)

save_parts_to_files(divided_content)
print("Parts saved as individual .txt files in the current directory.")

