import cv2
import time


class DetectDiffFromCam(object):
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.ret, self.frame1 = self.cap.read()
        self.frame1 = cv2.resize(self.frame1, (int(self.frame1.shape[1]/2), int(self.frame1.shape[0]/2)))
        self.gray1 = cv2.cvtColor(self.frame1, cv2.COLOR_BGR2GRAY)
        self.gray1 = cv2.GaussianBlur(self.gray1, (21, 21), 0)
        self.start_time = time.time()
        self.flag = False
        self.count = 0


    def captureVideo(self):
        self.ret, frame2 = self.cap.read()

        frame2 = cv2.resize(frame2, (int(frame2.shape[1]/2), int(frame2.shape[0]/2)))
        cv2.imshow("raw", frame2)
        
        # グレースケールに変換
        gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
        gray2 = cv2.GaussianBlur(gray2, (21, 21), 0)

        # フレーム間の差分を計算
        delta_frame = cv2.absdiff(self.gray1, gray2)
        thresh = cv2.threshold(delta_frame, 25, 255, cv2.THRESH_BINARY)[1]
        thresh = cv2.dilate(thresh, None, iterations=2)

        # 最初の5秒間は動き検知を行わない
        if time.time() - self.start_time > 5:
            # 変化のあるピクセル数を計算
            non_zero_count = cv2.countNonZero(thresh)
            total_pixels = thresh.shape[0] * thresh.shape[1]
            motion_ratio = non_zero_count / total_pixels

            print(motion_ratio)
            # 変化が10％以上なら動きを検知
            if motion_ratio > 0.07:
                # 画像を保存
                cv2.imwrite('motion_detected.jpg', frame2)
                print("Motion detected! Image saved.")
                self.start_time = time.time()
                if self.count%2==0:
                    self.flag = True
                self.count+=1

        # 現在のフレームを次のフレームと比較するために保存
        self.gray1 = gray2

        # 'q'キーで終了
        if cv2.waitKey(1) & 0xFF == ord('q'):
            return

    def releaseResoure(self):
        self.cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    DDC = DetectDiffFromCam()
    while True:
        DDC.captureVideo()
    DDC.releaseResoure()

