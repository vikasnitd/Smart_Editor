import io
from PIL import Image
import pytesseract
# wand is simple ImageMagick binding for Python
from wand.image import Image as im      

pdf = im(filename='IT-2013-14.pdf', resolution= 500)

pdf_to_img = pdf.convert('jpeg')

images=[]
# sequence seeks into files as Python sequences of PIL.pdf_to_img
for imag in pdf_to_img.sequence:
    imagePage = im(image=imag)
    images.append(imagePage.make_blob())
#Blob storage can store any type of text or binary data    

converted_text = []

for blob in images:
    img = Image.open(io.BytesIO(blob))          
    text = pytesseract.image_to_string(img , lang ="eng")
    converted_text.append(text)

for page in converted_text:
    print page
