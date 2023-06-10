import discord
from random import choice

def get_random_gif(gifs):
    return choice(gifs)

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # Find the channel named general in the message guild
    general_channel = discord.utils.get(message.guild.channels, name="demonologist-general-chat")

    # Check if the message was sent in the general channel
    if message.channel == general_channel:
        gif = get_random_gif([
            "https://tenor.com/view/pancake-gif-26384818",
            "https://tenor.com/view/pancakes-pancake-pancake-day-breakfast-shrove-tuesday-gif-20352113",
            "https://tenor.com/view/pancakes-food-breakfast-syrup-pancake-day-gif-16416592",
            "https://tenor.com/view/pancakes-food-breakfast-syrup-pancake-day-gif-16416605",
            "https://tenor.com/view/pancakes-food-breakfast-yummy-pancake-day-gif-16416582",
            "https://tenor.com/view/pancakes-food-breakfast-brunch-pancake-gif-16416337"
        ])

        await message.channel.send(gif)

try:
    client.run("my-token-here")
except Exception as e:
    print(e)
