from selenium import webdriver
from PIL import Image, ImageChops

# Set up the Selenium WebDriver
driver = webdriver.Chrome()

# Open the web page you want to test
driver.get("http://10.20.10.137:800/Default")

# Capture a screenshot of the webpage
screenshot_path = r"C:\Users\arslan.arif\PycharmProjects\pythonProject2\HRMS_screenshot.png"
driver.save_screenshot(screenshot_path)

def highlight_differences(img1, img2):
    # Create a new image to hold the highlighted differences
    diff_img = Image.new("RGB", img1.size)

    # Iterate over the pixels to find differences
    for x in range(img1.width):
        for y in range(img1.height):
            if img1.getpixel((x, y)) != img2.getpixel((x, y)):
                # Highlight the difference in red
                diff_img.putpixel((x, y), (255, 0, 0))  # Red color for differences
            else:
                # Keep the original pixel where they are the same
                diff_img.putpixel((x, y), img1.getpixel((x, y)))

    return diff_img

def compare_images(img1_path, img2_path, diff_img_path):
    # Open both images
    img1 = Image.open(img1_path)
    img2 = Image.open(img2_path)

    # Convert both images to the same mode
    img1 = img1.convert("RGB")
    img2 = img2.convert("RGB")

    # Resize img1 to img2's size if they are different
    if img1.size != img2.size:
        print(f"Resizing img1 from {img1.size} to {img2.size}")
        img1 = img1.resize(img2.size, Image.LANCZOS)

    # Compare the two images
    diff = ImageChops.difference(img1, img2)

    # If images are different, highlight the differences
    if diff.getbbox():
        highlighted_diff = highlight_differences(img1, img2)
        highlighted_diff.save(diff_img_path)
        print(f"Images are different. Highlighted differences saved at: {diff_img_path}")
    else:
        print("Images are identical.")

# Paths to your images
webpage_screenshot_path = r"C:\Users\arslan.arif\PycharmProjects\pythonProject2\HRMS_screenshot.png"
figma_design_path = r"D:\Arslan testing Data\Capture.JPG"  # Figma design exported as an image
difference_image_path = r"D:\Arslan testing Data\difference.png"  # Save difference as a new image file

# Compare the images
compare_images(webpage_screenshot_path, figma_design_path, difference_image_path)

# Close the browser
driver.quit()
