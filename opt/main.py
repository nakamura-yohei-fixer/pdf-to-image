import base64
from io import BytesIO
from pdf2image import convert_from_path, convert_from_bytes


images = convert_from_path('sample.pdf')

print(images)


def base64pdf_to_base64png(image):
    buffer = BytesIO()
    image.save(buffer, format="PNG")
    return base64.b64encode(buffer.getvalue()).decode().replace("'", "")


base64Pngs = list(map(base64pdf_to_base64png, images))
print(base64Pngs)
