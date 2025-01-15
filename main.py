import cv2
import numpy as np
import subprocess
from HandTrackingModule import HandDetector

def main():
    try:
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("无法打开摄像头")
            return

        detector = HandDetector(detectionCon=0.75, trackCon=0.75)

        # 初始化上一次的手势状态和按键显示变量
        previous_fingers = [False] * 5
        pressed_key = ''

        while True:
            success, img = cap.read()
            if not success:
                print("无法读取帧")
                continue

            img = detector.findHands(img)
            lmList = detector.findPosition(img, draw=False)

            if lmList:
                fingers = detector.fingerStatus(lmList)

                # 检查手势状态是否变化
                if fingers != previous_fingers:
                    # 将当前和先前的手势状态转换为字符串以便显示
                    current_fingers_str = ''.join(['1' if f else '0' for f in fingers])
                    previous_fingers_str = ''.join(['1' if f else '0' for f in previous_fingers])

                    # 在图像上绘制当前和先前的手势状态
                    cv2.putText(img, f"Current: {current_fingers_str}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)
                    cv2.putText(img, f"Previous: {previous_fingers_str}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 255), 2)

                    # 检查是否至少有三个手指闭合
                    if sum(fingers) <= 3:
                        subprocess.run(['wtype', ' '])
                        pressed_key = 'Space'
                    # 检查是否所有手指打开
                    elif all(fingers):
                        subprocess.run(['wtype', 'down'])
                        pressed_key = 'Down'

                    # 更新上一次的手势状态
                    previous_fingers = fingers

                # 在图像上显示按下的按键信息
            cv2.putText(img, f"Pressed Key: {pressed_key}", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)

            # 显示图像
            cv2.imshow("CV2", img)

            # 按 'q' 键退出循环
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    except Exception as e:
        print(f"程序运行过程中出现错误: {e}")
    finally:
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
