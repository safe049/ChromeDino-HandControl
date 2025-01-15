
# ChromeDino-HandControl
使用OpenCV程序让你可以通过手势来玩Chrome恐龙游戏

## 简介
ChromeDino-HandControl是一个开源项目，利用OpenCV库实现的手势识别技术，通过检测你的手势来控制Chrome浏览器中的恐龙跳跃

## 功能特点
- 手势控制：通过手势识别技术，用特定的手势控制游戏中的跳跃动作。
- 实时检测：能够实时检测你的手势进行按键输入

## 适用于
- Linux Wayland桌面环境
- Windows
- 你可以自行进行移植
  
## 硬件需求
- 一个摄像头

## 安装指南
1. 确保你的电脑安装了Python。
2. 打开命令行工具，输入以下命令来安装所需的Python库：
   ```bash
   pip install opencv-python mediapipe pyautogui
   ```
3. 下载本项目的源代码，解压后进入项目目录
4. 使用`python main.py`打开程序 [如果你是Windows用户,请使用`python main-windows.py`]

## 如何使用
1. 打开Chrome浏览器，进入谷歌小恐龙游戏界面或此网页:[https://chrome-dino-game.github.io/](https://chrome-dino-game.github.io/)
2. 启动本程序
3. 握拳以按下space键,然后松开
4. 就是这么用!

## 许可证
本项目使用Apache 2.0许可证,有关详细信息，请查看LICENSE文件

## 鸣谢
- 感谢[Mediapipe](https://github.com/google-ai-edge/mediapipe)项目提供的手势识别技术
- 感谢[OpenCV](https://github.com/opencv/opencv)项目提供的图像处理技术