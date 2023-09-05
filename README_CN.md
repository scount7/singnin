# GLaDOS-Bot-Action-with-Telegram-Notice

[English](https://github.com/FHYQ-Dong/GLaDOS-Bot-Action-with-Telegram-Notice/blob/main/README.md) | 简体中文

一个可以帮助您通过 Telegram 通知自动签到 GLaDOS 的 Github Action。

### 使用方法

#### 准备工作

1. 在 Telegram 上申请机器人，并记录其 `TOKEN`：

   - 您可以按照 BotFather 提供的指导进行操作。

   ![1](https://user-images.githubusercontent.com/87631978/230318685-64a109e4-4943-49c7-9d06-4e4d6e10d1d5.jpg)
   ![2](https://user-images.githubusercontent.com/87631978/230318690-f8ef0ffc-dde5-4d0a-9a54-5d06eb6118d5.jpg)

   - 记住：要与您的机器人开始聊天。

   ![3](https://user-images.githubusercontent.com/87631978/230319099-bc2e21a6-173a-4c57-986c-628ef01c4325.jpg)

2. 在 [RawDataBot](https://t.me/RawDataBot) 获取您的 Telegram `CHAT_ID`：

   - 点击“开始”按钮，RawDataBot 将向您发送一条消息，请找到“from”或“chat”部分，然后在其中找到您的“id”。

   ![4](https://user-images.githubusercontent.com/87631978/230319269-c9bd5220-472b-4be2-a00b-62ff94fbc9ab.jpg)

   - 配置完成后，可以删除此机器人。

3. 在签到 GLaDOS 时获取您的 cookie：

   - 打开 [GLaDOS](https://glados.one/console/checkin) 的签到页面。

   ![5](https://user-images.githubusercontent.com/87631978/230319385-2b151104-8f83-4f90-9b03-566674928c20.jpg)

   - 按下键盘上的 `F12`（对于一些笔记本电脑用户，可能是 `Fn`+`F12`）打开开发者工具。

   - 选择“网络”选项卡，然后在网站上按“签到”按钮。

   ![6](https://user-images.githubusercontent.com/87631978/230319977-602e9419-0dd5-49f1-933e-268cc69b1d28.jpg)

   - 点击一个记录，并选择“标头”标签，向下滚动，您可以在 “请求标头” 部分中看到自己的 `cookie`。
   - **记住：复制您的 `cookie` 值时不要包括其名称！！！**

   ![7](https://user-images.githubusercontent.com/87631978/230320024-17c2a01c-c6ad-4975-a593-9370563a123f.jpg)

#### 配置

1. Fork 此存储库（需要 Github 帐户）：

   - **记住：在您的 Fork 存储库中进行任何更改，而不是在原始存储库中！！！**

   ![8](https://user-images.githubusercontent.com/87631978/230322316-e1b7ef44-91ea-4067-9058-2ff3c4c2791c.jpg)

2. 进入此存储库的“设置”页面

3. 在“Security”下的 `Secrets and variables` -> `Actions` 中添加三个 `New Repository Secret`：`BOT_TOKEN`、`CHAT_ID` 和 `COOKIE`

 <img width="912" alt="10" src="https://user-images.githubusercontent.com/87631978/230323335-36aa16ec-665d-45ed-b870-4981843cbd01.png">
<img width="908" alt="11" src="https://user-images.githubusercontent.com/87631978/230323345-6502a29e-a88e-4b58-818d-8e0495b0e5d6.png">
<img width="911" alt="12" src="https://user-images.githubusercontent.com/87631978/230323349-badd6dd1-206a-4628-814a-107a16b48e27.png">

### 操作

- 您可以通过在“Action”页面上按“Run Workflow”按钮手动运行此 Github Action。
- 此操作将每天自动在北京时间中午 12:20 与晚上 18:20 运行。

![13](https://user-images.githubusercontent.com/87631978/230326733-2c9cdc45-f6a1-4c40-bf25-e3d1d90fd42c.jpg)


### 贡献者
<a href="https://github.com/FHYQ-Dong/GLaDOS-Bot-Action-with-Telegram-Notice/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=FHYQ-Dong/GLaDOS-Bot-Action-with-Telegram-Notice" />
</a>
