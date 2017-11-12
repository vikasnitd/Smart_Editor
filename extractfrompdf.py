import io
from PIL import Image
import pytesseract

from wand.image import Image as im

pdf = im(filename='IT-2013-14.pdf', resolution= 500)

pdf_to_img = pdf.convert('jpeg')

images=[]

for imag in pdf_to_img.sequence:
    imagePage = im(image=imag)
    images.append(imagePage.make_blob())

converted_text = []

for blob in images:
    img = Image.open(io.BytesIO(blob))
    text = pytesseract.image_to_string(img , lang ="eng")
    converted_text.append(text)

for page in converted_text:
    print page
