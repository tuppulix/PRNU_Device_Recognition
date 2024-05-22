import cv2
import numpy as np
from scipy.ndimage import gaussian_filter

def extract_prnu(image):
    # Step 1: Denoise the image using a Gaussian filter
    denoised_image = gaussian_filter(image, sigma=1)

    # Step 2: Subtract the denoised image from the original image to get the noise residual
    noise_residual = image.astype(float) - denoised_image.astype(float)

    # Step 3: Normalize the noise residual to zero mean and unit variance
    mean = np.mean(noise_residual)
    std = np.std(noise_residual)
    normalized_noise_residual = (noise_residual - mean) / std

    return normalized_noise_residual

def average_prnu(images):
    prnu_sum = None
    count = len(images)
    
    for image in images:
        prnu = extract_prnu(image)
        if prnu_sum is None:
            prnu_sum = prnu
        else:
            prnu_sum += prnu
    
    average_prnu = prnu_sum / count
    return average_prnu

def classify_image(image, average_prnu):
    prnu = extract_prnu(image)
    difference = np.linalg.norm(prnu - average_prnu)
    return difference

if __name__ == "__main__":
    # List of image paths
    image_paths = [
        'image1.jpg',
        'image2.jpg',
        'image3.jpg',
        'image4.jpg',
        'image5.jpg',
        'image6.jpg',
        'image7.jpg',
        'image8.jpg',
        'image9.jpg',
        'image10.jpg',
        'image11.jpg',
        'image12.jpg',
        'image13.jpg',
        'image14.jpg',
        'image15.jpg',
        'image16.jpg',
        'image17.jpg',
        'image18.jpg',
        'image19.jpg',
        'image20.jpg',
        'image21.jpg',
        'image22.jpg',
        'image23.jpg',
        'image24.jpg',
        'image25.jpg'
    ]
    
    images = [cv2.resize(cv2.imread(path, cv2.IMREAD_GRAYSCALE), (700, 1080)) for path in image_paths]
    
    # Calculate the average PRNU matrix
    avg_prnu = average_prnu(images)
    
    # Test image classification
    test_image_path = 'test_image.jpg'
    test_image = cv2.resize(cv2.imread(test_image_path, cv2.IMREAD_GRAYSCALE), (700, 1080))
    difference = classify_image(test_image, avg_prnu)
    
    print(f"Difference between test image PRNU and average PRNU: {difference}")
    
    # Display the average PRNU image (optional)
    cv2.imshow('Average PRNU', avg_prnu)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    # Optionally, save the average PRNU image
    cv2.imwrite('average_prnu_image.jpg', (avg_prnu * 255).astype(np.uint8))  # Scale back to 0-255 and convert to uint8 for saving as an image
