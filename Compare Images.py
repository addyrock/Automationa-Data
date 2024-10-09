from selenium import webdriver
from PIL import Image, ImageChops

# Set up the Selenium WebDriver
driver = webdriver.Chrome()

# Open the web page you want to test
driver.get("http://10.20.10.137:800/Default")

# Capture a screenshot of the webpage
screenshot_path = r"C:\Users\arslan.arif\PycharmProjects\pythonProject2\HRMS_screenshot.png"
driver.save_screenshot(screenshot_path)

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
        img1 = img1.resize(img2.size, Image.LANCZOS)  # Use LANCZOS instead of ANTIALIAS

    # Compare the two images
    diff = ImageChops.difference(img1, img2)

    # If images are different, save the difference image
    if diff.getbbox():
        diff.save(diff_img_path)
        print(f"Images are different. Saved difference image at: {diff_img_path}")
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

