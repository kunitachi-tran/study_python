from pdf2image import convert_from_path
import pytesseract
from PIL import Image
import os

# Đường dẫn đến file PDF
pdf_path = 'D:/HoanTV3/Learning/IT/Python/study_projects/OCR_ReadPDF/BID/BID_Q1_2024.pdf'
#pdf_path = 'BID_Q1_2024.pdf'
poppler_path = 'D:/Setups/poppler-24.02.0/Library/bin'

# Chuyển đổi PDF thành hình ảnh
pages = convert_from_path(pdf_path=pdf_path,dpi=500,poppler_path=poppler_path)

# Tạo thư mục tạm thời để lưu hình ảnh
temp_dir = 'temp_images'
os.makedirs(temp_dir, exist_ok=True)

# Lưu các hình ảnh vào thư mục tạm thời
for i, page in enumerate(pages):
   image_path = os.path.join(temp_dir, f'page_{i}.png')
   page.save(image_path, 'PNG')

# Sử dụng OCR để đọc nội dung từ các hình ảnh
text = ''

for i, image_path in enumerate(sorted(os.listdir(temp_dir))):
    image_path = os.path.join(temp_dir, image_path)
    text += f"Trang {i}: \n {pytesseract.image_to_string(image_path)}" 

with open("BID_Q1_2024.txt",mode="w") as file:
    file.write(text)

file.close()

# In nội dung đã đọc
print(text)

# Xóa thư mục tạm thời và các hình ảnh đã tạo
# for image_path in os.listdir(temp_dir):
#     os.remove(os.path.join(temp_dir, image_path))
# os.rmdir(temp_dir)