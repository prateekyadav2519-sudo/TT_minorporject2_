Here’s a clean, professional **README.md** you can directly use on your GitHub repository. It’s written in a technical-training style and clearly explains all constraints of **Minor Project 2**.

---

# ASCII Image Generator in Python (Minor Project – 2)

## Project Title

**Errling Halland Image Creation Using ASCII Characters and Loops in Python**

## Project Type

**Technical Training – Minor Project 2**

## Project Description

This project demonstrates how an image can be generated and displayed using **ASCII characters** in the terminal by processing raw image data with **pure Python logic**.

The program reads a **24-bit BMP image file**, extracts pixel information, converts it into grayscale intensity, and maps those values to ASCII characters using **for-loops and conditional statements only**.

> No external libraries
> No Pillow (PIL)
> No image converters
> Only core Python and logical constructs

---

## Technologies Used

* **Programming Language:** Python
* **Concepts Applied:**

  * For loops
  * While loops
  * Conditional statements
  * File handling
  * Binary data processing
  * ASCII character mapping

---

## Input Requirements

* Image must be:

  * **BMP format**
  * **24-bit (True Color)**
  * Uncompressed
* The BMP file should be placed in the same directory as the Python script.

---

## Working Principle

1. Read the BMP file in **binary mode**
2. Skip the BMP header and extract raw pixel data
3. Convert RGB values to grayscale intensity
4. Map intensity values to ASCII characters
5. Print the ASCII image directly in the **terminal**

---

## Constraints Followed

✔ No use of `Pillow`, `OpenCV`, or any image libraries
✔ No built-in image processing functions
✔ Only loops, conditionals, and basic Python
✔ Output strictly displayed in terminal
✔ Manual ASCII mapping logic



## Structure

```
 ASCII-Image-Generator
 ┣ ascii_image.py
 ┣ input.bmp
 ┗ README.md
```

## Output

* Displays an **ASCII representation of the image** in the terminal
* Uses characters like `*` to represent different pixel intensities

---

## Learning Outcomes

* Understanding low-level image data
* Working with binary files in Python
* Applying loops and conditionals effectively
* ASCII art generation logic
* Memory-efficient image handling

---

## Author

**Prateek Yadav**
Technical Training – Minor Project 2

---

