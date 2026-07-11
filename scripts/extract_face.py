import base64
from PIL import Image
from io import BytesIO

img = Image.open('my.png')
# Larger crop
face = img.crop((0, 30, 450, 650))

buffer = BytesIO()
face.save(buffer, format='PNG')
img_str = base64.b64encode(buffer.getvalue()).decode('utf-8')

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 450 620">
  <image width="450" height="620" href="data:image/png;base64,{img_str}" />
</svg>'''

with open('svg/face.svg', 'w') as f:
    f.write(svg)
