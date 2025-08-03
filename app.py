import io
import os
from flask import Flask, request, send_file, jsonify
from rembg import remove
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow all origins (for Blogger frontend)

@app.route("/")
def home():
    return jsonify({"message": "Flask BG Remover is live!"})

@app.route("/remove", methods=["POST"])
def remove_background():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    input_data = file.read()
    output_data = remove(input_data)

    return send_file(
        io.BytesIO(output_data),
        mimetype='image/png',
        as_attachment=False,
        download_name="output.png"
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
