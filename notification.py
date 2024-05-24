import requests

class NotificationToLine(object):
    def __init__(self):
        self.access_token = ''  # ここに発行したアクセストークンを入力

    def send_line_notify(self, message):
        line_notify_api = 'https://notify-api.line.me/api/notify'
        headers = {
            'Authorization': f'Bearer {self.access_token}'
        }
        data = {
            'message': message
        }
        response = requests.post(line_notify_api, headers=headers, data=data)
        return response.status_code

    def send_line_notify_with_image(self, message, image_path):
        line_notify_api = 'https://notify-api.line.me/api/notify'
        headers = {
            'Authorization': f'Bearer {self.access_token}'
        }
        data = {
            'message': message
        }
        files = {
            'imageFile': open(image_path, 'rb')
        }
        response = requests.post(line_notify_api, headers=headers, data=data, files=files)
        return response.status_code


if __name__ == "__main__":
    notify = NotificationToLine()

    # メッセージを送信
    message = 'Hello from Python!'
    status_code = notify.send_line_notify(message)

    if status_code == 200:
        print('通知を送信しました。')
    else:
        print(f'通知の送信に失敗しました。ステータスコード: {status_code}')

    # 画像付きメッセージを送信
    image_message = 'Hello from Python with image!'
    image_path = './motion_detected.jpg'  # ここに送信したい画像のパスを入力
    status_code_with_image = notify.send_line_notify_with_image(image_message, image_path)

    if status_code_with_image == 200:
        print('画像付き通知を送信しました。')
    else:
        print(f'画像付き通知の送信に失敗しました。ステータスコード: {status_code_with_image}')

