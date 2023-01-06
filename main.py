import discord
import asyncio
import requests
from discord.ext.commands import Bot
from discord.ext import commands
import datetime
import time
#readable = time.ctime(1668696846)


PREFIX = ("-")
intents = discord.Intents.default()
intents.members = True
help_command = commands.DefaultHelpCommand(
    no_category = 'Commands'
)
bot = commands.Bot(case_insensitive=True,intents=intents, command_prefix=PREFIX,help_command = help_command)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="your house"))
    print("on!")
    
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        print('Missing argument')

@bot.command()
async def btc(ctx):
    """ Shows current price of BTC"""
    price = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD').json()["USD"]
    pricey = str(price)
    msg = pricey + ' USD'
    await ctx.send('*'+msg+'*')
       

@bot.command()
async def btcb(ctx, what):
    """ Shows wallet balance of bitcoin wallet"""
    total = requests.get('https://blockchain.info/q/addressbalance/' + what)
    count = int(total.text)
    bal = str(count/100000000)
    msg = bal + ' BTC'
    await ctx.send('*'+msg+'*')
          
@bot.command()
async def eth(ctx):
    """ Shows current price of ETH"""
    price = requests.get('https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD').json()["USD"]
    pricey = str(price)
    msg = pricey + ' USD'
    await ctx.send('*'+msg+'*')
    
@bot.command()
async def ethb(ctx, what):
    """ Shows wallet balance of ethereum wallet"""
    total = requests.get('https://api-eu1.tatum.io/v3/ethereum/account/balance/' + what).json()['balance']
    bal = str(total)
    msg = bal + ' ETH'
    await ctx.send('*'+msg+'*')
    
@bot.command()
async def ltc(ctx):
    """ Shows current price of LTC"""
    price = requests.get('https://min-api.cryptocompare.com/data/price?fsym=LTC&tsyms=USD').json()["USD"]
    pricey = str(price)
    msg = pricey + ' USD'
    await ctx.send('*'+msg+'*')
    
@bot.command()
async def xmr(ctx):
    """ Shows current price of XMR"""
    price = requests.get('https://min-api.cryptocompare.com/data/price?fsym=XMR&tsyms=USD').json()["USD"]
    pricey = str(price)
    msg = pricey + ' USD'
    await ctx.send('*'+msg+'*')

@bot.command()
async def dbdsi(ctx, *what):
    """ Shows info about survivor in Dead by Daylight"""
    sur = ''.join(what)
    res = requests.get('https://dead-by-api.herokuapp.com/api/survs/' + sur)
    av = res.json()['data'][0]['imgs']['portrait']
    name = res.json()['data'][0]['name']
    licensed = res.json()['data'][0]['licensed']
    dif = res.json()['data'][0]['difficulty']
    nat = res.json()['data'][0]['nationality']
    dlc = res.json()['data'][0]['dlc']
    prk = res.json()['data'][0]['perks_names']
    img = res.json()['data'][0]['imgs']['store']
    rl = res.json()['data'][0]['role']
    embed = discord.Embed(title=f"{name}", description="Survivor Information", color=0x000000)
    embed.add_field(name='Licensed', value=f"{licensed}", inline=True)
    embed.add_field(name='Difficulty', value=f"{dif}", inline=True)
    embed.add_field(name='Role', value=f"{rl}", inline=True)
    embed.add_field(name='Nationality', value=f"{nat}", inline=True)
    embed.add_field(name='DLC', value=f"{dlc}", inline=True)
    embed.add_field(name='Perks', value=f"{prk}", inline=True)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_image(url=img)
    embed.set_thumbnail(url=av)
    embed.set_footer(text=f'{ctx.author.name}', icon_url=ctx.message.author.avatar_url)
    #print(av)
    await ctx.send(embed=embed)
    
@bot.command()
async def dbdki(ctx, *what):
    """ Shows info about killer in Dead by Daylight"""
    kil = ''.join(what)
    res = requests.get('https://dead-by-api.herokuapp.com/api/killers/the' + kil)
    av = res.json()['data'][0]['imgs']['portrait']
    name = res.json()['data'][0]['fullName']
    licensed = res.json()['data'][0]['licensed']
    dif = res.json()['data'][0]['difficulty']
    nat = res.json()['data'][0]['nationality']
    dlc = res.json()['data'][0]['dlc']
    prk = res.json()['data'][0]['perks_names']
    img = res.json()['data'][0]['imgs']['store']
    rl = res.json()['data'][0]['realm']
    pat = res.json()['data'][0]['powerAttackType']
    wp = res.json()['data'][0]['weapon']
    ms = res.json()['data'][0]['moveSpeed']
    tr = res.json()['data'][0]['terrorRadius']
    hg = res.json()['data'][0]['height']
    embed = discord.Embed(title=f"{name}", description="Survivor Information", color=0x000000)
    embed.add_field(name='Licensed', value=f"{licensed}", inline=True)
    embed.add_field(name='Difficulty', value=f"{dif}", inline=True)
    embed.add_field(name='Realm', value=f"{rl}", inline=True)
    embed.add_field(name='Nationality', value=f"{nat}", inline=True)
    embed.add_field(name='DLC', value=f"{dlc}", inline=True)
    embed.add_field(name='Power Attack Type', value=f"{pat}", inline=True)
    embed.add_field(name='Weapon', value=f"{wp}", inline=True)
    embed.add_field(name='Movement Speed', value=f"{ms}", inline=True)
    embed.add_field(name='Terror Radius', value=f"{tr}", inline=True)
    embed.add_field(name='Height', value=f"{hg}", inline=True)
    embed.add_field(name='Perks', value=f"{prk}", inline=True)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_image(url=img)
    embed.set_thumbnail(url=av)
    embed.set_footer(text=f'{ctx.author.name}', icon_url=ctx.message.author.avatar_url)
    #print(av)
    await ctx.send(embed=embed)




@bot.command()
async def dbdid(ctx):
    """ Shows ItemID for item from Dead by Daylight"""
    res = requests.get('https://dead-by-api.herokuapp.com/api/items?fields=code')
    flash = res.json()['data'][0]['code']
    i1 = res.json()['data'][1]['code']
    i2 = res.json()['data'][2]['code']
    i3 = res.json()['data'][3]['code']
    i4 = res.json()['data'][4]['code']
    i5 = res.json()['data'][5]['code']
    i6 = res.json()['data'][6]['code']
    i7 = res.json()['data'][7]['code']
    i8 = res.json()['data'][8]['code']
    i9 = res.json()['data'][9]['code']
    i10 = res.json()['data'][10]['code']
    i11 = res.json()['data'][11]['code']
    i12 = res.json()['data'][12]['code']
    i13 = res.json()['data'][13]['code']
    i14 = res.json()['data'][14]['code']
    i15 = res.json()['data'][15]['code']
    i16 = res.json()['data'][16]['code']
    i17 = res.json()['data'][17]['code']
    i18 = res.json()['data'][18]['code']
    i19 = res.json()['data'][19]['code']
    i20 = res.json()['data'][20]['code']
    i21 = res.json()['data'][21]['code']
    i22 = res.json()['data'][22]['code']
    i23 = res.json()['data'][23]['code']
    i24 = res.json()['data'][24]['code']
    i25 = res.json()['data'][25]['code']
    i26 = res.json()['data'][26]['code']
    i27 = res.json()['data'][27]['code']
    i28 = res.json()['data'][28]['code']
    i29 = res.json()['data'][29]['code']
    i30 = res.json()['data'][30]['code']
    i31 = res.json()['data'][31]['code']
    
    embed = discord.Embed(title=f"Items", description="Item IDS", color=0x000000)
    embed.add_field(name='Ids', value=f"{flash},{i1},{i2},{i3},{i4},{i5},{i6},{i7},{i8},{i9},{i10},{i11},{i12},{i13},{i14},{i15},{i16},{i17},{i18},{i19},{i20},{i21},{i22},{i23},{i24},{i25},{i26},{i27},{i28},{i29},{i30},{i31}", inline=True)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'{ctx.author.name}', icon_url=ctx.message.author.avatar_url)
    #print(av)
    await ctx.send(embed=embed)
    
    
    

@bot.command()
async def dbdii(ctx, what):
    """ Shows info about Item in Dead by Daylight"""
    res = requests.get('https://dead-by-api.herokuapp.com/api/items/' + what)
    name = res.json()['data'][0]['name']
    #print(name)
    rar = res.json()['data'][0]['rarity']
    des = res.json()['data'][0]['description']
    img = res.json()['data'][0]['icon']
    embed = discord.Embed(title=f"{name}", description="Item Information", color=0x000000)
    embed.add_field(name='Rarity', value=f"{rar}", inline=True)
    embed.add_field(name='Description', value=f"{des}", inline=True)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_thumbnail(url=img)
    embed.set_footer(text=f'{ctx.author.name}', icon_url=ctx.message.author.avatar_url)
    await ctx.send(embed=embed)

@bot.command()
async def dbdrr(ctx):
    """ Shows info about Rank Reset in Dead by Daylight"""
    res = requests.get('https://dbd.tricky.lol/api/rankreset')
    resets = res.json()['rankreset']
    dat = time.ctime(resets)
    #print(name)
    embed = discord.Embed(title=f"Rank Reset", description="Date Info", color=0x000000)
    embed.add_field(name='Resets at:', value=f"{dat}", inline=True)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'{ctx.author.name}', icon_url=ctx.message.author.avatar_url)
    await ctx.send(embed=embed)

@bot.command()
async def dbdsos(ctx):
    """ Shows Shrine of Secrets in Dead by Daylight"""
    res = requests.get('https://dbd.tricky.lol/api/shrine')
    
    perk1 = res.json()['perks'][0]['id']
    perk12 = res.json()['perks'][1]['id']
    perk13 = res.json()['perks'][2]['id']
    perk14 = res.json()['perks'][3]['id']
    
    ress = requests.get('https://dbd.tricky.lol/api/perkinfo?perk=' + perk1 +'&pretty')
    ress1 = requests.get('https://dbd.tricky.lol/api/perkinfo?perk=' + perk12 +'&pretty')
    ress2 = requests.get('https://dbd.tricky.lol/api/perkinfo?perk=' + perk13 +'&pretty')
    ress3 = requests.get('https://dbd.tricky.lol/api/perkinfo?perk=' + perk14 +'&pretty')
    
    perks1 = ress.text.replace('&nbsp;', '')
    perks2 = ress1.text.replace('&nbsp;', '')
    perks3 = ress2.text.replace('&nbsp;', '')
    perks4 = ress3.text.replace('&nbsp;', '')
    resets = res.json()['end']
    dat = time.ctime(resets)
    
 
        
       
    embed = discord.Embed(title=f"Shrine of Secrets", description=f"**Ends at** {dat}", color=0x000000)
    embed.add_field(name=f'{perk1}', value=f"{perks1}", inline=True)
    embed.add_field(name=f'{perk12}', value=f"{perks2}", inline=True)
    embed.add_field(name=f'{perk13}', value=f"{perks3}", inline=True)
    embed.add_field(name=f'{perk14}', value=f"{perks4}", inline=True)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'{ctx.author.name}', icon_url=ctx.message.author.avatar_url)
    await ctx.send(embed=embed)

@bot.command()
async def serverinfo(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="Server Information", color=0x000000)
    embed.timestamp = datetime.datetime.utcnow()
    embed.add_field(name='Server ID', value=f"{ctx.guild.id}", inline=True)
    embed.add_field(name='Created On', value=ctx.guild.created_at.strftime("%b %d %Y"), inline=True)
    embed.add_field(name='Owner', value=f"{ctx.guild.owner.mention}", inline=True)
    embed.add_field(name='Members', value=f'{ctx.guild.member_count} Members', inline=True)
    embed.add_field(name='Channels', value=f'{len(ctx.guild.text_channels)} Text | {len(ctx.guild.voice_channels)} Voice', inline=True)
    embed.add_field(name='Region', value=f'{ctx.guild.region}', inline=True)
    #embed.set_thumbnail(url=ctx.guild.icon_url) 
    embed.set_footer(text=f'{ctx.author.name}', icon_url=ctx.message.author.avatar_url)    
    await ctx.send(embed=embed)
    
bot.run('')
