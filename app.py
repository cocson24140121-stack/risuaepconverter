import io
import re
from flask import Flask, render_template, request, send_file, flash, redirect

app = Flask(__name__)
app.secret_key = "risuaepconverter-secret-key"

VERSION_SIGNATURES = {
    "15.x": b"\x00\x0F",  # CC 2018
    "16.x": b"\x00\x10",  # CC 2019
    "17.x": b"\x00\x11",  # 2020
    "18.x": b"\x00\x12",  # 2021
    "22.x": b"\x00\x16",  # 2022
    "23.x": b"\x00\x17",  # 2023
    "24.x": b"\x00\x18"   # 2024
}

def patch_aep_bytes(data: bytes, target_ver: str) -> bytes:
    new_bytes = bytearray(data)
    target_tag = VERSION_SIGNATURES.get(target_ver)
    
    if not target_tag:
        return data

    pattern = rb"Egg\d"
    matches = [m.start() for m in re.finditer(pattern, data)]
    
    for idx in matches:
        offset = idx + 4
        if offset + 2 <= len(new_bytes):
            new_bytes[offset:offset+2] = target_tag

    return bytes(new_bytes)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files.get("file")
        target_version = request.form.get("target_version")

        if not file or file.filename == "":
            return redirect(request.url)

        if not file.filename.lower().endswith(".aep"):
            return redirect(request.url)

        file_bytes = file.read()
        converted_data = patch_aep_bytes(file_bytes, target_version)
        
        output_name = f"risu_{target_version}_{file.filename}"
        return send_file(
            io.BytesIO(converted_data),
            as_attachment=True,
            download_name=output_name,
            mimetype="application/octet-stream"
        )

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
