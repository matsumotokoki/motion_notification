from transformers import pipeline
import requests
from PIL import Image
from io import BytesIO
from googletrans import Translator

# 画像キャプション生成のパイプラインを作成
# 各画像URLをループしてキャプションを生成
# 画像のダウンロード
# image = Image.open("./motion_detected.jpg")

# 画像を表示
class Caption(object):
    def __init__(self):
        self.captioner = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")

    def translate_en_to_ja(self,text):
        translator = Translator()
        translation= translator.translate(text, src='en', dest='ja')
        return translation.text

    def make_caption(self,img):
        captions = self.captioner(img)
        generated_text = captions[0]['generated_text']
        print(f"キャプション: {generated_text}")

        # キャプションを日本語に翻訳
        translated_caption = self.translate_en_to_ja(generated_text)
        print(f"翻訳されたキャプション: {translated_caption}\n")

        return translated_caption


if __name__ == "__main__":
    image = Image.open("./motion_detected.jpg")
    image.show()
    caption = Caption()
    caption.make_caption(image)
