import discord
import os
import requests
import random
from keep_alive import keep_alive

#create an instance of the discord api
client = discord.Client()


def return_doge():
  r = requests.get('https://dog.ceo/api/breeds/image/random')
  response = r.json()
  response = response ['message']
  return response


def image_search(query):
  r = requests.get("https://api.qwant.com/api/search/images",
    params={
        'count': 200,
        'q': query,
        't': 'images',
        'safesearch': 0,
        'locale': 'en_US',
        'uiv': 4
    },
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    }
    )

  response = r.json().get('data').get('result').get('items')
  urls = [r.get('media') for r in response]

  image = random.choice(urls)

  return image



#start up event
@client.event
async def on_ready():
  print("We have connected as {0.user}".format(client))

#message events
@client.event
async def on_message(message):
  if message.author == client:
    return

  msg = message.content

    #response message
  if msg.startswith("//hello"):
    await message.channel.send(f'Whats up {message.author}')

    #return a dog image
  if msg == "//doge":
    doge = return_doge()
    await message.channel.send(doge)

#return queried image_search
  if msg.startswith("//search"):
    query = msg.split('//search ',1)[1]
    picture = image_search(query)
    await message.channel.send(picture)

#keep the server alive
keep_alive()


#run the bot
client.run(os.getenv('TOKEN'))


import requests

r = requests.get('https://dog.ceo/api/breeds/image/random')

response = r.json()

response = response['message']

print(response)