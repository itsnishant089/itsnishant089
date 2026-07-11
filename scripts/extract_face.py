import base64
from PIL import Image
from io import BytesIO

# Crop face
img = Image.open('my.png')
# Assuming face is roughly in this region: x: 0-380, y: 0-450
face = img.crop((0, 0, 380, 450))

# Save to buffer
buffer = BytesIO()
face.save(buffer, format='PNG')
img_str = base64.b64encode(buffer.getvalue()).decode('utf-8')

# Create SVG
svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 380 450">
  <image width="380" height="450" href="data:image/png;base64,{img_str}" />
</svg>'''

with open('svg/face.svg', 'w') as f:
    f.write(svg)

print('Base64 SVG generated!')
