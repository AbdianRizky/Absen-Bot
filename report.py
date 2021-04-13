import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

class SendReportToDiscord(discord.Client):
  async def on_ready(self):
    print('Logged on as {0}!'.format(self.user))

  async def on_message(self, message):
    print('Message from {0.author}: {0.content}'.format(message))
    if message.author == self.user:
      return

    if message.content.startswith('$hello'):
      await message.channel.send('Hello!')

report = SendReportToDiscord()
report.run(TOKEN)


