# PBMImageKarabulutF.py
# Furkan Karabulut (fkarabu)
# Class: CSC 205-002
# Date: 03/03/2024

# This class is used to craete a PBM image object and manipulate it.
# contained in a separate source code file from our main program. Our main
# program should contain the code to instantiate the PBMimage objects and ask the user for the 2 image
# filenames used to create the blended image.

class PBMimage:
    
    # Constructor
    def __init__(self, ASCI, comment, width, height, maxColor, pixels):
        self.__ASCI = ASCI
        self.__comment = comment
        self.__width = width
        self.__height = height
        self.__maxColor = maxColor
        self.__pixels = pixels
        
    # Accessor methods
    @property
    def ASCI(self):
        return self.__ASCI
    
    @property
    def comment(self):
        return self.__comment
    
    @property
    def width(self):
        return self.__width
    
    @property
    def height(self):
        return self.__height
    
    @property
    def maxColor(self):
        return self.__maxColor
    
    @property
    def pixels(self):
        return self.__pixels
    
    # Setter
    @ASCI.setter
    def ASCI(self, ASCI):
        self.__ASCI = ASCI
    
    @comment.setter
    def comment(self, comment):
        self.__comment = comment
        


    @pixels.setter
    def pixels(self, pixels):
        self.__pixels = pixels
        
    @maxColor.setter
    def maxColor(self, maxColor):
        self.__maxColor = maxColor
    
    @width.setter
    def width(self, width):
        self.__width = width
    
    @height.setter
    def height(self, height):
        self.__height = height
    
    
    # Method to read the PBM image file
    # method that is passed the name of the image file in which the image is stored. It should
    # open the file, read in the image data, store the data in the object and close the file. While the image
    # comment is often the second line of the file, it could be any of the first 4 lines of the file. Your code
    # should recognize the comment to prevent the image from being read in improperly or an exception
    # from being thrown. 
    # Method to read the PBM image file
    def load_image(self, fileName):
        try:
            with open(fileName, 'r') as file:
                # Temporary storage for the first four lines
                headLines = [file.readline().strip() for _ in range(4)]
                
                # Initialize variables for the header information
                self.comment = None
                size_detected = False

                for line in headLines:
                    if line.startswith('#'):
                        self.comment = line  # Comment line
                    elif line.startswith('P'):
                        self.magic_number = line  # Magic number (P3 for color images)
                    elif ' ' in line and not size_detected:  # Detects size line, ensures it's only done once
                        size = line.split()
                        self.width, self.height = int(size[0]), int(size[1])
                        size_detected = True
                    else:
                        # print(line)
                        self.maxColor = int(line)
                        

                # Ensuring we have read the magic number and dimensions
                if not self.magic_number or not size_detected:
                    raise ValueError("Invalid PBM file format.")

                # Reading pixel data
                pixels_data = file.read().split()
                self.pixels = [int(pixel) for pixel in pixels_data]
                
        except FileNotFoundError:
            print(f"[Errno 2] No such file or directory: {fileName}")
    
    # An output_image method that is passed the name of the file into which the image data should be
    # dumped. This method should open the file, write the image data to the file, and close the file. Based on
    # the image type, it should accommodate both P2 and P3 image types.
    def output_image(self, filename):
        try:
            with open(filename, 'w') as file:
                # Write the magic number and the comment if it exists
                file.write(f"{self.ASCI}\n")
                if self.comment:
                    file.write(f"{self.comment}\n")
                
                # Write the width, height, and max color value
                file.write(f"{self.width} {self.height}\n")
                file.write(f"{self.maxColor}\n")
                
                # Writing pixel data based on the image type
                if self.ASCI == 'P3':  # Color image
                    for i in range(0, len(self.pixels), 3):
                        file.write(f"{self.pixels[i]}\n{self.pixels[i+1]}\n{self.pixels[i+2]}\n")
                elif self.ASCI == 'P2':  # Grayscale image
                    for i in range(len(self.pixels)):
                        file.write(f"{self.pixels[i]}\n")
        except Exception as e:
            print(f"An error occurred while writing the image file: {e}")
    
    # method to override the class method to output the image comment, magic number,
    # width, and height
    def __str__(self):
        # Initialize the base string with the comment if it exists
        str_representation = f"{self.comment}\n" if self.comment else ""
        
        # Add the magic number, width, and height to the string
        str_representation += f"Type: {self.magic_number}\n"
        str_representation += f"Width: {self.width} Height: {self.height}"
        
        return str_representation
        