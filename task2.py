# Develop a simple image encryption tool using pixel manipulation that support operations
# like swapping pixel values or applying a basic mathematical operation to each pixel.

from PIL import Image

def encrypt_image(INPUT_PATH, OUTPUT_PATH, key=(10, -92, 85), mode="math"):
    try:
        img=Image.open(INPUT_PATH).convert("RGB")
        pixels=img.load()
        width, height=img.size
        if mode.upper()=="MATH":
            for i in range(width):
                for j in range(height):
                    try:
                        r,g,b = pixels[i, j]
                        kr,kg,kb=key
                        encrypted_pixel=((r + kr) % 256, (g + kg) % 256, (b + kb) % 256)
                        pixels[i,j]=encrypted_pixel
                    except Exception as e:
                        print(f"Error processing pixel ({i},{j}): {e}")
        elif mode.upper()=="SWAP":
            for i in range(width):
                for j in range(height // 2):
                    try:
                        opposite_j=height-1-j
                        pixels[i,j],pixels[i,opposite_j]=pixels[i,opposite_j],pixels[i,j]
                    except Exception as e:
                        print(f"Error swapping pixel ({i},{j}): {e}")
        else:
            print(f"Unknown mode: {mode}")
            return
        img.save(OUTPUT_PATH)
        print(f"Image encrypted and saved to {OUTPUT_PATH}")
    except Exception as e:
        print(f"Failed to encrypt image: {e}")

def decrypt_image(INPUT_PATH, OUTPUT_PATH, key=(10, -92, 85), mode="math"):
    try:
        img=Image.open(INPUT_PATH).convert("RGB")
        pixels=img.load()
        width, height=img.size
        if mode.upper()=="MATH":
            for i in range(width):
                for j in range(height):
                    try:
                        r,g,b=pixels[i, j]
                        kr,kg,kb=key
                        decrypted_pixel=((r-kr)%256,(g-kg)%256,(b-kb)%256)
                        pixels[i,j]=decrypted_pixel
                    except Exception as e:
                        print(f"Error processing pixel ({i},{j}): {e}")
        elif mode.upper()=="SWAP":
            for i in range(width):
                for j in range(height // 2):
                    try:
                        opposite_j=height-1-j
                        pixels[i,j],pixels[i,opposite_j]=pixels[i,opposite_j],pixels[i,j]
                    except Exception as e:
                        print(f"Error swapping pixel ({i},{j}): {e}")
        else:
            print(f"Unknown mode: {mode}")
            return
        img.save(OUTPUT_PATH)
        print(f"Image decrypted and saved to {OUTPUT_PATH}")
    except Exception as e:
        print(f"Failed to decrypt image: {e}")

def compare_images(img1_path, img2_path, diff_output_path=None):
    try:
        img1=Image.open(img1_path).convert("RGB")
        img2=Image.open(img2_path).convert("RGB")
        if img1.size!=img2.size:
            print("Images are different sizes. Cannot compare.")
            return
        width, height=img1.size
        pixels1=img1.load()
        pixels2=img2.load()
        diff_img=Image.new("RGB", (width, height), (0, 0, 0))
        diff_pixels=diff_img.load()
        total_pixels=width * height
        matching_pixels=0
        for i in range(width):
            for j in range(height):
                if pixels1[i, j]==pixels2[i, j]:
                    diff_pixels[i, j]=(0, 0, 0) # Black pixel if Same
                    matching_pixels+=1
                else:
                    diff_pixels[i, j]=(255, 0, 0)  # Red pixel if different

        if diff_output_path:
            diff_img.save(diff_output_path)
            print(f"Difference image saved to: {diff_output_path}")
        print(f"Matching pixels: {matching_pixels}/{total_pixels}")
        print(f"Accuracy: {(matching_pixels / total_pixels) * 100:.2f}%")
    except Exception as e:
        print(f"Error comparing images: {e}")


if __name__ == "__main__":
    INPUT_IMG=r"C:\Users\ANSHU\Pictures\Screenshots\Screenshot (1).png"
    ENCRYPTED_IMG=r"A:\Projects\Internship Projects\encrypted.png"
    DECRYPTED_IMG=r"A:\Projects\Internship Projects\decrypted.png"
    DIFF_IMG=r"A:\Projects\Internship Projects\difference.png"
    print(f"{"-"*50}Welcome{"-"*50}")
    print("1. Encrypt Image")
    print("2. Decrypt Image")
    print("3. Compare Image")
    n=int(input("Enter Operation : "))
    if n==1:
        print("Modes : \n\'MATH\':For applying basic math operations.\n\'SWAP\':For applying Pixel Swapping\n")
        selected_mode=input("Enter mode according to above: ")
        print(f"Mode Selected: {selected_mode}\n")
        encrypt_image(INPUT_IMG, ENCRYPTED_IMG, mode=selected_mode)
    elif n==2:
        print("Modes : \n\'MATH\':For applying basic math operations.\n\'SWAP\':For applying Pixel Swapping\n")
        selected_mode=input("Enter mode according to above: ")
        print(f"Mode Selected: {selected_mode}\n")
        decrypt_image(ENCRYPTED_IMG, DECRYPTED_IMG, mode=selected_mode)
    elif n==3:
        compare_images(INPUT_IMG, DECRYPTED_IMG, diff_output_path=DIFF_IMG)
    else:
        print("Not Valid Operation")
    print("Task Completed Successfully!")