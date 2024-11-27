from flask import send_from_directory, jsonify

ALLOWED_EXTENSIONS = {'png'}
IMAGE_FOLDER = 'images'


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def image(filename):
    if not allowed_file(filename):
        return jsonify({
            "error": "Invalid file extension",
            "message": f"Image extension should be .png"
        }), 400

    print(f"API – /images/{{filename}} – {filename}")
    return send_from_directory(IMAGE_FOLDER, filename), 200

