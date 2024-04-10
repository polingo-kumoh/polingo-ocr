from flask import Flask, request, jsonify
import os

app = Flask(__name__)

app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 5MB 제한

@app.route('/to-text', methods=['POST'])
def image_to_text():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # 파일 확장자 검증
    _, file_extension = os.path.splitext(file.filename)
    if file_extension.lower() != '.pdf':
        return jsonify({"error": "Invalid file type. Only PDF files are allowed."}), 400

    # 파일을 스트림으로 읽기



    # 예시 응답
    return jsonify({"data": result}), 200

    return jsonify({"error": "Unknown error occurred"}), 500

if __name__ == '__main__':
