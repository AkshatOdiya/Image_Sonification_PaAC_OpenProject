# Image_Sonification_PaAC_OpenProject
This repository include the code followed for image sonification and use of tools like sonoUno(Web version is also available)/Photosounder along with python and libraries like openCV or PIL.

# Part1:

It contains how pixel values of an image can be extracted for all three R,G,B column in the csv file.


# Part2:

The file "Mapping_and_Generating_Sound" (sound file: "image_sound_short.wav"),  contains code that is based on:
1. Pixel Brightness is used to deteremine the frequency of the generated sound, where frequency of the sound is directly proportional to brightness of the pixel.
2. Brightness value is taken as average of the pixel values(R,G,B).
3. The brightness value (range from 0 to 255) is mapped to frequency range 200 to 2000 Hz by linear mapping along with noramlisation of brightness value.
4. The computed frequency is used to generate a sine wave this creates a sound tone lasting desired duration.
  
The file "Mapping_and_Generating_Sound_raw_rgb" (sound file: "image_sound_raw_rgb.wav") contains code for mapping the the raw values of R,G,B with the sound parameters such that:

i) R(red) -----------> Frequency

ii) G(Green) ------------> Volume

iii) B(Blue) ------------> Duration

Pixels are processed directly without combining or averaging.

# Part3:

This part contains the python file ('cli_tool_to_sonify.py') which can be used as a CLI Tool to convert the pngs in to the sound with two options (brightness based or RGB values based), this python file uses two functions corresponding to how would you like to sonify the image or those two options.
The File can be run in cmd with command [python  python .\cli_tool_to_sonify.py]. It takes the images path you want to sonify. The example usage is shown below in the image.

![Screenshot 2024-12-25 142138](https://github.com/user-attachments/assets/891762ee-d7fb-4176-a41e-c23644f7089c)


