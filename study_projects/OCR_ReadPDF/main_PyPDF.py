import PyPDF2

# Path to your PDF file
pdf_path = 'D:/HoanTV3/Learning/IT/Python/study_projects/OCR_ReadPDF/BID_Q1_2024.pdf'

# Open the PDF file in binary mode
with open(pdf_path, 'rb') as file:
    # Create a PDF file reader object
    pdf_reader = PyPDF2.PdfReader(file)
    
    # Get the total number of pages in the PDF
    num_pages = len(pdf_reader.pages)
    print(f"Number of pages: {num_pages}")
    # Extract text from each page
    extracted_text = ''
    for page_num in range(num_pages):
        # Get a specific page object
        page = pdf_reader.pages[page_num]
        
        # Extract text from the page
        text = page.extract_text()
        
        # Append the extracted text to the result
        print(f"Page: {page_num}. Text: {text}")
        extracted_text += text

# Print or use the extracted text
print(extracted_text)

with open("BID_Q1_2024_PyPDF2.txt",mode="w") as file:
    file.write(extracted_text)

file.close()