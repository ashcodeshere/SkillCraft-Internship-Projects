# Develop a single encryption tool using pixel manipulation that Supports basic operations like swapping pixel values 
# or applying a basic mathematical operations to each pixel

from PIL import Image

def encrypt_image(INPUT_PATH,OUTPUT_PATH,key=None):
    img=Image.open(INPUT_PATH).convert("RGB")
    pixels=img.load()
    width,height=img.size
    for i in range(width):
        for j in range(height):
            r,g,b=pixels[i,j]
            decrypted_pixel=(r+10,g-92,b+85)
            pixels[i,j]=decrypted_pixel
    img.save(OUTPUT_PATH)



def decrypt_image(INPUT_PATH,OUTPUT_PATH,key=None):
    img=Image.open(INPUT_PATH)
    pixels=img.load()
    width,height=img.size
    for i in range(width):
        for j in range(height):
            r,g,b=pixels[i,j]
            decrypted_pixel=(r-10,g+92,b-85)
            pixels[i,j]=decrypted_pixel
    img.save(OUTPUT_PATH)



INPUT_IMG=r"-" #Add inputfile path
OUTPUT_IMG=r"-" #Add outputfile path
encrypt_image(INPUT_PATH=INPUT_IMG,OUTPUT_PATH=OUTPUT_IMG)
INPUT_IMG=OUTPUT_IMG
OUTPUT_IMG=r"-" #Add outputfile path
decrypt_image(INPUT_IMG,OUTPUT_IMG)
print(" !!Task Completed!! ")