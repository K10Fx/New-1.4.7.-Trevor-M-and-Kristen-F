import PIL
import matplotlib.pyplot as plt
import os.path  
import PIL.ImageDraw

def frame(original_image, percent_of_side):
    width, height = original_image.size
    border = int(percent_of_side*min(width, height))
    frame_mask=PIL.Image.new('RGBA', (width, height), (0, 0, 0, 0))
    drawing_layer = PIL.ImageDraw.Draw(frame_mask)
    
    drawing_layer.polygon([(15,15),(15,15),
                            (15,15),(15,15)],
                            fill=(127,0,127,255))
    drawing_layer.polygon([(15,border),(width,border),
                            (width,height-border),(15,height-border)],
                            fill=(127,0,127,255))
    
    result = PIL.Image.new('RGBA', original_image.size, (0,0,128,255))
    result.paste(original_image, (0,0), mask=frame_mask)
    return result
    
    
def get_images(directory=None):
    if directory == None:
        directory = os.getcwd()
    image_list = []
    file_list = []
    directory_list = os.listdir(directory)
    for entry in directory_list:
        absolute_filename = os.path.join(directory, entry)
        try:
            image = PIL.Image.open(absolute_filename)
            file_list += [entry]
            image_list += [image]
        except IOError:
            pass
    return image_list, file_list


def frame_all_images(directory=None):
    if directory==None:
        directory = os.getcwd()
    new_directory = os.path.join(directory, 'familyphotos1')
    try:
        os.mkdir(new_directory)
    except OSError:
        pass
    image_list, file_list = get_images(directory)
    for n in range(len(image_list)):
        filename, filetype = file_list[n].split('.')
        new_image = frame(image_list[n],.30)
        new_image_filename = os.path.join(new_directory, filename + '.png')
        new_image.save(new_image_filename) 