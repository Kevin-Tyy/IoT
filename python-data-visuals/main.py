import face_recognition
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image

# Load an image
image_path = 'path/to/your/image.jpg'  # Replace with the path to your image
image = face_recognition.load_image_file(image_path)

# Find all face locations in the image
face_locations = face_recognition.face_locations(image)

# Display the image with rectangles around detected faces
plt.imshow(Image.fromarray(image))
ax = plt.gca()

for face_location in face_locations:
    top, right, bottom, left = face_location
    rect = patches.Rectangle((left, top), right - left, bottom - top, linewidth=2, edgecolor='r', facecolor='none')
    ax.add_patch(rect)

plt.axis('off')
plt.show()
