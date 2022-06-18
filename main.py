import io
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
    print('Labels:')

    for label in labels:
        print(label.description)

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))


# The name of the image file to annotate
file_name = os.path.abspath('resources/wakeupcat.jpg')
