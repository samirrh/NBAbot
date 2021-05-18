import os
import requests
import discord
from bs4 import BeautifulSoup
from discord.ext import commands
bot = commands.Bot(command_prefix='$')

import random

#embed=discord.Embed(title="Player of the Week", url='https://basketball.realgm.com/nba/awards/by-type/Player-Of-The-Week/30', color=0x159619)
def get_pow():
  url = 'https://basketball.realgm.com/nba/awards/by-type/Player-Of-The-Week/30'
  embed=discord.Embed(title="Player of the Week", url='https://basketball.realgm.com/nba/awards/by-type/Player-Of-The-Week/30', color=0x159619)
  response = requests.get(url)
  playersInfo = {
    'date':'',
    'East':{
      'name':'',
      'team':'',
      'pos':'',
      'age':'',
    },
    'West':{
      'name':'',
      'team':'',
      'pos':'',
      'age':'',
    }
  }
  soup = BeautifulSoup(response.content, 'html.parser')
  table = soup.find('table', attrs={'class':'tablesaw','data-tablesaw-mode':'swipe'}).tbody
  trs = table.find_all('tr')
  for count, tr in enumerate(trs):
    if count<2:
      tds = tr.find_all('td')
      playersInfo['date']=tds[3].text
      playersInfo[tds[2].text]['name']=tds[1].text
      playersInfo[tds[2].text]['team']=tds[4].text
      playersInfo[tds[2].text]['pos']=tds[5].text
      playersInfo[tds[2].text]['age']=tds[8].text
  embed.add_field(name="Eastern Conference Player of the Week", value=playersInfo['East']['name'], inline=False)
  embed.add_field(name="Eastern Conference Player of the Week - "+playersInfo['date'], value=playersInfo['East']['name'], inline=False)
  #embed.set_thumbnail(url="https://i.imgur.com/axLm3p6.jpeg")
  #embed.set_image(url="https://www.basketball-reference.com/req/202104203/images/players/tatumja01.jpg")
  #embed.set_image(url="https://www.basketball-reference.com/req/202104203/images/players/bookede01.jpg")
  embed.add_field(name="Team", value=playersInfo['East']['team'], inline=True)
  embed.add_field(name="Position", value=playersInfo['East']['pos'], inline=True)
  embed.add_field(name="Age", value=playersInfo['East']['age'], inline=True)
  embed.add_field(name="Western Conference Player of the Week", value=playersInfo['West']['name'], inline=False)
  embed.add_field(name="Team", value=playersInfo['West']['team'], inline=True)
  embed.add_field(name="Position", value=playersInfo['West']['pos'], inline=True)
  embed.add_field(name="Age", value=playersInfo['West']['age'], inline=True)
  return embed

#refactor function 
def get_powWest(weeksAgo):
  if weeksAgo == 0:
    targetIndex = 1
  else:
    targetIndex = weeksAgo*2+1
  statURL = 'https://basketball.realgm.com/nba/awards/by-type/Player-Of-The-Week/30'
  embed=discord.Embed(title="Western Conference Player of the Week", url=statURL, color=0x159619)
  response = requests.get(statURL)
  playerInfo = {
    'date':'',
    'name':'',
    'team':'',
    'pos':'',
    'age':''
  }
  soup = BeautifulSoup(response.content, 'html.parser')
  table = soup.find('table', attrs={'class':'tablesaw','data-tablesaw-mode':'swipe'}).tbody
  trs = table.find_all('tr')
  for index, tr in enumerate(trs):
    if index == targetIndex:
      print(index)
      tds = tr.find_all('td')
      playerInfo['date']=tds[3].text
      playerInfo['name']=tds[1].text
      playerInfo['team']=tds[4].text
      playerInfo['pos']=tds[5].text
      playerInfo['age']=tds[8].text
    elif index > targetIndex:
      print(index)
      break
    else:
      print(index)
      continue
  urlId = playerInfo['name'].split()[1].lower()[:5] + playerInfo['name'].split()[0].lower()[:2] + '01.jpg'
  embed.add_field(name="Name", value=playerInfo['name'], inline=False)
  embed.add_field(name="Team", value=playerInfo['team'], inline=True)
  embed.add_field(name="Position", value=playerInfo['pos'], inline=True)
  embed.add_field(name="Age", value=playerInfo['age'], inline=True)
  embed.set_image(url="https://www.basketball-reference.com/req/202104203/images/players/" + urlId)
  if weeksAgo > 0:
    embed.set_footer(text='Player of the Week Recipient on ' + playerInfo['date'] + ' - ' + 'Approx '+str(weeksAgo)+' weeks ago.')
  return embed

def get_powEast():
  random_number = random.randint(0,167776)
  randomColor = random_number
  url = 'https://basketball.realgm.com/nba/awards/by-type/Player-Of-The-Week/30'
  embed=discord.Embed(title="Eastern Conference Player of the Week", url=url, color=randomColor)
  response = requests.get(url)
  playerInfo = {
    'name':'',
    'team':'',
    'pos':'',
    'age':''
  }
  soup = BeautifulSoup(response.content, 'html.parser')
  table = soup.find('table', attrs={'class':'tablesaw','data-tablesaw-mode':'swipe'}).tbody
  trs = table.find_all('tr')
  for count, tr in enumerate(trs):
    if count == 0:
      print(count)
      tds = tr.find_all('td')
      playerInfo['name']=tds[1].text
      playerInfo['team']=tds[4].text
      playerInfo['pos']=tds[5].text
      playerInfo['age']=tds[8].text
    elif count > 0:
      print(count)
      break
    else:
      print(count)
      continue
  urlId = playerInfo['name'].split()[1].lower()[:5] + playerInfo['name'].split()[0].lower()[:2] + '01.jpg'
  embed.add_field(name="Name", value=playerInfo['name'], inline=False)
  embed.add_field(name="Team", value=playerInfo['team'], inline=True)
  embed.add_field(name="Position", value=playerInfo['pos'], inline=True)
  embed.add_field(name="Age", value=playerInfo['age'], inline=True)
  embed.set_image(url="https://www.basketball-reference.com/req/202104203/images/players/" + urlId)
  return embed


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.command()
async def ECpow(ctx, arg=0):
    await ctx.send(embed=get_powEast())

@bot.command()    
async def WCpow(ctx, arg=0):
    await ctx.send(embed=get_powWest(arg))

@bot.command()
async def NBApow(ctx):
    await ctx.send(embed=get_pow())

bot.run(os.environ['TOKEN'])

