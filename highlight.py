from PIL import Image, ImageDraw
import xml.etree.ElementTree as ET
import re
import os

data_path = "./Data/"
image_path = "./Images/"
output_path = "./Output/"

#find leaf nodes and corresponding corners given XML and (empty) corner list
def find_leaf_corners(el, corners_list):
    if len(list(el)) == 0:  # Check if the element has no children
        format_str = el.attrib["bounds"]
        bounds_li = [int(num) for num in re.findall(r'\d+', format_str)]
        left, top, right, bottom = bounds_li[0], bounds_li[1], bounds_li[2], bounds_li[3]
        corners_list.append((left, top, right, bottom))
    else:
        for child in el:
            find_leaf_corners(child, corners_list)

#highlight image 
def highlight_image(img, corners_list):
    new = Image.new('RGBA', img.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(new)

    for corners in corners_list:
        draw.rectangle([(corners[0], corners[1]), (corners[2], corners[3])], outline="yellow", width=4, fill=(255, 255, 0, 30))
        out = Image.alpha_composite(img, new)
    return out
        
def save_image(img_out, out_path, img_name):
    file_path = os.path.join(out_path, img_name + "_out.png")
    img_out.save(file_path, format='PNG')

def main():
    data_list = os.listdir(data_path)

    for f in data_list:
        img_name = f[:-4]+".png"

        #Each XML file ought to have a corresponding image with the same file name
        try:
            img = Image.open(image_path + img_name).convert("RGBA")
        except:
            print(f"No corresponding image file for file {f}")
            continue

        #XML file validity check
        try:
            tree = ET.parse(data_path + f)
        except:
            print(f"XML parsing error on file {f}")
            continue
        
        
        corners_list = []
        root = tree.getroot()
        find_leaf_corners(root, corners_list)

        if corners_list:
            out = highlight_image(img, corners_list)
        else:
            print(f"No leaf nodes found in XML file {f}")

        save_image(out, output_path, img_name)
            
if __name__ == "__main__":
    main()