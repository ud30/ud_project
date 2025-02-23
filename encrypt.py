import cv2
import os

def encrypt_image(image_path, message, password):
    img = cv2.imread(image_path)  # Load the image

    if img is None:
        print("Error: Image not found. Check the file path.")
        return

    d = {chr(i): i for i in range(255)}

    n, m, z = 0, 0, 0

    for char in message:
        img[n, m, z] = d[char]
        n += 1
        m += 1
        z = (z + 1) % 3

    cv2.imwrite("encryptedImage.jpg", img)
    print("Message encrypted and saved as 'encryptedImage.jpg'.")
    os.system("start encryptedImage.jpg")  # Open the encrypted image on Windows

if __name__ == "__main__":
    image_path = input("Enter image path: ")
    message = input("Enter secret message: ")
    password = input("Set a passcode for decryption: ")

    with open("password.txt", "w") as file:
        file.write(password)  # Save password for decryption

    encrypt_image(image_path, message, password)
