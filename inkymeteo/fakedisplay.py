from font_fredoka_one import FredokaOne
#from inky.auto import auto
from PIL import Image, ImageDraw, ImageFont

import os


class Display:

    def __init__(self):
        image = self.create_new_inky_image()


    def create_new_inky_image(self):
        PATH = os.path.dirname(__file__)

        #inky_display = auto(ask_user=True, verbose=True)
        #w, h = inky_display.resolution
        #inky_display.set_border(inky_display.BLACK)

        
        #image = Image.open(os.path.join(PATH, "resources/backdrop.png")).resize(250,122)
        image = Image.new('RGB', (250, 122), color = 'black')
        #breakpoint()
        # draw object
        draw = ImageDraw.Draw(image)
        #draw.line((69, 36, 69, 81))
        draw.line((0, 31, 250, 31))
        draw.line((166,0, 166, 122))      # Vertical line
        image.save("coucou.png")
        

if __name__ == "__main__":
    display = Display()




    # # Load our icon files and generate masks
    # for icon in glob.glob(os.path.join(PATH, "resources/icon-*.png")):
    #     icon_name = icon.split("icon-")[1].replace(".png", "")
    #     icon_image = Image.open(icon)
    #     icons[icon_name] = icon_image
    #     masks[icon_name] = create_mask(icon_image)

    # # Load the FredokaOne font
    # font = ImageFont.truetype(FredokaOne, 22)
    # Draw lines to frame the weather data
    # draw.line((69, 36, 69, 81))       # Vertical line
    # draw.line((31, 35, 184, 35))      # Horizontal top line
    # draw.line((69, 58, 174, 58))      # Horizontal middle line
    # draw.line((169, 58, 169, 58), 2)  # Red seaweed pixel :D

    # Write text with weather values to the canvas
    # datetime = time.strftime("%d/%m %H:%M")
    # draw.text((36, 12), datetime, inky_display.WHITE, font=font)
    # draw.text((72, 34), "T", inky_display.WHITE, font=font)
    # draw.text((92, 34), u"{}°".format(temperature), inky_display.WHITE if temperature < WARNING_TEMP else inky_display.RED, font=font)
    # draw.text((72, 58), "P", inky_display.WHITE, font=font)
    # draw.text((92, 58), "{}".format(pressure), inky_display.WHITE, font=font)

    # # Draw the current weather icon over the backdrop
    # if weather_icon is not None:
    #     img.paste(icons[weather_icon], (28, 36), masks[weather_icon])
    # else:
    #     draw.text((28, 36), "?", inky_display.RED, font=font)
    # # Display the weather data on Inky pHAT
    # inky_display.set_image(img)
    # inky_display.show()