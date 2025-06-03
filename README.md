# OpticDecode
I am Dipak Mane, currently pursuing my first year (2024–25) in the Electronics and Telecommunication (ENTC) branch at Vishwakarma Institute of Technology, Pune.

As part of a Mathematics case study project at college, our group explored the topic "Image Processing – How It Works and Its Applications." Each member focused on a specific subtopic, and I chose to research how the Government of India utilizes image processing and recognition technologies in systems such as FASTag toll collection and automatic challan generation. These systems use cameras and software to capture and interpret vehicle number plates, making toll payment and traffic violation detection faster and more efficient.

Through this case study, I gained a foundational understanding of how digital images are represented and analyzed by machines. I learned that each image is made up of pixels, and each pixel holds information in the form of RGB (Red, Green, Blue) values. These values can be considered as vectors in a color space. Image processing software detects changes in these pixel vectors by computing gradients — essentially measuring how quickly and in which direction the colors change across an image. This is a fundamental step in identifying shapes, edges, and features within the image.

Further, I studied how these gradient changes help the software recognize specific patterns. For example, sudden changes in pixel values often indicate the boundary of an object, such as a vehicle or a license plate. The system then isolates these regions and uses optical character recognition (OCR) techniques to extract readable text from the image — such as the alphanumeric characters on a number plate. These text values are then matched against a central database for identification, toll deduction, or issuing fines for traffic violations.

This project also introduced me to the basics of machine learning and computer vision models, many of which are implemented in Python using libraries like OpenCV, NumPy, and Tesseract OCR. I reviewed Python code for image text recognition models, which include steps like image pre-processing, contour detection, thresholding, and character segmentation. These processes together enable automated recognition of vehicle number plates in real-time.

Overall, this case study not only helped me understand the mathematical concepts behind image processing but also gave me a practical view of how such technology is already being used in real-life applications by government and private sectors. It sparked my interest in the field of artificial intelligence, and I look forward to exploring more about computer vision, deep learning, and embedded systems in the future.

I have attacted the python code for demo and one image 

ThankYou

To Run THis Files You Need to Install followings things in Your system

Tesseract https://github.com/UB-Mannheim/tesseract/wiki
pip install opencv-python numpy pytesseract pillow (in Python Pip)
