import cv2
import pytesseract
import numpy as np

# Set Tesseract path (adjust for your system)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def preprocess_image(image_path):
    try:
        # Read the image
        img = cv2.imread(image_path)
        if img is None:
            raise ValueError("Could not read the image file")
            
        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # Noise reduction
        gray = cv2.bilateralFilter(gray, 11, 17, 17)
        
        # Edge detection
        edged = cv2.Canny(gray, 170, 200)
        
        # Find contours
        contours, _ = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]
        
        plate_contour = None
        
        for contour in contours:
            perimeter = cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, 0.02 * perimeter, True)
            
            if len(approx) == 4:
                plate_contour = approx
                break
                
        if plate_contour is None:
            print("No license plate found")
            return None
            
        # Crop the license plate
        mask = np.zeros(gray.shape, np.uint8)
        cv2.drawContours(mask, [plate_contour], 0, 255, -1)
        new_image = cv2.bitwise_and(img, img, mask=mask)
        
        (x, y) = np.where(mask == 255)
        (topx, topy) = (np.min(x), np.min(y))
        (bottomx, bottomy) = (np.max(x), np.max(y))
        cropped = gray[topx:bottomx+1, topy:bottomy+1]
        
        return cropped
        
    except Exception as e:
        print(f"Error processing image: {e}")
        return None

def recognize_plate_text(image):
    try:
        # Configure Tesseract
        config = '--oem 3 --psm 6 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        text = pytesseract.image_to_string(image, config=config)
        return ''.join(e for e in text if e.isalnum())
    except Exception as e:
        print(f"Error recognizing text: {e}")
        return ""

def main(image_path):
    plate_image = preprocess_image(image_path)
    
    if plate_image is not None:
        # Display the license plate
        cv2.imshow('License Plate', plate_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
        # Recognize the text
        plate_text = recognize_plate_text(plate_image)
        print(f"Recognized License Plate: {plate_text}")
    else:
        print("License plate detection failed")

if __name__ == "__main__":
    # Use an absolute path to your image file
    image_path = r"C:\Users\Asus\OneDrive\Desktop\Dipak\image2.jpg"  # Change this to your actual image path
    main(image_path)