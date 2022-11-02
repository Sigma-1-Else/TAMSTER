import keep_alive
import discord
import os
import time
import discord.ext
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, CheckFailure, check
import math
from mpmath import csc as csc
import sys

#^ basic imports for other features of discord.py and python ^

client = discord.Client()

client = commands.Bot(command_prefix='!')  #put your own prefix here



@client.event
async def on_ready():
    #will print "bot online" in the console when the bot is online
  print('bot online')
  channel = client.get_channel(896125546398883872)
  await channel.send('https://tenor.com/view/tam-online-online-tam-gif-22232645')

client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=str(len(client.guilds))+ ' servers with the boyz'))


@client.command()
async def ping(ctx):
    print(ctx)
    print(type(ctx))
    await ctx.send(
        "pong!"
    )  #simple command so that when you type "!ping" the bot will respond with "pong!"

#constants
g = 9.8 #m/s^2
G = 6.67408 #10^-11 m^3 kg^-1 s^-2


@client.command(name="hp",aliases=["h","hlep"])
async def hp(ctx):
  embed = discord.Embed(title="Tamster Help", description="This bot was made to do lawncapper questions. Call the command of the question then add the given values seperated by spaces to be calculated.", color=0xFF5733)
  embed = embed.set_author(name=ctx.author.display_name, url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
icon_url=ctx.author.avatar_url)
  embed = embed.add_field(
        name="Lawncapper Questions",
        value=
        "Contains a list of the added questions and their format. Format: !lawncapper [page #(1 is default)]Command: !lawncapper, alt commands:!lc, !loncapa,!lawncapapa",
        inline=False)
  await ctx.send(embed = embed)

@client.command(name="servercount",aliases=['sc','servers','server','count'])
async def servercount(ctx):
  await client.change_presence(game=discord.Game(name="on " + str(len(client.guilds)) + " Servers.", type=0))
  await ctx.send("I'm in " + str(len(client.guilds)) + " servers!")

@client.command(name="lawncapper",
                aliases=["lc", "lawn", "loncapa", "lawncapapa"])
async def lawncapper(ctx,page=1):
  pg = str(page)
  print(pg)
  embed = discord.Embed(
        title="Lawncapper Questions",
        url="",
        description=
        "These are the added questions so far, ping Jay for adding more.",
        color=0xFF5733)
  embed = embed.set_author(name=ctx.author.display_name, url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", icon_url=ctx.author.avatar_url)
  if pg == '1':
    embed = embed.add_field(name="Pages",value="Page 1 of 2", inline=False)
    embed = embed.add_field(
        name="Car and Truck",
        value=
        "format = !carandtruck [truckspeed] [thetar] [distance]\nalternate commands = !ct, !cartruck, !truck",
        inline=False)
    embed = embed.add_field(
        name="Two Arrows Shot Upward",
        value=
        "format = !twoarrows [velocity of 1st arrow] [time between arrows]\nalternate commands = !2arrows,!arrow,!arrows,!2a,!ta",
        inline=False)
    embed = embed.add_field(
        name="Distance to Horizon",
        value=
        "format = !distancetohorizon [height] [radius]\nalternate commands = !dh,!dth,!disttohorizon,!horizon",
        inline=False)
    embed = embed.add_field(
        name="Big Bird Acceleration",
        value=
        "format = !bigbirdacceleration [initial speed] [final speed] [v1] [v2]\nalternate commands = !bba,!bigbird,!ba,!birdacceleration",
        inline=False)
    embed = embed.add_field(
        name="Accelerating Runners",
        value=
        "format = !acceleratingrunners [dist] [acc1] [acc2]\nalternate commands = !ar,!rugbyplayers,!rb",
        inline=False)
    embed = embed.add_field(
        name="Rising Balloon Drop Item",
        value=
        "format = !risingballoondropitem [velocity] [distance]\nalternate commands = !rbdi,!balloon,!risingballoon,!balloondrop,!balloondropitem" ,
        inline=False)
    embed = embed.add_field(
        name="Bear Chases Tourist",
        value=
        "format = !bearchasestourist [touristspeed] [distancebetween] [moosespeed]\nalternate commands = !moosechasestourists,!bct,!mct,!bearchase,!moosechase,!touristchase" ,
        inline=False)
  elif pg == '2':
    embed = embed.add_field(name="Pages",value="Page 2 of 2", inline=False)
    embed = embed.add_field(
        name="2D Vector combination",
        value=
        "format = !2dvectorcombination [coeffecient1] [vector1firstval] [vector1secondval] [leadingsignandcoeffecient2] [vector2firstval] [vector2secondval] with fraction values as decimals\n alternate commands = !2vc, !2dvc, !twovectorcomb" ,
        inline=False)
    embed = embed.add_field(
        name="Applied Trig Problem",
        value=
        "format = !appliedtrig [height] [deg]\n alternate commands = !at, !apptrig, !buildingindistance, !bid" ,
        inline=False)
    embed = embed.add_field(
        name="Vector Magnitude Problem",
        value=
        "format = !vectormagnitude [vector1stval] [vector2ndval] [vector3rd](0 if none provided)\n alternate commands = !vectormag, !vm, !vecmag" ,
        inline=False)
    embed = embed.add_field(
        name="Vector Dot Product Problem",
        value=
        "format = !vectordotproduct [vector1 1stval] [vector1 2ndval] [vector1 1stval] [vector1 2ndval]\n alternate commands = !vectordp, !vdp, !vecdotprod",
        inline=False)
    embed = embed.add_field(
        name="Airplane Takeoff Problem",
        value=
        "format = !airplanetakeoff [airplane mass] [airplane force] [pilot mass]\n alternate commands = !planetakeoff, !apto, !pt",
        inline=False)
    embed = embed.add_field(
        name="Roof Tile Falling Problem",
        value=
        "format = !rooftilefalling [time] [height]\n alternate commands = !tilefalling, !rooftile, !rtf",
        inline=False)
    embed = embed.add_field(
        name="Vector Cross Product Problem",
        value=
        "format = !vectorcrossproduct [vector1 1stval] [vector1 2ndval] [vector1 3rdval] [vector2 1stval] [vector2 2ndval] [vector2 3rdval]\n alternate commands = !vectorcp, !vcp, !veccrossprod",
        inline=False)
    embed = embed.add_field(
        name="Right Triangle Problem",
        value=
        "format = !righttriangle [hypotenuse] [angleα]\n alternate commands = !rt, !hypotenuseangle, !triangle",
        inline=False)
    embed = embed.add_field(
        name="Two Balloons Problem",
        value=
        "format = !twoballoons [h1] [h2] [angleα]\n alternate commands = !tb, !balloons, !2balloons, !2b",
        inline=False)
    embed = embed.add_field(
        name="Antenna Height Problem",
        value=
        "format = !antennaheight [dist] [angbase] [angtop]\n alternate commands = !ah, !antheight",
        inline=False)
    embed = embed.add_field(
      name = "Period with mass and force constant equation T=2π√(m/k)", value = "format: !period [T(e if not given)] [M(e if not given)] [K(e if not given)]", inline = False
    )
  else:
    embed = embed.add_field(name="Invalid field",value="We only have 2 pages currently",inline=False)
  embed=embed.set_thumbnail(url="https://media.discordapp.net/attachments/899181574535389234/919977550137147472/Screenshot_2021-12-13_7.37.58_AM.png")
  await ctx.send(embed=embed)

@client.command(name="period")
async def period(ctx,t,m,k):
  lst = [t,m,k]
  x = lst.index('e')
  lst.remove('e')

  embed = discord.Embed(title="Period with mass and force constant")
  embed = embed.set_author(name=ctx.author.display_name, url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ", icon_url=ctx.author.avatar_url)
  if x==0:
    ans = round(2*math.pi()*math.sqrt(float(m)/float(k)),2)
  elif x==1:
    ans = "not done"
    embed = embed.add_field(name="Answer", value= "The mass is " + str(ans) + " .", inline=False)
  elif x==2:
    ans = round(4*m*math.pi()^2/t^2,2)
    embed = embed.add_field(name="Answer", value= "The spring constant is " + str(ans) + " .", inline=False)
  else:
    ans = "didn't work"
    embed = embed.add_field(name="Answer", value= str(ans) + " .", inline=False)
  
  embed = embed.set_thumbnail(url="https://media.discordapp.net/attachments/899181574535389234/919977550137147472/Screenshot_2021-12-13_7.37.58_AM.png")
  await ctx.send(embed=embed)

@client.command(name="twoballoons",aliases=["tb",'balloons','2balloons','2b'])
async def twoballoons(ctx,h1,h2,ang):
  try:
    h1 = float(h1)
    h2 = float(h2)
    ang = float(ang)

    h = h2-h1

    #tan ang = h/x
    #x = h/tan ang

    x = round(h/math.tan(math.radians(ang)),2)

    #sin ang = h/hyp
    #hyp = h/sin ang
    hyp = round(h/math.sin(math.radians(ang)),2)

    embed = discord.Embed(title="Two Balloons Problem")
    embed = embed.set_author(name=ctx.author.display_name, url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ", icon_url=ctx.author.avatar_url)
    embed = embed.add_field(name="Horizontal Distance b/w Balloons", value= "The horizontal distance between the balloons is " + str(x) + " .", inline=False)
    embed = embed.add_field(name="Total Distance b/w Balloons", value= "The total distance between the balloons is " + str(hyp) + " .", inline=False)
    embed = embed.set_thumbnail(url="https://media.discordapp.net/attachments/899181574535389234/919977550137147472/Screenshot_2021-12-13_7.37.58_AM.png")
    await ctx.send(embed=embed)
  except:
    await ctx.send("Use format !twoballoons [h1] [h2] [angleα]")

@client.command(name="vectorcrossproduct",aliases=["vectorcp",'vcp','veccrossprod'])
async def vectorcrossproduct(ctx,v1a,v1b,v1c,v2a,v2b,v2c):
  try:
    v1a = float(v1a)
    v2a = float(v2a)
    v1b = float(v1b)
    v2b = float(v2b)
    v1c = float(v1c)
    v2c = float(v2c)

    ans1 = round(v1b * v2c - v1c * v2b,2)
    ans2 = round(v1c * v2a - v1a * v2c,2)
    ans3 = round(v1a * v2b - v1b * v2a,2)

    embed = discord.Embed(title="Vector Cross Product Problem")
    embed = embed.set_author(name=ctx.author.display_name, url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ", icon_url=ctx.author.avatar_url)
    embed = embed.add_field(name="Vector Cross Product", value= "The vector cross product is 〈" + str(ans1) + ", " + str(ans2) + ", " + str(ans3) + "〉", inline=False)
    embed = embed.set_thumbnail(url="https://media.discordapp.net/attachments/899181574535389234/919977550137147472/Screenshot_2021-12-13_7.37.58_AM.png")
    await ctx.send(embed=embed)
  except:
    await ctx.send("Use format !vectorcrossproduct [vector1 1stval] [vector1 2ndval] [vector1 3rdval] [vector2 1stval] [vector2 2ndval] [vector2 3rdval]")

@client.command(name="rooftilefalling",aliases=["rtf",'rooftile','tilefalling'])
async def rooftilefalling(ctx,t,h):
  try:
    t = float(t)
    h = float(h)

    #1/2*g*t^2 + x*t = h
    #x is initial velocity(velocity at when it reaches top of window)
    x = (h-((1/2)*g*(t**2)))/t
    #t2 is time taken before reaching top of window
    t2 = x/g
    #1/2*g*t2^2 + 0*t2 = h2
    #h2 is height between top of window and top of building
    ans=round(t2**2*g/2,2)
    

    embed = discord.Embed(title="Roof Tile Falling Problem")
    embed = embed.set_author(name=ctx.author.display_name, url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ", icon_url=ctx.author.avatar_url)
    embed = embed.add_field(name="Dist b/w Roof and Window", value= "The distance between the roof and the top of the window is " + str(ans) + " .", inline=False)
    embed = embed.set_thumbnail(url="https://media.discordapp.net/attachments/899181574535389234/919977550137147472/Screenshot_2021-12-13_7.37.58_AM.png")
    await ctx.send(embed=embed)
  except:
    await ctx.send("Use format !rooftilefalling [time] [height]") 

@client.command(name="airplanetakeoff",aliases=["planetakeoff",'apto','pt'])
async def airplanetakeoff(ctx,p,nf,pm):
  try:
    p = float(p)
    nf = float(nf)
    pm = float(pm)

    ans = round(pm * nf/p,2)

    embed = discord.Embed(title="Airplane Takeoff Problem")
    embed = embed.set_author(name=ctx.author.display_name, url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ", icon_url=ctx.author.avatar_url)
    embed = embed.add_field(name="Force on Pilot", value= "The force on the pilot is " + str(ans) + " .", inline=False)
    embed = embed.set_thumbnail(url="https://media.discordapp.net/attachments/899181574535389234/919977550137147472/Screenshot_2021-12-13_7.37.58_AM.png")
    await ctx.send(embed=embed)
  except:
    await ctx.send("Use format !airplanetakeoff [airplane mass] [airplane force] [pilot mass]")

@client.command(name="vectordotproduct",aliases=["vectordp",'vdp','vecdotprod'])
async def vectordotproduct(ctx,v1a,v1b,v2a,v2b):
  try:
    v1a = float(v1a)
    v2a = float(v2a)
    v1b = float(v1b)
    v2b = float(v2b)

    ans = round(v1a * v2a + v1b*v2b)

    embed = discord.Embed(title="Vector Dot Product Problem")
    embed = embed.set_author(name=ctx.author.display_name, url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ", icon_url=ctx.author.avatar_url)
    embed = embed.add_field(name="Vector Dot Product", value= "The vector dot product is " + str(ans) + " .", inline=False)
    embed = embed.set_thumbnail(url="https://media.discordapp.net/attachments/899181574535389234/919977550137147472/Screenshot_2021-12-13_7.37.58_AM.png")
    await ctx.send(embed=embed)
  except:
    await ctx.send("Use format !vectordotproduct [vector1 1stval] [vector1 2ndval] [vector1 1stval] [vector1 2ndval]")

@client.command(name="vectormagnitude",aliases=["vectormag",'vm','vecmag'])
async def vectormagnitude(ctx,v1,v2,v3):
  try:
    v1 = float(v1)
    v2 = float(v2)

    v12 = v1**2 + v2**2
    
    if v3 != 0:
      v3 = float(v3)
      ans = round(math.sqrt(v12+v3**2),2)
    else:
      ans = round(math.sqrt(v12),2)

    embed = discord.Embed(title="Vector Magnitude Problem")
    embed = embed.set_author(name=ctx.author.display_name, url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ", icon_url=ctx.author.avatar_url)
    embed = embed.add_field(name="Vector Magnitude", value= "The vector magnitude is " + str(ans) + " .", inline=False)
    embed = embed.set_thumbnail(url="https://media.discordapp.net/attachments/899181574535389234/919977550137147472/Screenshot_2021-12-13_7.37.58_AM.png")
    await ctx.send(embed=embed)
  except:
    await ctx.send("Use format !vectormagnitude [vector1stval] [vector2ndval] [vector3rdval](0 if not used)")

@client.command(name="appliedtrig",aliases=["at",'apptrig','buildingindistance','bid'])
async def appliedtrig(ctx,height,deg):
  try:
    height = float(height)
    deg = float(deg)

    dist = round(height/math.tan(math.radians(deg)),2)


    embed = discord.Embed(title="Applied Trig Problem")
    embed = embed.set_author(name=ctx.author.display_name, url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ", icon_url=ctx.author.avatar_url)
    embed = embed.add_field(name="Dist to tower", value= "You are " + str(dist) + " meters from the base of the building.", inline=False)
    embed = embed.set_thumbnail(url="https://media.discordapp.net/attachments/899181574535389234/919977550137147472/Screenshot_2021-12-13_7.37.58_AM.png")
    await ctx.send(embed=embed)
  except:
    await ctx.send("Use format !appliedtrig [height] [deg]")


@client.command(name="antennaheight",aliases=["ah",'antheight'])
async def antennaheight(ctx,dist,angbase,angtop):
  #try:
    dist = float(dist)
    angbase = float(angbase)
    angtop = float(angtop)

    #tanB*H-tanA*H
    tans = math.tan(math.radians(angtop))-math.tan(math.radians(angbase))
    ans = round(tans*dist,2)

    ans2 = round(csc(math.radians(angtop))*math.tan(math.radians(angtop))*dist,2)

    embed = discord.Embed(title="Antenna Height Problem")
    embed = embed.set_author(name=ctx.author.display_name, url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ", icon_url=ctx.author.avatar_url)
    embed = embed.add_field(name="Tower Length", value= "The height of the antenna is " + str(ans) + " meters.", inline=False)
    embed = embed.add_field(name="Dist to top of tower", value= "The height of the antenna is " + str(ans2) + " meters.", inline=False)
    embed = embed.set_thumbnail(url="https://i.ibb.co/CJ1yCZF/image-2022-03-24-155027.png")
    await ctx.send(embed=embed)
  #except:
   # await ctx.send("Use format !antennaheight [dist] [angbase] [angtop]")



@client.command(name="2Dvectorcombination",aliases=["2vc",'2dvc','twovectorcomb'])
async def twodvectorcomb(ctx,ce1,v1a,v1b,ce2,v2a,v2b):
  try:
    v1a = float(v1a)
    v1b = float(v1b)
    v2a = float(v2a)
    v2b = float(v2b)
    ce1 = float(ce1)
    ce2 = float(ce2)
    
    ans1 = round(ce1*v1a + ce2*v2a,2)
    ans2 = round(ce1*v1b + ce2*v2b,2)


    embed = discord.Embed(title="2D Vector Combination Problem")
    embed = embed.set_author(name=ctx.author.display_name, url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ", icon_url=ctx.author.avatar_url)
    embed = embed.add_field(name="Final vector answer", value= "〈" + str(ans1) + ", " + str(ans2) + "〉", inline=False)
    embed = embed.set_thumbnail(url="https://media.discordapp.net/attachments/899181574535389234/919977550137147472/Screenshot_2021-12-13_7.37.58_AM.png")
    await ctx.send(embed=embed)
  except:
    await ctx.send("use format !2dvectorcombination [coeffecient1] [vector1firstval] [vector1secondval] [leadingsignandcoeffecient2] [vector2firstval] [vector2secondval] with fraction values as decimals")

@client.command(name="righttriangle", aliases=['rt', 'triangle','hypotenuseangle'])
async def righttriangle(ctx, hyp, angle):
  try:
    hyp = float(hyp)
    angA = float(angle)
    
    #law of sines : a=bsinα/sinβ
    a = round(hyp*math.sin(math.radians(angA)),2)

    angB = round(90 - angA,2)

    b = round(hyp*math.sin(math.radians(angB)),2)

    embed = discord.Embed(title="Right Triangle Problem")
    embed = embed.set_author(name=ctx.author.display_name, url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ", icon_url=ctx.author.avatar_url)
    embed = embed.add_field(name="Side A Length", value= "The length of side A " + str(a) + ".", inline=False)
    embed = embed.add_field(name="Side B Length", value= "The length of side A is equal to " + str(b) + ".", inline=False)
    embed = embed.add_field(name="Angle β Measure", value= "The measure of angle β is equal to " + str(angB) + ".", inline=False)
    embed = embed.set_thumbnail(url="https://media.discordapp.net/attachments/899181574535389234/919977550137147472/Screenshot_2021-12-13_7.37.58_AM.png")
    await ctx.send(embed=embed)
  except:
    await ctx.send("use format !righttriangle [hypotenuse] [angleα]")

  

@client.command(name="bearchasestourist", aliases=['moosechasestourists','bct','mct','bearchase','moosechase','touristchase'])
async def bearchasestourist(ctx,touristspeed,distbw,moosespeed):
  try:
    ts = float(touristspeed)
    db = float(distbw)
    ms = float(moosespeed)

    s=ms-ts
    t=db/s
    dist = t*ts

    embed = discord.Embed(title="Bear Chases Tourist Problem")
    embed = embed.set_author(name=ctx.author.display_name, url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ", icon_url=ctx.author.avatar_url)
    embed = embed.add_field(name="Maximum Possible Distance", value=str(dist) + " meters", inline=False)
    embed=embed.set_thumbnail(url="https://media.discordapp.net/attachments/899181574535389234/919977550137147472/Screenshot_2021-12-13_7.37.58_AM.png")
    await ctx.send(embed=embed)
  except:
    await ctx.send("use format !bearchasestourist [touristspeed] [distancebetween] [moosespeed]")

@client.command(name="risingballoondropitem", aliases = ['rbdi','balloon','risingballoon','balloondrop','balloondropitem'])
async def risingballoondropitem(ctx,velocity,distance):
  try: 
    g = 9.8
    gi = g/2
    vel=float(velocity)
    dist=0-float(distance)

    discriminant = vel**2-(4*(gi)*(dist))
    if discriminant < 0:
      await ctx.send("Discriminant is less than 0")
    #0=dist-vel*t+(1/2)gt^2
    else:
      t = (vel+math.sqrt(discriminant))/(2*gi)
      
      embed = discord.Embed(title="Rising Balloon Drop Problem")
      embed = embed.set_author(name=ctx.author.display_name, url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ", icon_url=ctx.author.avatar_url)
      embed = embed.add_field(name="Time to hit ground", value=str(t) + " seconds", inline=False)
      embed=embed.set_thumbnail(url="https://media.discordapp.net/attachments/899181574535389234/919977550137147472/Screenshot_2021-12-13_7.37.58_AM.png")
      await ctx.send(embed=embed)
  except:
    await ctx.send("use format !risingballoondropitem [velocity] [distance]")

  

@client.command(name="acceleratingrunners", aliases=['ar','rugbyplayers','rb'])
async def acceleratingrunners(ctx, dist, acc1, acc2):
  try:
    dist = float(dist)
    acc1 = float(acc1)
    acc2 = float(acc2)

    acc = acc1 + acc2
    t = math.sqrt(2*dist/acc)

    p1 = ((t**2)*acc1)/2
    p2 = ((t**2)*acc2)/2

    embed = discord.Embed(title="Accelerating Runners Problem")
    embed = embed.set_author(name=ctx.author.display_name, url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ", icon_url=ctx.author.avatar_url)
    embed = embed.add_field(name="Part 1(Time to collision)", value=str(t) + " seconds", inline=False)
    embed = embed.add_field(name="Part 2(Player 1 distance)", value=str(p1) + " meters", inline=False)
    embed = embed.add_field(name="Part 3(Player 2 distance)", value=str(p2) + " meters", inline=False)
    embed=embed.set_thumbnail(url="https://media.discordapp.net/attachments/899181574535389234/919977550137147472/Screenshot_2021-12-13_7.37.58_AM.png")
    await ctx.send(embed=embed)
  except:
    await ctx.send("use format !acceleratingrunners [dist] [acc1] [acc2]")

@client.command(name="distancetohorizon",aliases=["dh","dth","disttohorizon","horizon"])
async def distancetohorizon(ctx, height, radius):
  try:
    height = float(height)
    radius = float(radius)

    ansm = math.sqrt((radius+height)**2-(radius)**2)

    embed = discord.Embed(title="Distance to Horizon Problem")
    embed = embed.set_author(name=ctx.author.display_name, url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ", icon_url=ctx.author.avatar_url)
    embed = embed.add_field(name="Part 1(Distance to Horizon in meters)", value=str(ansm) + " meters", inline=False)
    embed = embed.add_field(name="Part 2(Distance to Horizon in miles)", value=str(ansm*0.000621371) + " miles", inline=False)
    embed=embed.set_thumbnail(url="https://media.discordapp.net/attachments/899181574535389234/919977550137147472/Screenshot_2021-12-13_7.37.58_AM.png")
    await ctx.send(embed=embed)
  except:
    await ctx.send("use format !distancetohorizon [height] [radius]")



@client.command(name="bigbirdacceleration",aliases=["bba",'bigbird','ba','birdacceleration'])
async def bigbirdacceleration(ctx,initial,final, t1, t2):
  try:
    initial = float(initial)
    final = float(final)
    t1 = float(t1)
    t2 = float(t2)

    acceleration = (final-initial)/t1

    after = final+t2*acceleration

    embed = discord.Embed(title="Big Bird Acceleration Problem")
    embed = embed.set_author(name=ctx.author.display_name, url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ", icon_url=ctx.author.avatar_url)
    embed = embed.add_field(name="Part 1(Acceleration)", value=str(acceleration) + " m/s^2", inline=False)
    embed = embed.add_field(name="Part 2(Velocity after time)", value=str(after) + " m/s", inline=False)
    embed=embed.set_thumbnail(url="https://media.discordapp.net/attachments/899181574535389234/919977550137147472/Screenshot_2021-12-13_7.37.58_AM.png")
    await ctx.send(embed=embed)
  except:
    await ctx.send("Bad syntax")

@client.command(name="twoarrows", aliases = ["2arrows","arrow","arrows","2a","ta"])
async def twoarrows(ctx,v1,delay):
  # CONSTANTS
  g = -9.80665  # m/s^2

  # INPUT
  try:
      v1 = float(v1)  # speed of arrow 1
      delay = float(delay)  # delay between arrow launches
  except (IndexError, ValueError):
      await ctx.send("use format !twoarrows [v1] [delay]")

  peak_time = -v1/g  # time taken for arrow to reach max height
  v2 = -g*(peak_time-delay)  # speed of arrow 2

  t1 = peak_time  # time from launch to peak for arrow 1
  t2 = (peak_time-delay)  # time from launch to peak for arrow 2
  max_height1 = v1*t1+g/2*t1**2  # max height of arrow 1
  max_height2 = v2*t2+g/2*t2**2  # max height of arrow 2

  # OUTPUT
  embed = discord.Embed(title="Two Arrows Shot Upward Problem")
  embed = embed.set_author(name=ctx.author.display_name, url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ", icon_url=ctx.author.avatar_url)
  embed = embed.add_field(name="Part 1(Speed of Second Arrow)", value=f"Speed of 2nd arrow: {v2:.3f} m/s", inline=False)
  embed = embed.add_field(name="Part 2(Max Height of 1st Arrow)", value=f"Max height of 1st arrow: {max_height1:.3f} m", inline=False)
  embed = embed.add_field(name="Part 3(Max Height of 2nd Arrow)", value=f"Max height of 2nd arrow: {max_height2:.3f} m", inline=False)
  embed=embed.set_thumbnail(url="https://media.discordapp.net/attachments/899181574535389234/919977550137147472/Screenshot_2021-12-13_7.37.58_AM.png")
  await ctx.send(embed=embed)

@client.command(name="cartruck", aliases=["ct", "carandtruck"])
async def cartruck(ctx, truck, theta, dist):
    try:
      truck = float(truck)
      theta = float(theta)
      dist = float(dist)
      print(truck, dist, theta)

      firstTerm = truck / (2 * math.cos(math.degrees(theta)))
      secondTerm = math.pow(truck, 2) * math.pow(math.sin(math.degrees(theta)),
                                                2)

      secondTerm += 9.8 * dist * math.sin(math.degrees(2 * theta))
      secondTerm = math.sqrt(secondTerm)
      secondTerm = secondTerm / math.sin(math.degrees(2 * theta))

      initial_velocity = firstTerm + secondTerm
      second_initial = math.sqrt(9.8 * dist / math.sin(math.degrees(2 * theta)))

      embed = discord.Embed(title="Car and Truck Problem")
      embed = embed.set_author(name=ctx.author.display_name,
                              url="",
                              icon_url=ctx.author.avatar_url)
      embed = embed.add_field(name="Part 1(Moving Trucks)",
                              value="Initial Velocity = " +
                              str(initial_velocity),
                              inline=False)
      embed = embed.add_field(name="Part 2(Still Trucks)",
                              value="Initial Velocity = " + str(second_initial),
                              inline=False)
      embed=embed.set_thumbnail(url="https://media.discordapp.net/attachments/899181574535389234/919977550137147472/Screenshot_2021-12-13_7.37.58_AM.png")
      await ctx.send(embed=embed)
    except:
      await ctx.send("sike that's the wrong numbah(or u just messed up the sin tax)") #nice thx

print(client.guilds)

def fake_socket():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("", PORT))
    s.listen(1)
    while True:
        s.accept()


if __name__ == "__main__":
    fake_socket_process = multiprocessing.Process(target=fake_socket)
    fake_socket_process.start()

    # run bot
    client.run(TOKEN)
