# Kizmeow-OpenSea-and-Etherscan-Discord-Bot

A Discord bot wrote with Python. Kizmeow let you track your NFT project and display some useful information(e.g. market cap, floor price, total supply, eth price, gas fee, transaction history, display NFT owner, download original resolution NFT image...etc) by calling Etherscan and OpenSea API.

If you like this project, please give me star on the upper right corner:)

I rewrote my code and updated bot to V3, if you still need V2, it's in the `archive` folder.

V3 is more stable and faster than V2. I add buttons to the commands and replace the old library with Pycord 2.0.0, it's easier to use now. I also remove some unnecessary permissions, makes Kizmeow safer.

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

`/help` display help message

![image](https://user-images.githubusercontent.com/80938768/164337448-46de8952-c06c-444d-87a0-414273be0d44.png)

`/meow` return bot latency

![image](https://user-images.githubusercontent.com/80938768/164338206-20e35442-ce34-4d24-aa86-2d8e934e938f.png)

`/invite` invite Kizmeow to your server

![image](https://user-images.githubusercontent.com/80938768/164338268-dd8b3a89-04c6-473b-8103-f5b12d4e4f39.png)

\[NFT commands] 

`/project_realtime` display project realtime information

![image](https://user-images.githubusercontent.com/80938768/164338371-d34321e9-f0f1-4958-a3ad-3c6e93dbbf6e.png)

`/project_history` display project history information

![image](https://user-images.githubusercontent.com/80938768/164338500-c11125c9-45d9-4e39-899f-d3e0bf323282.png)

`/project_nft` display information of specific NFT

![image](https://user-images.githubusercontent.com/80938768/164338606-84142664-055a-4231-af88-a82e7598a266.png)

-------------------------------------------------------------------------------------------------------------------------------------------------

Requirements
-----------------
**environment**

+ Python > 3.8

**packages**

+ discord
+ py-cord 2.0.0b1

-------------------------------------------------------------------------------------------------------------------------------------------------

Video Tutorial
-----------------

check out the [tutorial](https://www.youtube.com/watch?v=WFP9LdiB8yk) from V2.

-------------------------------------------------------------------------------------------------------------------------------------------------

Usage
-----------------
You need [Discord bot token](https://discord.com/developers/applications). And if you want to use "send message in specific channel when there's a list or sold event of your NFT collection on OpenSea" this function, you'll also need OpenSea API key, you can apply for the API key [here](https://docs.opensea.io/reference/request-an-api-key). Fill in the google form to apply for the API key. They will send API key to your gmail in about 2 days

1. Download [it](https://github.com/Xeift/Kizmeow-OpenSea-and-Etherscan-Discord-Bot/archive/refs/heads/main.zip) and unzip it.
2. Make sure you have install python, Install all the packages in **Requirement** using `pip install PACKAGE_NAME`.
3. Remember to change discord bot token.
4. Run main.py with Visual Studio Code or Python's built-in IDLE.

-------------------------------------------------------------------------------------------------------------------------------------------------

Official Website
-----------------
https://watercatuwu.github.io/kizmeow-nft-site/ 

by WaterCatMeow

-------------------------------------------------------------------------------------------------------------------------------------------------

Bot Avatar Illustrator
-----------------
[姬玥 Kiyue](https://www.facebook.com/profile.php?id=100026170072950)
![avatar](https://user-images.githubusercontent.com/80938768/146544100-315cdd44-7461-441b-a3dd-d3ee653b145a.png)

-------------------------------------------------------------------------------------------------------------------------------------------------

Author
-----------------

Xeift#1230
