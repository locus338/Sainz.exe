import os
import discord
import typing
import googletrans
from discord.ext import commands
from threading import Thread
from flask import Flask, render_template
intent = discord.Intents.all()
intent.message_content = True
app = Flask(__name__,template_folder="Templates")
bot = commands.Bot(command_prefix="~", intents=intent , help_command=None)

def run():
    app.run(host='0.0.0.0', port=10000, use_reloader=False, debug=True)
def stay():
    thread = Thread(target=run)
    thread.start()

@app.route('/')
def index():
    return 'Index Page'
SRCLanguage = "zh-TW"

@bot.event
async def on_ready():
   print('成功登入')
   guild = bot.get_guild(979253935816704030)
   await guild.leave()

@bot.command(aliases=['t','T','trans','Trans','TRANS','tran','Tran','TRAN'])
async def translate(ctx, *, message: typing.Optional[str] = None):
   if message is None:
       await ctx.reply("請輸入要翻譯的內容")
       return

   if ctx.message.author == bot.user:
       print("逼逼逼")
       return
   else:
       print("執行成功!")
       translator = googletrans.Translator()
       if translator.detect(message).lang == 'zh-CN':
           pass
       print(translator.detect(message).lang)
       if translator.detect(message).lang != "zh-TW":
           remessage = translator.translate(
               message, dest='zh-TW').text
           await ctx.reply(remessage)
       if translator.detect(message).lang != "en":
           remessageen = translator.translate(message, dest='en').text
           await ctx.reply(remessageen)
@bot.event
async def on_ready():
    print('目前登入身份：',bot.user)
    game = discord.Game('EK的電腦')
    #discord.Status.<狀態>，可以是online,offline,idle,dnd,invisible
    await bot.change_presence(status=discord.Status.online, activity=game)

@bot.command(aliases=['PING', 'PINGS', 'pings', 'Ping', 'Pings'])
async def ping(ctx):
   await ctx.send(F'Render：{round(bot.latency*1000)}ms')  

@bot.command(help_command=None)
async def help(ctx):
    await ctx.reply("`~translate`開始翻譯\n\n**別名**：`t`、`tran`、`trans`")

if __name__ == "__main__":
    token = os.getenv("TOKEN")    
    stay()
    bot.run(token)
