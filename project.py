import os
import sys

# ==========================================
# 1. SETTINGS & CONSTANTS
# ==========================================
ASCII_CHARS = "*"

INPUT_FILENAME = "output.bmp"  # You MUST save your image as a 24-bit BMP file first!
OUTPUT_WIDTH = 150           # Width of the ASCII art in characters

# ==========================================
# 2. CORE LOGIC FUNCTIONS (NO LIBRARIES)
# ==========================================

def read_bmp_data(filepath):
    """
    Reads a 24-bit BMP file manually byte-by-byte using file seeking.
    Returns: width, height, and a list of lists containing (r, g, b) tuples.
    """
    if not os.path.exists(filepath):
        print(f"Error: '{filepath}' not found. Please convert your image to .bmp format!")
        sys.exit(1)

    with open(filepath, 'rb') as f:
        # --- Parse BMP Header Manually ---
        # BMP Header starts with 'BM'.
        # Width is at byte 18 (4 bytes), Height is at byte 22 (4 bytes).
        f.seek(18)
        width = int.from_bytes(f.read(4), 'little')
        height = int.from_bytes(f.read(4), 'little')

        f.seek(28)
        bits_per_pixel = int.from_bytes(f.read(2), 'little')

        if bits_per_pixel != 24:
            print("Error: Please save the image as a '24-bit Bitmap' (BMP).")
            sys.exit(1)

        # Pixel data usually starts at offset 54
        f.seek(10)
        data_offset = int.from_bytes(f.read(4), 'little')

        # --- Calculate Padding ---
        # BMP rows are padded to be a multiple of 4 bytes
        padding = (4 - (width * 3) % 4) % 4

        pixels = []
        f.seek(data_offset)

        # --- Manual Loop to Read Pixels ---
        # Note: BMP stores pixels Bottom-to-Top, so we read normally then reverse later
        for y in range(height):
            row = []
            for x in range(width):
                # Read 3 bytes: Blue, Green, Red (BMP stores as BGR)
                b = int.from_bytes(f.read(1), 'little')
                g = int.from_bytes(f.read(1), 'little')
                r = int.from_bytes(f.read(1), 'little')
                row.append((r, g, b))

            # Skip the padding bytes at the end of the row
            f.read(padding)
            pixels.append(row)

    # Reverse list because BMP is stored upside down
    return width, height, pixels[::-1]

def resize_pixels(pixels, old_w, old_h, new_w):
    """
    Manually resizes the image grid using 'Nearest Neighbor' logic.
    We skip pixels to make the image smaller.
    """
    # Calculate aspect ratio (terminal characters are roughly 2x as tall as wide, so we adjust)
    aspect_ratio = old_h / old_w
    new_h = int(new_w * aspect_ratio * 0.55)

    resized = []

    # Calculate step size (how many pixels to jump)
    step_x = old_w / new_w
    step_y = old_h / new_h

    # --- Nested Loops for Resizing ---
    for y in range(new_h):
        new_row = []
        # Find the corresponding Y logic in the original image
        src_y = int(y * step_y)
        # Clamp to bounds
        src_y = min(src_y, old_h - 1)

        for x in range(new_w):
            # Find the corresponding X logic in the original image
            src_x = int(x * step_x)
            src_x = min(src_x, old_w - 1)

            pixel = pixels[src_y][src_x]
            new_row.append(pixel)
        resized.append(new_row)

    return resized, new_h

def enhance_color_manual(r, g, b, factor=1.5):
    """
    Manually increases saturation/pop without 'ImageEnhance'.
    Simple logic: move values further away from the average.
    """
    # Clamp values between 0 and 255
    def clamp(val):
        return max(0, min(255, int(val)))

    # Calculate average gray
    avg = (r + g + b) / 3

    # Apply logic: new_color = avg + (old_color - avg) * factor
    new_r = clamp(avg + (r - avg) * factor)
    new_g = clamp(avg + (g - avg) * factor)
    new_b = clamp(avg + (b - avg) * factor)

    return new_r, new_g, new_b

def get_ansi_color_string(r, g, b, char):
    """Returns the character wrapped in ANSI escape codes for color."""
    return f"\033[38;2;{r};{g};{b}m{char}\033[0m"

# ==========================================
# 3. MAIN EXECUTION
# ==========================================
def main():
    print(f"Reading raw binary data from {INPUT_FILENAME}...")

    # 1. Read the raw bytes manually
    w, h, raw_pixels = read_bmp_data(INPUT_FILENAME)
    print(f"Original Image: {w}x{h} pixels")

    # 2. Resize using logic loops
    print(f"Resizing to width {OUTPUT_WIDTH}...")
    resized_pixels, new_h = resize_pixels(raw_pixels, w, h, OUTPUT_WIDTH)

    # 3. Generate ASCII
    ascii_art = ""

    for row in resized_pixels:
        for (r, g, b) in row:
            # Enhance color manually (optional innovation)
            r, g, b = enhance_color_manual(r, g, b)

            # Calculate brightness for character selection
            char="*"


            ascii_art += get_ansi_color_string(r, g, b, char)
        ascii_art += "\n"

    # 4. Print Result
    print(ascii_art)

if __name__ == "__main__":
    main()