from paddleocr import PaddleOCR
import cv2

# Load Paddle OCR model once for all images
ocr = PaddleOCR(lang="japan")

def clean_text(texts: list[str]) -> str:
    text ="\n".join(texts)
    text = text.replace("\n\n", "\n").strip()
    return text

def extract_text_from_image(image_path: str) -> str:
    # deep learning model to do ocr.
    img = cv2.imread(image_path)
    # rezie image to fit into the deep learning model
    img = cv2.resize(img, (1200, 1600))
    result = ocr.predict(img)

    # clean text to have string in each line as output for readibility of LLM
    text = clean_text(result[0]["rec_texts"])

    return text
