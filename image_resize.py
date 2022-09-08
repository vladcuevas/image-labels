import cv2
import os

directory = "./resources/"

for root, subdirectories, files in os.walk(directory):

    # extensions
    ext = ('.JPG', 'jpg', 'png', '.PNG')

    for file in files:

        print(os.path.join(root, file))
        file_name = os.path.abspath(os.path.join(root, file))

        if file_name.endswith(ext):
 
            img = cv2.imread(file_name, cv2.IMREAD_UNCHANGED)
            
            print('Original Dimensions : ', img.shape)
            
            scale_percent = 50 # percent of original size
            width = int(img.shape[1] * scale_percent / 100)
            height = int(img.shape[0] * scale_percent / 100)
            dim = (width, height)
            
            # resize image
            resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
            
            print('Resized Dimensions : ',resized.shape)
            
            cv2.imwrite(file_name, resized)
            # cv2.imshow("Resized image", resized)
            # cv2.waitKey(0)
            cv2.destroyAllWindows()