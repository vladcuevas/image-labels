import re
import os

def detect_labels(path):
    """Detects labels in the file."""
    # Imports the Google Cloud client library
    from google.cloud import vision
    import io

    # Instantiates a client
    client = vision.ImageAnnotatorClient()

    # Loads the image into memory
    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    # Performs label detection on the image file
    response = client.label_detection(image=image)
    labels = response.label_annotations

    keywords = []
    for label in labels:
        keywords.append(label.description)

    with open(f"{path}.txt", 'w', encoding='UTF-8', newline='\n') as f:
        #keywords
        f.write(", ".join(keywords))
        f.write("\n")
        #hashtags
        out0 = [x.replace(' ', '') for x in keywords]
        out0 = f'#{" ".join(out0)}'
        out0 = re.sub(r'-', '', out0)
        f.write(re.sub(r'\s', ' #', out0))

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))


# The name of the images file to annotate

directory = "./resources/"

for root, subdirectories, files in os.walk(directory):

    # extensions
    ext = ('.JPG', 'jpg')

    for file in files:

        print(os.path.join(root, file))
        file_name = os.path.abspath(os.path.join(root, file))

        if file_name.endswith(ext):

            detect_labels(file_name)

            print('done')
