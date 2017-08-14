
import time, sys, getopt
import Adafruit_SSD1306
import Image
import ImageDraw
import ImageFont

# Beaglebone Black pin configuration:
RST = 'P9_15'

# 128x64 display with hardware I2C:
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3D)

# Initialize library.
disp.begin()

# Clear display.
disp.clear()
disp.display()

# Create blank image for drawing. Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))
top = 2

def main(mystr, fsize):
  #print mystr, fsize
  fsize = int(fsize)
  disp.clear()
  disp.display()

  # Get drawing object to draw on image.
  draw = ImageDraw.Draw(image)

  # Draw a black filled box to clear the image.
  draw.rectangle((0,0,width,height), outline=0, fill=0)

  '''# Read the sys arguments
  fsize = 36
  mystr = 'Lamprey'
  argv = sys.argv[1:]

  opts, args = getopt.getopt(argv,"f:s:t:")
  for opt, arg in opts:
    if opt in ("-f", "--font"):
       font=arg
    elif opt in ("-s", "--size"):
       fsize = int(arg)
    elif opt in ("-t", "--text"):
       mystr = arg
  '''

  font = ImageFont.truetype(filename='/usr/share/fonts/truetype/computer_pixel-7.ttf', size=fsize)
  if font == 'modern':
	font = ImageFont.truetype(filename='/usr/share/fonts/truetype/modern_lcd-7.ttf', size=fsize)
  if font == 'invaders':
	font = ImageFont.truetype(filename='/usr/share/fonts/truetype/pixel_invaders.ttf', size=fsize)

  # Load default font.
  #font = ImageFont.load_default() 

  if mystr == 'Lamprey':
    # Write two lines of text.
    draw.text((20, top),    'The',  font=font, fill=255)
    draw.text((20, top+20), 'Lamprey', font=font, fill=255)
  else:
    w,h = draw.textsize(mystr)
    draw.text(((width-w)/2-fsize/2, (height-h)/2-fsize/3), mystr, font=font, fill=255)

  # Display image
  disp.image(image)
  disp.display()

if __name__=="__main__":
  sas=len(sys.argv)
  #Defaults are set here
  if sas>1:
    mystr=sys.argv[1]
  else:
    mystr='Lamprey'

  if sas>2:
    fontsize=sys.argv[2]
  else:
    fontsize=36
  main(mystr, fontsize)
