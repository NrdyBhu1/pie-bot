from discord.ext import commands
from discord import Member, Client
import discord
from card import *

class MyClient(Client):
	async def on_ready(self):
		activity = discord.Activity(type=discord.ActivityType.watching, name="Hentai")
		await self.change_presence(status=discord.Status.online, activity=activity)
		print('Logged on as ' + str(self.user))

	async def on_message(self, message):
		if message.content.lower() == "pie green card":
			await message.channel.send(file=discord.File(get_green_card(message.author.name, message.author.avatar_url, message.author.status, message.author.activity)))
		elif message.content.lower() == "pie blue card":
			await message.channel.send(file=discord.File(get_blue_card(message.author.name, message.author.avatar_url, message.author.status, message.author.activity)))
		elif message.content.lower() == "pie purp card":
			await message.channel.send(file=discord.File(get_purp_card(message.author.name, message.author.avatar_url, message.author.status, message.author.activity)))
		elif message.content.lower() == "pie yellow card":
			await message.channel.send(file=discord.File(get_yellow_card(message.author.name, message.author.avatar_url, message.author.status, message.author.activity)))
		elif message.content.lower() == "pie white card":
			await message.channel.send(file=discord.File(get_white_card(message.author.name, message.author.avatar_url, message.author.status, message.author.activity)))


		## clear
		splmsg = message.content.lower().split(" ")
		if splmsg[0] == "pie" and splmsg[1] == "clear" and len(splmsg) == 3:
			await self.clear_msgs(message.channel, int(splmsg[2]))
##			print(splmsg[2])

	async def clear_msgs(self, chnl, number):
			number = int(number)
			counter = 0
			async for x in chnl.history(limit = number):
				if counter < number:
						await x.delete()
						counter += 1


client_token = "NzcyMDMyMzk#wtf#3NTQ5NzY0#stop#NjA5.X50xMw.uQqOHGLXEZ5#scanning#X1h824YLUJG-Y5iE"
DISCORDBOT_TOKEN = client_token.split("#")

bot = MyClient()
bot.run(DISCORDBOT_TOKEN[0]+DISCORDBOT_TOKEN[2]+DISCORDBOT_TOKEN[4]+DISCORDBOT_TOKEN[6])
