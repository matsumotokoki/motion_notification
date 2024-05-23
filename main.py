import sys
import os

import notification
import caption
import detect_diff

def main():
    cap = caption.Caption()
    DDC = detect_diff.DetectDiffFromCam()
    notify = notification.NotificationToLine()
    
    while True:
        DDC.captureVideo()
        if DDC.flag:
            image = "./motion_detected.jpg"
            cap_text = cap.make_caption(image)
            try:status_code_with_image = notify.send_line_notify_with_image("『" + cap_text + "』が検知されました．", image)
            except: status_code = notify.send_line_notify("『" + cap_text + " 』が検知されました．")
            DDC.flag = False

    DDC.releaseResoure()

if __name__ == "__main__":
    main()
