# %%
import cv2
from pydub.generators import Sine
from pydub import AudioSegment
import numpy as np
from tqdm import tqdm

# %%
def Brightness_based_sound(image, tone_duration=50, block_size=16, max_duration=15000):
    height, width, _ = image.shape
    sound = AudioSegment.silent(duration=0)  # Start with silent audio
    total_tones = max_duration // tone_duration  # Max number of tones

    # Downsample image by processing blocks of pixels
    row_step = max(1, height // total_tones)

    for i in tqdm(range(0, height, row_step), desc="Processing rows", unit="row"):
        for j in range(0, width, block_size):
            block = image[i:i+row_step, j:j+block_size]
            average_pixel = np.mean(block, axis=(0, 1))  # Taking Average of RGB values
            brightness = int(np.mean(average_pixel))
            frequency = 200 + (brightness / 255) * 1800  # Scale brightness to frequency

            # A sine wave at the mapped frequency
            tone = Sine(frequency).to_audio_segment(duration=tone_duration)

            # Adding tone to the overall sound
            sound += tone

            # Stop if we exceed max_duration
            if len(sound) >= max_duration:
                break

    return sound[:max_duration]  # Trim the sound to max_duration


# %%
def pixel_values_based_sound(image, base_frequency=200, max_frequency=2000, block_size=16, max_duration=15000):
    height, width, _ = image.shape
    sound = AudioSegment.silent(duration=0)  # Start with silent audio
    total_tones = max_duration // 50  # Estimate total tones based on ~50ms per tone
    row_step = max(1, height // total_tones)

    for i in tqdm(range(0, height, row_step), desc="Processing rows", unit="row"):
        for j in range(0, width, block_size):
            # Use raw R, G, B values from the current pixel or block
            pixel = image[i, j]

            # Extract R, G, B components
            red, green, blue = pixel

            # Map R (Red) to frequency
            frequency = base_frequency + (red / 255) * (max_frequency - base_frequency)

            # Map G (Green) to volume
            volume = int((green / 255) * 10) - 5  # Scale volume to [-5dB, 5dB]

            # Map B (Blue) to duration
            tone_duration = 20 + (blue / 255) * 80  # Scale duration to 20-100ms

            tone = Sine(frequency).to_audio_segment(duration=tone_duration).apply_gain(volume)

            # Mix the tone into the overall sound
            sound += tone

            # Apply constraint, Stop if the maximum duration is reached
            if len(sound) >= max_duration:
                break

    return sound[:max_duration]  # This trim the sound to the maximum allowed duration


# %%
print("How would you like your sound to be generated?")
print("1. Pixel values (RGB) Based")
print("2. Brightness Based")

try:
    l = int(input("Enter the option number (1 or 2): "))
    path = input("Enter the path of the PNG file you want to sonify: ")
    image = cv2.imread(path)

    if image is None:
        print("Error: Could not read the image. Please check the path and file format.")
        exit()

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB
    image = cv2.resize(image, (100, 100))  # Resize for processing

    print("Generating sound from the image...")
    if l == 1:
        sound = Brightness_based_sound(image)
        sound.export("brightness_based_image_sound.wav", format="wav")
        print("Sound generated and saved as 'brightness_based_image_sound.wav'.")
    elif l == 2:
        sound = pixel_values_based_sound(image)
        sound.export("pixel_values_based_image_sound.wav", format="wav")
        print("Sound generated and saved as 'pixel_values_based_image_sound.wav'.")
    else:
        print("Invalid number.")
except ValueError:
    print("Error: Please enter a valid number.")

