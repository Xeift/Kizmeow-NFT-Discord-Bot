# Kizmeow-OpenSea-and-Etherscan-Discord-Bot

### [中文版](https://github.com/Xeift/Kizmeow-OpenSea-and-Etherscan-Discord-Bot/blob/main/%E8%AE%80%E6%88%91.md) | [English Ver](https://github.com/Xeift/Kizmeow-OpenSea-and-Etherscan-Discord-Bot/blob/main/README.md)
A Discord bot wrote with Python. Kizmeow let you track your NFT project and display some useful information(e.g. market cap, floor price, total supply, eth price, gas fee, transaction history, display NFT owner, download original resolution NFT image...etc) by calling Etherscan and OpenSea API.(This repl is in development)


This repl is not finish yet. If you want to try, you can invite the bot to your test server.

[Chinese bot](https://discord.com/api/oauth2/authorize?client_id=886198731328868402&permissions=534727097920&scope=bot%20applications.commands) | [English bot](https://discord.com/api/oauth2/authorize?client_id=886198731328868402&permissions=534727097920&scope=bot%20applications.commands)

I will make a more detailed tutorial later:)

Note
-----------------
If you no nothing about coding, I suggest you contact me via Discord Xeift#1230, I can create customize bot for your project for free.
Or you can just simply invite the bot to your server.

[Chinese bot](https://discord.com/api/oauth2/authorize?client_id=886198731328868402&permissions=534727097920&scope=bot%20applications.commands) | [English bot](https://discord.com/api/oauth2/authorize?client_id=886198731328868402&permissions=534727097920&scope=bot%20applications.commands)

You can use the commands listed below

`/demi-human`

display real-time price of Demi-Human.

`/demi-human-history`

display history price of Demi-Human.

`/demi-nft`

search specific Demi-Human NFT by token id. option: token_id

`/project`

display real-time price of specific project. option:project_name

`/project-history`

display history price of specific project. option:project_name

`/nft`

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

### 1.run it on repl.it
You can run it on repl.it, just fork [it](https://replit.com/@Kizmeow-NFT-Tracker) and run. Remember to change discord bot token, OpenSea API token, Etherscan API key and guild id and put them in environment variable. **DO NOT PUT TOKENS IN YOUR CODE DIRECTLY** cuz repls on replit is public if you use their free plan, and there are some ppl using scrypt to grab your token.
Next, copy the link here, ![image](https://user-images.githubusercontent.com/80938768/146533872-021b05b3-f18c-44db-a943-527903dc6616.png) create a [Uptimerbot](https://uptimerobot.com/) account and paste your link here. ![image](https://user-images.githubusercontent.com/80938768/146534310-74201ab2-700e-4271-94a2-f2ecf8d12acb.png)

### 2.run it on your computer
Just download [it](https://github.com/Xeift/Kizmeow-OpenSea-and-Etherscan-Discord-Bot/archive/refs/heads/main.zip) and install all the packages in **Requirement**, make sure you have install python. Remember to change discord bot token, OpenSea API token , Etherscan API key and giild id. Then, run main.py

Tutorial
-----------------
not finished yet:/

Bot Avatar Illustrator
-----------------
[姬玥 Kiyue](https://www.facebook.com/profile.php?id=100026170072950)
![avatar](https://user-images.githubusercontent.com/80938768/146544100-315cdd44-7461-441b-a3dd-d3ee653b145a.png)
