import sys
from PIL import Image

def image_to_ascii_svg(image_path, output_path, width_chars=80, scale=0.5):
    # ASCII characters from darkest to lightest
    chars = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", ".", " "]
    
    try:
        img = Image.open(image_path).convert('L')
    except Exception as e:
        print(f"Error opening image: {e}")
        return

    # Resize image
    aspect_ratio = img.height / img.width
    height_chars = int(aspect_ratio * width_chars * scale)
    img = img.resize((width_chars, height_chars))
    
    pixels = img.getdata()
    
    # Map pixels to characters
    ascii_str = ""
    for pixel_value in pixels:
        index = int(pixel_value / 255 * (len(chars) - 1))
        ascii_str += chars[index]
    
    # Split string into lines
    ascii_lines = [ascii_str[i:i+width_chars] for i in range(0, len(ascii_str), width_chars)]
    
    # Generate SVG
    svg_width = width_chars * 6
    svg_height = height_chars * 12
    
    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {svg_width} {svg_height}">
  <style>
    .ascii {{
      font-family: monospace;
      font-size: 10px;
      fill: #ffdb58; /* Gold/Yellow color to match screenshot */
      white-space: pre;
    }}
  </style>
  <rect width="100%" height="100%" fill="#000000"/>
  <g class="ascii">
'''
    
    for idx, line in enumerate(ascii_lines):
        # Escape characters for XML
        line_escaped = line.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        y_pos = (idx + 1) * 12
        svg_content += f'    <text x="0" y="{y_pos}">{line_escaped}</text>\n'
        
    svg_content += '''  </g>
</svg>'''

    with open(output_path, 'w') as f:
        f.write(svg_content)
        
    print(f"Success! Generated {output_path}")
    print("Copy the contents of this file or link to it in your profile SVG.")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python image_to_ascii_svg.py <input_image> <output_svg>")
        print("Example: python image_to_ascii_svg.py my_face.jpg ascii_portrait.svg")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        image_to_ascii_svg(input_file, output_file, width_chars=100, scale=0.6)
