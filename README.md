# Kizmeow-OpenSea-and-Etherscan-Discord-Bot

A Discord bot wrote with Python. Kizmeow let you track your NFT project and display some useful information(e.g. market cap, floor price, total supply, eth price, gas fee, transaction history, display NFT owner, download original resolution NFT image...etc) by calling Etherscan and OpenSea API.

If you like this project, please give me star on the upper right corner:)

I rewrote my code and updated bot to V3, if you still need V2, it's in the `achive` folder.

[Kizmeow NFT Tracker V3 invite link](https://discord.com/api/oauth2/authorize?client_id=923512417907015693&permissions=277025508352&scope=applications.commands%20bot)

If you no nothing about coding, you can just simply click the blue letter above and invite the bot to your server.

-------------------------------------------------------------------------------------------------------------------------------------------------

Quickstart
-----------------
As you can see, there are 3 folders.

![image](https://user-images.githubusercontent.com/80938768/164334232-7e6c6a00-a9ec-417d-bb7a-2fc7f82d926f.png)


I put the code of old bots in `achive` folder.

`Kizmeow NFT Tracker V3` is the main bot, most functions are in this bot.

`Kizmeow OpenSea Trade Tracker` is the bot that will send embed message in specific channel when there's a list or sold event on OpenSea. This is its only function. In order to use this bot, you need **OpenSea API key**.

-------------------------------------------------------------------------------------------------------------------------------------------------

What can these bots do?
-----------------
### `Kizmeow OpenSea Trade Tracker`

send message in specific channel when there's a list or sold event of your NFT collection on OpenSea

![image](https://user-images.githubusercontent.com/80938768/149489498-5e80a294-a9a6-4a3d-8af2-fdcb6d530ba1.png)

### `Kizmeow NFT Tracker V3`

note: project_name is the text at the end of OpenSea url

![image](https://user-images.githubusercontent.com/80938768/155941533-a9e86c86-54e5-4708-b1fe-0b05ca48033c.png)

-------------------------------------------------------------------------------------------------------------------------------------------------
\[system commands]

`/help`

display help message

`/meow`

return bot latency

`/invite`

invite Kizmeow to your server

\[NFT commands]

`/project_realtime`

display project realtime information

`/project_history`

display project history information

`/project_nft`

display information of specific NFT

-------------------------------------------------------------------------------------------------------------------------------------------------

Requirements
-----------------
**environment**

+ Python > 3.8

**packages**

+ discord
+ discord-py-slash-command
+ urllib
+ json
+ asyncio
+ request

-------------------------------------------------------------------------------------------------------------------------------------------------

Video Tutorial
-----------------
check out 

Usage
-----------------
There are 2 ways to run this bot.
Whether you choose first or second method, you'll need [Discord bot token](https://discord.com/developers/applications) and [Etherscan API](https://etherscan.io/myapikey). If you choose the second method, you'll also need [Uptimerbot](https://uptimerobot.com/) account. If you want to use "send message in specific channel when there's a list or sold event of your NFT collection on OpenSea" this function, you'll also need OpenSea API key, you can apply for the API key [here](https://docs.opensea.io/reference/request-an-api-key). Fill in the google form to apply for the API key. They will send API key to your gmail in about 2 days

### 1.run it on repl.it(cloud)
You can run it on repl.it, just fork [it](https://replit.com/@xeiftc/Kizmeow-NFT-Tracker-V2) and run. Remember to change discord bot token and Etherscan API key, then put them in environment variable. **DO NOT PUT TOKENS IN YOUR CODE DIRECTLY** cuz repls on replit is public if you use their free plan, and there are some ppl using scrypt to grab your token.
Next, copy the link here, ![image](https://user-images.githubusercontent.com/80938768/146533872-021b05b3-f18c-44db-a943-527903dc6616.png) create a [Uptimerbot](https://uptimerobot.com/) account and paste your link here. ![image](https://user-images.githubusercontent.com/80938768/146534310-74201ab2-700e-4271-94a2-f2ecf8d12acb.png)

### 2.run it on your computer(local)
Just download [it](https://github.com/Xeift/Kizmeow-OpenSea-and-Etherscan-Discord-Bot/archive/refs/heads/main.zip) and install all the packages in **Requirement**, make sure you have install python. Remember to change discord bot token and Etherscan API key. Then, run main.py

Official Website
-----------------
https://watercatuwu.github.io/kizmeow-nft-site/ 

by WaterCatMeow

Bot Avatar Illustrator
-----------------
[姬玥 Kiyue](https://www.facebook.com/profile.php?id=100026170072950)
![avatar](https://user-images.githubusercontent.com/80938768/146544100-315cdd44-7461-441b-a3dd-d3ee653b145a.png)
