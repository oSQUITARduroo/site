from flask import Flask, request, render_template
import os
import subprocess

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    if request.method == 'POST':
        file = request.files['file']
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)

        # Ejecutar strings
        strings_output = subprocess.getoutput(f"strings '{filepath}'")

        # Ejecutar exiftool
        exif_output = subprocess.getoutput(f"exiftool '{filepath}'")

        # Ejecutar binwalk
        binwalk_output = subprocess.getoutput(f"binwalk '{filepath}'")

        result = f"== STRINGS ==\n{strings_output}\n\n== EXIFTOOL ==\n{exif_output}\n\n== BINWALK ==\n{binwalk_output}"

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
