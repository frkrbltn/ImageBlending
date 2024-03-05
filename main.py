# mainKarabulutF.py
# Furkan Karabulut (fkarabu)
# Class: CSC 205-002
# Date: 03/03/2024

# This program is used to blend two PBM images together and create a new PBM image.

from pbmimage import PBMimage

MAX_PIXEL_VALUE = 255
def main():
    
    image1 = PBMimage('', '', -1, -1, -1, [])
    image2 = PBMimage('', '', -1, -1, -1, [])
    
    # # Ask the user for the 2 image filenames
    file1 = input("Enter input filename for image 1: ")
    image1.load_image(file1)
    
    
    file2 = input("Enter input filename for image 2: ")
    image2.load_image(file2)
    
    
    
    blended = blending_images(image1, image2)
    
    
    convert_to_bw = input("Convert the image to greyscale? (Enter 'yes' or 'no'): ")
    
    while convert_to_bw not in ['yes', 'no']:
        print("Invalid input. Please enter 'yes' or 'no'")
        convert_to_bw = input("Convert the image to greyscale? (Enter 'yes' or 'no'): ").lower()
        return

    if convert_to_bw == 'yes':
        converted_image = convert_to_BW(blended)
        converted_image.output_image('imageBW.pgm')
        print("Output file for blended image: imageBW.pgm")
        print(converted_image.comment)
        print(f"Type: {converted_image.ASCI}")
        print(f"Width: {converted_image.width} Height: {converted_image.height}")
    else:
        converted_image = blended
        converted_image.output_image('imageBlend.ppm')
        print("Output file for blended image: imageBlend.ppm")
        print(converted_image.comment)
        print(f"Type: {converted_image.ASCI}")
        print(f"Width: {converted_image.width} Height: {converted_image.height}")

    # converted_image = convert_to_BW(blended) if convert_to_bw == 'yes' else blended
    
    # converted_image.output_image('imageBlend.ppm')
    
    # print("Output file for blended image: imageBlend.ppm")
    # print(converted_image.comment)
    # print(f"Type: {converted_image.ASCI}")
    # print(f"Width: {converted_image.width} Height: {converted_image.height}")
    
    
    
    
    # print(PBMimage1.__str__())
    # print(PBMimage1.maxColor)
    # print(PBMimage1.width)
    # print(PBMimage1.height)
    # print(PBMimage1.comment)
    # print(PBMimage1.ASCI)
    
    # print(PBMimage1.pixels[0:10])
    
    

# Contain a function external of the class called blend_images whose 2 arguments are the names of
# the image objects to be blended. It should return an image object holding the blended image. Instead 
# of assuming a 50% / 50% blending ratio, prompt the user for the blending weight for the first image.
# Make sure that their input is a value between 0-100%. You can calculate the weight for the second
# image assuming a 100% total weight
def blending_images(PBMimage1, PBMimage2):
        
    while 1:
        weight1 = int(input("Enter blending weight of first image as a percent: "))
        if (weight1 < 0 or weight1 > 100):
            print("Invalid input. Please enter a value between 0-100")
            continue
        weight2 = 100 - weight1
        break
    
    weight1 = float(weight1 / 100)
    weight2 = float(weight2 / 100)
    
    # Check if the images are the same size
    min_width = min(PBMimage1.width, PBMimage2.width)
    min_height = min(PBMimage1.height, PBMimage2.height)
    
    # Initialize the list for the blended pixels
    blending_pixels = []

    # Adjust the loop to blend pixels based on the smallest dimensions
    for y in range(min_height):
        for x in range(min_width):
            index = (y * min_width + x) * 3  # Assuming 3 channels (R, G, B) per pixel
            r = int(PBMimage1.pixels[index] * weight1 + PBMimage2.pixels[index] * weight2)
            g = int(PBMimage1.pixels[index + 1] * weight1 + PBMimage2.pixels[index + 1] * weight2)
            b = int(PBMimage1.pixels[index + 2] * weight1 + PBMimage2.pixels[index + 2] * weight2)
            blending_pixels.extend([min(r, MAX_PIXEL_VALUE), min(g, MAX_PIXEL_VALUE), min(b, MAX_PIXEL_VALUE)])
    
    # Create a new PBMimage object for the blended image
    weight1 = weight1 * 100
    weight2 = weight2 * 100
    blended_image = PBMimage('P3', f"# blended image {weight1}%/{weight2}%", min_width, min_height, 255, blending_pixels)
    
    return blended_image
    
def convert_to_BW(blended_image):
    greyscale_pixels = []
    
    for i in range(0, len(blended_image.pixels), 3):
        # Apply the 30% red, 60% green, 10% blue weighting
        grey_value = int(blended_image.pixels[i] * 0.3 + blended_image.pixels[i+1] * 0.6 + blended_image.pixels[i+2] * 0.1)
        greyscale_pixels.append(grey_value)
    
    # Create a new PBMimage object for the greyscale image
    # Assuming greyscale images use P2 format and max color value of 255
    greyscale_image = PBMimage('P2', "# converted to greyscale", blended_image.width, blended_image.height, 255, greyscale_pixels)
    
    return greyscale_image
    
# Method to read the PBM image file
# if the user enters the wrong file name, the program should prompt the user again for the correct file name
# until the correct file name is entered
def entry_for_image(image_number):
    while True:
        file_name = input(f"Enter input filename for image {image_number}: ")
        image = PBMimage('', '', -1, -1, -1, [])
        try:
            image.load_image(file_name)
            return image  # Return the loaded image object upon success
        except FileNotFoundError:
            print(f"[Errno 2] No such file or directory: '{file_name}'")
    
    


if __name__ == "__main__":
    main()