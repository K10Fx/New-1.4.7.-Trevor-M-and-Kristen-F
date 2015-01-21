import PIL
import matplotlib.pyplot as plt
import os.path  
import PIL.ImageDraw

def frame(original_image, percent_of_side):
    '''Frames the original images
    It returns a new PIL.image with a frame around it
    percent_of_side is positive, but less than 1
    '''
    #set the border size of the new images
    width, height = original_image.size
    border = int(percent_of_side*min(width, height))
    
    #create an opaque mask to cover the pictures' edges
    frame_mask=PIL.Image.new('RGBA', (width, height), (0, 0, 0, 0))
    drawing_layer = PIL.ImageDraw.Draw(frame_mask)
    
    #create a rectangular border around the images
    drawing_layer.polygon([(15,15),(15,15),
                            (15,15),(15,15)],
                            fill=(127,0,127,255))
    drawing_layer.polygon([(15,border),(width,border),
                            (width,height-border),(15,height-border)],
                            fill=(127,0,127,255))
    drawing_layer.polygon([(border, 15),(border,width),
                            (width, height-border),(height-border, 15)],
                            fill=(127,0,127,255))
                            
    #return the new images with an opaque navy blue border
    result = PIL.Image.new('RGBA', original_image.size, (25,0,135,255))
    result.paste(original_image, (0,0), mask=frame_mask)
    return result
    
    
def get_images(directory=None):
    '''Return new PIL.Image for every picture under this directory
    When there isn't a designated directory, then it is stored in the most recent one
    Returns two lists containing the images and their files, respectively
    '''
    #If the directory isn't specified, use the current one
    if directory == None:
        directory = os.getcwd()
    #Aggregators
    image_list = []
    file_list = []
    #Obtain a list of files
    directory_list = os.listdir(directory)
    for entry in directory_list:
        absolute_filename = os.path.join(directory, entry)
        try:
            image = PIL.Image.open(absolute_filename)
            file_list += [entry]
            image_list += [image]
        #Ignore errors
        except IOError:
            pass
    return image_list, file_list


def frame_all_images(directory=None):
    '''Alters all images in the directory to have a border rather than just one
    Also uses the most recent directory if one is not designated
    Puts the new images in the subdirectory/ folder 'familyphotos1'
    Any new pictures created are type .png instead of .jpg
    '''
    #Creates the new subdirectory/ folder that the pictures are filed under
    if directory==None:
        directory = os.getcwd()
    new_directory = os.path.join(directory, 'familyphotos2')
    try:
        os.mkdir(new_directory)
    #Ignore errors    
    except OSError:
        pass
    #Load all of the images into their respective lists mentioned earlier    
    image_list, file_list = get_images(directory)
    #Going through the length of the lists, it saves the new images
    for n in range(len(image_list)):
        filename, filetype = file_list[n].split('.')
        #Frame the borders
        new_image = frame(image_list[n],.10)
        #Convert all images to .png
        new_image_filename = os.path.join(new_directory, filename + '.png')
        new_image.save(new_image_filename) 