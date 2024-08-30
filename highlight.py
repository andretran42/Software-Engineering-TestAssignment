from PIL import Image, ImageDraw
import xml.etree.ElementTree as ET


image = Image.open('./Images/com.apalon.ringtones.png')

image = image.convert("RGBA")
new = Image.new('RGBA', image.size, (255, 255, 255, 0))

draw = ImageDraw.Draw(new)

# Define the area to highlight (a rectangle in this example)
left, top, right, bottom = 0, 96, 224, 320

# Draw a rectangle over the area (with a semi-transparent fill and a solid border)
draw.rectangle([(left, top), (right, bottom)], outline="red", width=5, fill=(255, 0, 0, 40))

out = Image.alpha_composite(image, new)
# Save or show the result
out.show()

