import discord
import os
from dotenv import load_dotenv

from response import get_response, mikaGPT_response

# loading the TOKEN
# The model is using the dotenv for accessing the token this will make the token safe
load_dotenv()
TOKEN = os.getenv('TOKEN')

# Specifying the intent of the bots
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# You can add a comment 'NOQA' to ignore warnings

# This is the event listener for on start.
# This function is similar to the start() function in Unity C#
@client.event
async def on_ready() -> None:
    print('We have logged in as {0.user}'.format(client))

# This function is for message event.
# If the bot register an event which is a message it will execute the functions below
@client.event
async def on_message(message):
    #This if statement checks whether the message is from ourselves.
    if message.author == client.user:
        return
    Sensei = message.author.name
    if message.content.startswith('$hello'):
        print(f"Message received: {message.content}")  # added line
        await message.channel.send('Hello!')

    if message.content.startswith('$luv'):
        print(f"Message received: {message.content}")  # added line
        await message.channel.send('I love you!')

    if message.content.startswith('$misono'):
        new_content = message.content[6:]  # Remove the '$mika' prefix
        response = get_response(new_content, Sensei)

        # Check if the response is empty or invalid
        if response and response.strip():  # Ensure it's not empty or just whitespace
            await message.channel.send(response)
        else:
            await message.channel.send("I'm sorry, I couldn't generate a response.")

    if message.content.startswith('$mikaGPT'):
        new_content = message.content[9:]  # Remove the '$mikaGPT' prefix
        mika = mikaGPT_response(new_content, Sensei)
        await message.channel.send(mika)



try:
    client.run(TOKEN)
except Exception as e:
    print(e)
