import discord
from timer_checker import main_loop
import parser_local
import files
import commands
import json

def load_config():
    with open('config.json', 'r+') as f:
        return json.load(f)


client = discord.Client()

@client.event
async def on_ready():
    print('logged in')
    me = client.get_user(load_config()['author'])
    await me.send('logged in')
    print(client.users)
    await main_loop(client)


@client.event
async def on_message(message):
    global client
    msg = message
    cha = msg.channel
    par = parser_local.parse_message(message.content)
    if par[0] == 'rem':
        await commands.load_commands(msg, msg.author, par, client)



client.run(load_config()['secret'])