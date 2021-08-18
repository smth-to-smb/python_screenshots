import os
import config_parsing

# Dictionary with settings from a JSON file
settings = config_parsing.config_parsing()

# Processing images
# Directory with images
imagesFolderName = settings["imagesfoldername"]

# Image naming pattern
imagesNamingPattern = settings["imagesnamingpattern"]

# Image source directory
screenshotSourceFolderPath = settings["screenshotsourcefolderpath"]

# Destination directory for images
destinationFolderPath = settings["imagesfolderpath"] + imagesFolderName + '/'

# Trimmed path for inserting filename to a Markdown file
fileNamePath = 'images/' + imagesFolderName + '/'

# Iterator of the folder with screenshots
sourcefolderscan = os.listdir(screenshotSourceFolderPath)

# Итератор папки файлов для переноса
#destinationfolderscan = os.listdir(destinationfolderpath)

destinationfolderscan = 0

# Checking whether the destination path exists. If not, it can be created
try:
    destinationfolderscan = os.listdir(destinationFolderPath)
except FileNotFoundError:
    print("Folder \"" + imagesFolderName + "\" does not exist. Do you want to create it (Y/N)?"+"\n")
    createdestinationfolder = input("\n")
    if createdestinationfolder in ("Y", "y"):
        os.makedirs(destinationFolderPath)
        print("Folder \"" + imagesFolderName + "\" has been created.")
        print("\n")
        destinationfolderscan = os.listdir(destinationFolderPath)
    if createdestinationfolder in ("N", "n"):
        print("Exiting the script.")
        raise exit()

# List of screenshot files which should be moved
filestobemoved = []

# a. Searching for files in the folder iterator
# b. Appending them to the list of files
for i in sourcefolderscan:
    if i.find('Screenshot') != -1:
        filestobemoved.append(i)

# Exiting the script if no new screenshots were found
if len(filestobemoved) == 0:
    print("No new screenshots were found. Exiting the script")
    raise SystemExit

# 2. Defining the index for a screenshot file

# The biggest index variable
destinationcounter = 0

# Searching for the biggest index in the file list
for k in destinationfolderscan:
    if k.find(imagesNamingPattern) != -1:
        begin = int(k.rindex("_")) + 1 # Index begin
        end = int(len(k) - 4) # Index end
        number = int(k[begin:end])
        if number > destinationcounter: # Checking for the current sourcefoldercounter index
            destinationcounter = number # Assigning the biggest index to sourcefoldercounter

# Incrementing the index
destinationcounter += 1

# Entering a screenshot caption
figure_name = input("Enter the caption name (s - skip): ")
skiplist = ['s', 'S']

# Assigning the default name to the screenshot
if figure_name in skiplist:
    figure_name = settings["defaultcaptionnamingpattern"]

# Returning a Markdown-formatted link to the screenshot file
for l in filestobemoved:
    for m in sourcefolderscan:
        if l == m: # Filename in the source folder equals the filename in the destination folder
            os.replace(screenshotSourceFolderPath + l,
                       destinationFolderPath
                       + imagesNamingPattern
                       + str(destinationcounter)
                       + ".png")
            print()
            print("!["+figure_name+"](" + destinationFolderPath + imagesNamingPattern + str(destinationcounter)+".png)")
            destinationcounter += 1
