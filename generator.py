from PIL import Image
import os

def clear_temp():
    folder = './temp'
    for temp in os.listdir(folder):
        os.remove(os.path.join(folder, temp))
    print('\ntemporary folder successfully cleaned!\n')

# function to generate a wallpaper for a background and a logo
def generate_wallpaper(bg, logo):
    bg_width, bg_heigth = bg.size
    l_width, l_heigth = logo.size
    if logo.format == 'PNG':
        bg.paste(logo, ((bg_width - l_width) // 2, (bg_heigth - l_heigth) // 2 ), logo)
    else:
        bg.paste(logo, ((bg_width - l_width) // 2, (bg_heigth - l_heigth) // 2 ))
    bg_name = os.path.basename(bg.filename)
    bg_name = os.path.splitext(bg_name)[0]
    logo_name = os.path.basename(logo.filename)
    filename = bg_name + '_' + logo_name
    bg.save('./wallpapers/' + filename)
    print('NEW ' + filename + ' WALLPAPER GENERATED!')

def main():
    print('\n-----------------------WALLPAPER GENERATOR-----------------------\n')

    for bg_file in os.listdir('./backgrounds'):
        for logo_file in os.listdir('./logos'):
            background = Image.open('./backgrounds/' + str(bg_file), 'r')
            bg_width, bg_heigth = background.size
            logo = Image.open('./logos/' + str(logo_file), 'r')
            l_width, l_heigth = logo.size
            # crop logo if necessary
            if l_heigth >= bg_heigth:
                logo.thumbnail((350, 350))
                logo.save('./temp/' + os.path.basename(logo.filename))
                temp = Image.open('./temp/' + os.path.basename(logo.filename), 'r')
                generate_wallpaper(background, temp)              
            else:
                generate_wallpaper(background, logo)

    # in case you want to keep the cropped images, stop calling this function and check the temp folder
    clear_temp()

if __name__ == "__main__":
    main()