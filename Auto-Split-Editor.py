# Auto-Split-Editor
# Nick Furlo aka earllgray
# August 2021
# The GNU General Public License v3.0
import os
import shutil


# Start menu, might add more functionality later.
def start():
    if not os.path.exists('images'):
        print("images folder does not exist, creating one...")
        os.makedirs('images')
    print("Make sure split images from your autos-plitter have been copied to the 'images' folder.")
    choice = input("What would you like to do? \n1. Change Thresholds\n")
    if int(choice) == 1:
        changeThresholds()
    else:
        print("nope")
        start()


# Given a filename and new threshold, this function will generate a filename with the new threshold value.
def generateThreshold(filename, threshold):
    if int(threshold) >= 100:
        print("Enter an integer less than 100")
        return 1
    # gets index values for #s after the decimal place. These indexes are used to replace that portion of text with the new threshold.
    lindex = filename.find("(") + 3
    rindex = filename.find(")") - 1
    newFilename = filename[0:lindex] + threshold + filename[rindex + 1:]
    return newFilename


# Started by start selection. This function gets input from the user and calls generateThreshold. It then use shutil to rename the file. It iterates through all files in the images folder.
def changeThresholds():
    print("\nEnter threshold values as integers, s to skip, or q to quit. Ex: 80% = 80")
    for filename in os.listdir("images"):
        fullPath = os.path.join("images", filename)
        if os.path.isfile(fullPath):
            print("What threshold do you want for this image?\n" + fullPath[7:])
            threshold = input()
            if threshold.lower() == "s":
                print("Skipped.\n")
            elif threshold.lower() == "q":
                return print("Quitting!")
            else:
                newFilename = generateThreshold(filename, threshold)
                if isinstance(newFilename, int):
                    return print("error generating filename.")
                print("New Filename: " + newFilename + "\n")
                newFull = fullPath[0:7] + newFilename
                shutil.move(fullPath, newFull)


start()
