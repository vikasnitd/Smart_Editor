from PIL import Image
import pytesseract

im = Image.open("img.jpg")  # creating an image object

text = pytesseract.image_to_string(im, lang="eng" ) #recognize text from the image 

print(text) #print the text


