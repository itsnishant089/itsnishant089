import base64
import re

# Read the NEW face image (image.png - the proper ASCII art face)
with open('image.png', 'rb') as f:
    img_data = f.read()

img_str = base64.b64encode(img_data).decode('utf-8')

# Create the SVG image tag for the face - positioned in the top-left blank space
face_svg = f'''<g transform="translate(20, 20)">
  <image width="350" height="420" href="data:image/png;base64,{img_str}" opacity="1" />
</g>'''

# Read the layout
with open('svg/unified_layout.svg', 'r', encoding='utf-8') as f:
    layout = f.read()

# Replace the existing ASCII portrait block
pattern = r'<!-- ==================== ASCII PORTRAIT \(TOP LEFT\) ==================== -->.*?<!-- ==================== HEADER'
replacement = f'<!-- ==================== ASCII PORTRAIT (TOP LEFT) ==================== -->\n{face_svg}\n\n  <!-- ==================== HEADER'

new_layout = re.sub(pattern, replacement, layout, flags=re.DOTALL)

with open('svg/unified_layout.svg', 'w', encoding='utf-8') as f:
    f.write(new_layout)

print('Done! Replaced face with image.png!')
