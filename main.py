import discord
import random
import asyncio
from discord.ext import commands
import bot_database

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(intents=intents, command_prefix='$')


@bot.event
async def on_ready():
    print("Logged in as {0.user}".format(bot))


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content == '$whoami':
        await message.channel.send(message.author)

    ######################################### database commads  ####################################


    if message.content == '$register':
        usr = str(message.author)
        bot_database.register(usr)
        await message.channel.send(usr+" Have been registered!")



    #################################################################################################
    x = random.randint(1, 5)
    c = str(x) + ' Primos have been thrown at you!'

    if message.content.startswith('wish'):
        await message.channel.send(c)
    await bot.process_commands(message)


@bot.command()
async def happy(ctx):
    await ctx.send("Why bro?")


@bot.command(name="gamble")
async def _command(ctx):
    await ctx.send(f"Are you sure you want to gamble? \n Select either Y or N")

    # This will make sure that the response will only be registered if the following
    # conditions are met:
    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and \
               msg.content.lower() in ["y", "n"]

    try:
        msg = await bot.wait_for("message", check=check, timeout=5.0)
        if msg.content.lower() == "y":
            x = random.randint(-100, 100)
            if (x < 0):
                c = 'Oh no! You lost ' + str(abs(x)) + ' primos!'
                await ctx.send(c)

            elif x >= 0:
                c = 'Congratulations you gained ' + str(x) + ' primos!'
                await ctx.send(c)

        else:
            await ctx.send("Then don't call me dumbo!")
    except:
        await ctx.send("Y u bully me")






bot.run("MTAzMjUzNTkwMDUzMTQ2NjI5MQ.GVvbTp.wo68RLazlH9Pf36p_pZ1fBGiXV9Lb1NgKFZzQo")
