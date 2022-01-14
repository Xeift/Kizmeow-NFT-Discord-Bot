# Kizmeow-OpenSea-and-Etherscan-Discord-Bot

### [中文版](https://github.com/Xeift/Kizmeow-OpenSea-and-Etherscan-Discord-Bot/blob/main/%E8%AE%80%E6%88%91.md) | [English Ver](https://github.com/Xeift/Kizmeow-OpenSea-and-Etherscan-Discord-Bot/blob/main/README.md)
A Discord bot wrote with Python. Kizmeow let you track your NFT project and display some useful information(e.g. market cap, floor price, total supply, eth price, gas fee, transaction history, display NFT owner, download original resolution NFT image...etc) by calling Etherscan and OpenSea API.(This repl is in development)

If you like this project, please give me star on the upper right corner:)

This repl is not finish yet. If you want to try, you can simply click the blue letter below and invite the bot to your test server.
There are still some bugs, I'll fix them ASAP.

Please use this version, V2 follows the modular design and I fixed some bugs in the previous version. There's no Chinese version for V2 currently.

[Kizmeow NFT Tracker V2 invite link](https://discord.com/api/oauth2/authorize?client_id=923512417907015693&permissions=534723951680&scope=applications.commands%20bot)

[Kizmeow NFT Tracker V2 repl.it](https://replit.com/@xeiftc/Kizmeow-NFT-Tracker-V2)


These bots are just demos, if you found commands not work, please kick the bot and reinvite it to your server.
If you found bots offline, that's normal, I run these bots on repl.it, somtimes bots will offline because many people use my demo bots.
If you want a stable bot, I suggest you build your own bot base on my code, or run the bot on your computer insted of on repl.it

Note
-----------------
If you no nothing about coding, I suggest you contact me via Discord Xeift#1230, I can create customize bot for your project for free.
Or you can just simply click the blue letter below and invite the bot to your server.

[Kizmeow NFT Tracker V2 invite link](https://discord.com/api/oauth2/authorize?client_id=923512417907015693&permissions=534723951680&scope=applications.commands%20bot)

What can this bot do?
-----------------
send message in specific channel when there's a list or sold event of your NFT collection on OpenSea

![image](https://user-images.githubusercontent.com/80938768/149489498-5e80a294-a9a6-4a3d-8af2-fdcb6d530ba1.png)

In addition to the above function, you can also use the commands listed below

`/demi-human`   //you can change these three commands below to your project in code. You can contact me if you know nothing about coding.

display real-time price of Demi-Human.

`/demi-human-history`

display history price of Demi-Human.

`/demi-nft`

search specific Demi-Human NFT by token id. option: token_id

-------------------------------------------------------------------------------------------------------------------------------------------------

`/project-realtime`

display real-time price of specific project. option:project_name

`/project-history`

display history price of specific project. option:project_name

`/project-nft`

search the NFT of a specific item and a specific number. option:contract_address token_id

`/txn`

enter the address and display the transaction record. option: eth_address

`/account_info`

enter the address to display ETH balance and Demi NFT balance. option: eth_address

Requirements
-----------------
**environment**

+ Python > 3.8

**packages**

+ discord
+ discord-py-slash-command
+ qrcode
+ urllib
+ json
+ asyncio
+ request
+ flask

Usage
-----------------
There are 2 ways to run this bot.
Whether you choose first or second method, you'll need [Discord bot token](https://discord.com/developers/applications) and [Etherscan API](https://etherscan.io/myapikey). If you choose the second method, you'll also need [Uptimerbot](https://uptimerobot.com/) account.

### 1.run it on repl.it(cloud)
You can run it on repl.it, just fork [it](https://replit.com/@xeiftc/Kizmeow-NFT-Tracker-V2) and run. Remember to change discord bot token and Etherscan API key, then put them in environment variable. **DO NOT PUT TOKENS IN YOUR CODE DIRECTLY** cuz repls on replit is public if you use their free plan, and there are some ppl using scrypt to grab your token.
Next, copy the link here, ![image](https://user-images.githubusercontent.com/80938768/146533872-021b05b3-f18c-44db-a943-527903dc6616.png) create a [Uptimerbot](https://uptimerobot.com/) account and paste your link here. ![image](https://user-images.githubusercontent.com/80938768/146534310-74201ab2-700e-4271-94a2-f2ecf8d12acb.png)

### 2.run it on your computer(local)
Just download [it](https://github.com/Xeift/Kizmeow-OpenSea-and-Etherscan-Discord-Bot/archive/refs/heads/main.zip) and install all the packages in **Requirement**, make sure you have install python. Remember to change discord bot token and Etherscan API key. Then, run main.py

Video Tutorial
-----------------
If you want to use different version bot, change the repl.it link I fork in the video.

https://www.youtube.com/watch?v=WFP9LdiB8yk

Official Website
-----------------
https://watercatuwu.github.io/kizmeow-nft-site/ 

by WaterCatMeow

Bot Avatar Illustrator
-----------------
[姬玥 Kiyue](https://www.facebook.com/profile.php?id=100026170072950)
![avatar](https://user-images.githubusercontent.com/80938768/146544100-315cdd44-7461-441b-a3dd-d3ee653b145a.png)
