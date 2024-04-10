import easyocr
from PIL import Image
import io
import numpy as np

class OCRProcessor:
    def __init__(self, language_code, font_path="NanumGothic-Regular.ttf", font_size=15):
        self.font_path = font_path
        self.font_size = font_size
        # 여기서 GPU 사용 여부를 설정할 수 있습니다. 시스템에 따라 False로 설정할 필요가 있을 수 있습니다.
        self.reader = easyocr.Reader([language_code], gpu=True)

    def process_image(self, image_bytes):

        # 이미지에서 텍스트 추출
        image = Image.open(io.BytesIO(image_bytes))
        np_image = np.array(image)
        result = self.reader.readtext(np_image)


        # 추출된 텍스트만을 리스트로 컴파일
        extracted_texts = [text[1] for text in result]

        return extracted_texts

