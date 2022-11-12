# Kizmeow-NFT-Discord-Bot

A Discord bot develop with Python. Kizmeow let you track your NFT project and display useful information(e.g. market cap, floor price, total supply, eth price, gas fee, transaction history, NFT owner, download original resolution NFT image...etc) by calling Etherscan and OpenSea API.

If you like this project, please give me star on the upper right corner :)

[Kizmeow NFT Tracker V3 invite link](https://discord.com/api/oauth2/authorize?client_id=923512417907015693&permissions=277025508352&scope=applications.commands%20bot)

If you no nothing about coding, you can just simply click the blue letter above and invite the bot to your server.

-------------------------------------------------------------------------------------------------------------------------------------------------

[system commands]

`/help` display help message

![image](https://user-images.githubusercontent.com/80938768/164337448-46de8952-c06c-444d-87a0-414273be0d44.png)

`/meow` return bot latency

![image](https://user-images.githubusercontent.com/80938768/164338206-20e35442-ce34-4d24-aa86-2d8e934e938f.png)

`/invite` invite Kizmeow to your server

![image](https://user-images.githubusercontent.com/80938768/164338268-dd8b3a89-04c6-473b-8103-f5b12d4e4f39.png)

[NFT commands] 

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

check out the [tutorial](https://www.youtube.com/watch?v=WFP9LdiB8yk) from V2 if you want to host the bot by yourself.

-------------------------------------------------------------------------------------------------------------------------------------------------

Usage
-----------------
You need [Discord bot token](https://discord.com/developers/applications)

1. Download [it](https://github.com/Xeift/Kizmeow-OpenSea-and-Etherscan-Discord-Bot/archive/refs/heads/main.zip) and unzip it.
2. Make sure you have install python, Install all the packages in **Requirement** using `pip install PACKAGE_NAME`.
3. Remember to change discord bot token.
4. Run config.py with Visual Studio Code or Python's built-in IDLE, enter your Etherscan API key and Discord bot token to configure your bot.
5. Run main.py with Visual Studio Code or Python's built-in IDLE to start the bot.

-------------------------------------------------------------------------------------------------------------------------------------------------

FAQ
-----------------
Why did I see "The application did not respond"?


![image](https://user-images.githubusercontent.com/80938768/174103309-8c31a358-8078-40bb-b0b2-7b19b6509548.png)

1. The collection is too new
2. The collection is not on ETH Mainnet(Polygon, Solana). Currently, Kizmeow only support NFTs on Mainnet.
3. You entered wrong parameter. For example, you use `/project_nft` command, entered `0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d` and `45678` as parameter. Since there 's no BAYC#45678, your command failed.
4. My old pc shutdown for some reason. Very likely because of the fucking win10 update.

What is `collection_slug`?


collection_slug is the text at the end of OpenSea collection url

![image](https://user-images.githubusercontent.com/80938768/155941533-a9e86c86-54e5-4708-b1fe-0b05ca48033c.png)
-------------------------------------------------------------------------------------------------------------------------------------------------


Bot Avatar Illustrator
-----------------
[姬玥 Kiyue](https://www.facebook.com/profile.php?id=100026170072950)
![avatar](https://user-images.githubusercontent.com/80938768/146544100-315cdd44-7461-441b-a3dd-d3ee653b145a.png)

-------------------------------------------------------------------------------------------------------------------------------------------------

Author
-----------------

`xeift.eth` (Xeift#1230)

`c0mradΞ.eth` (c0mradΞ.eth#0084)
