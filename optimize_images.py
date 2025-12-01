import os
import subprocess
import sys

def optimize_image(input_path, output_path, max_width):
    try:
        # Use sips to resize and convert to jpeg
        subprocess.run(['sips', '-Z', str(max_width), '-s', 'format', 'jpeg', '-s', 'formatOptions', '80', input_path, '--out', output_path], check=True)
        print(f"Optimized: {input_path} -> {output_path}")
    except Exception as e:
        print(f"Failed to optimize {input_path}: {e}")

# Hero Image
optimize_image('images/hero-image.png', 'images/hero-image.jpg', 1920)

# Prototype Image
optimize_image('images/prototype-image.png', 'images/prototype-image.jpg', 1000)

# Team Images
team_dir = 'images/team'
if os.path.exists(team_dir):
    for filename in os.listdir(team_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            input_path = os.path.join(team_dir, filename)
            output_path = os.path.join(team_dir, os.path.splitext(filename)[0] + '.jpg')
            optimize_image(input_path, output_path, 400)

