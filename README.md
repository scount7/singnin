# GLaDOS-Bot-Action-with-Telegram-Notice

English | [简体中文](https://github.com/FHYQ-Dong/GLaDOS-Bot-Action-with-Telegram-Notice/blob/main/README_CN.md)

 A Github Action that can help you sign in GlaDOS automatically with telegram notice.  
 
 Thanks [@GithubGaoYang](https://github.com/GithubGaoYang) for Chinese version.
 
### Usage
#### Preparation  

 1. Apply for a bot on telegram at [BotFather](https://t.me/BotFather) and remember its `TOKEN`:  
 
    - You can follow the guidance provided by BotFather.  
    
    ![1](https://user-images.githubusercontent.com/87631978/230318685-64a109e4-4943-49c7-9d06-4e4d6e10d1d5.jpg)
    ![2](https://user-images.githubusercontent.com/87631978/230318690-f8ef0ffc-dde5-4d0a-9a54-5d06eb6118d5.jpg)
    
    - Remember: start a chat with your bot.  
    
    ![3](https://user-images.githubusercontent.com/87631978/230319099-bc2e21a6-173a-4c57-986c-628ef01c4325.jpg)

 2. Get your telegram `CHAT_ID` at [RawDataBot](https://t.me/RawDataBot):  
 
    - Touch the start button and RawDataBot will send you a message, find the `from` or `chat` section and then find your `id` in it.  
    
    ![4](https://user-images.githubusercontent.com/87631978/230319269-c9bd5220-472b-4be2-a00b-62ff94fbc9ab.jpg)

    - You can delete this bot after finishing configuration.
    
 3. Get your cookie when you check in GLaDOS:  
 
    - Open the sign in page on [GLaDOS](https://glados.one/console/checkin).  
    
    ![5](https://user-images.githubusercontent.com/87631978/230319385-2b151104-8f83-4f90-9b03-566674928c20.jpg)

    - Press `F12` on your keyboard (for some laptop users, it may be `Fn`+`F12`) to open developer tools.
    - Choose `Network` tab and press the `Sign in` button on the website.  
    
    ![6](https://user-images.githubusercontent.com/87631978/230319977-602e9419-0dd5-49f1-933e-268cc69b1d28.jpg)

    - Click one record and choose `Header` tab, scroll down and you can see your `cookie` in `Request Header` section. 
    - **Remember: COPY THE VALUE OF YOUR COOKIE WITHOUT ITS NAME!!!**  
    
    ![7](https://user-images.githubusercontent.com/87631978/230320024-17c2a01c-c6ad-4975-a593-9370563a123f.jpg)

#### Configuration  

 1. Fork this repository (Need a Github account):  
 
    - **Remember: make ANY changes in your FORKED REPOSITORY, NOT THE ORIGINAL ONE!!!**  
    
    ![8](https://user-images.githubusercontent.com/87631978/230322316-e1b7ef44-91ea-4067-9058-2ff3c4c2791c.jpg)

 2. Enter the Settings Page of the repository
 3. Enter `Secrets and variables` -> `Actions` in `Security`  
 
 ![9](https://user-images.githubusercontent.com/87631978/230322987-cc24350a-b96b-40a2-a97d-128a22adaf96.jpg)

 4. Add three `New Repository Secret`: `BOT_TOKEN`, `CHAT_ID` and `COOKIE`  
 
 <img width="912" alt="10" src="https://user-images.githubusercontent.com/87631978/230323335-36aa16ec-665d-45ed-b870-4981843cbd01.png">
<img width="908" alt="11" src="https://user-images.githubusercontent.com/87631978/230323345-6502a29e-a88e-4b58-818d-8e0495b0e5d6.png">
<img width="911" alt="12" src="https://user-images.githubusercontent.com/87631978/230323349-badd6dd1-206a-4628-814a-107a16b48e27.png">


### Action
 - You can run this Github Action manually by pressing `Run Workflow` button on `Action` page.
 - And the Action will always run at 12:20 p.m. and 18:20 p.m.(GMT+8:00) automatically.  
 
 ![13](https://user-images.githubusercontent.com/87631978/230326733-2c9cdc45-f6a1-4c40-bf25-e3d1d90fd42c.jpg)
 
 
 ### Contributors
<a href="https://github.com/FHYQ-Dong/GLaDOS-Bot-Action-with-Telegram-Notice/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=FHYQ-Dong/GLaDOS-Bot-Action-with-Telegram-Notice" />
</a>
