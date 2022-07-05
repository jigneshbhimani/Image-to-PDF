import img2pdf
from PIL import Image

# Image path
img_path = "C:/Users/DELL/OneDrive/Pictures/LifeCycleMethod.png"

# PDF path
pdf_path = "C:/Users/DELL/OneDrive/Pictures/file.pdf"

# Open image
image = Image.open(img_path)

# Converting into chunks using img2pdf
pdf_bytes = img2pdf.convert(image.filename)

# Creating pdf file
file = open(pdf_path, "wb")

# Writing pdf files with chunks
file.write(pdf_bytes)

# Closing image file
image.close()

# Closing pdf file
file.close()

print("Successfully made pdf file")