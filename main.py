import discord
import random
import asyncio
from discord.ext import commands
import bot_database
import calendar
import time

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(intents=intents, command_prefix='$')


@bot.event
async def on_ready():
    print("Logged in as {0.user}".format(bot))


@bot.event
async def on_message(message):
    usr = str(message.author)
    if message.author == bot.user:
        return

    if message.content == '$whoami':
        await message.channel.send(message.author)

    ######################################### database commads  ####################################

    if message.content == '$register':
        bot_database.register(usr)
        await message.channel.send(usr + " Have been registered!")

    if message.content == '$wallet':
        primo = str(bot_database.wallet(usr))
        await message.channel.send("U have " + primo + " primo in your wallet!")

    if message.content.startswith('$wish'):
        current_GMT = time.gmtime()
        time_stamp = calendar.timegm(current_GMT)
        if bot_database.wish_timestamp_get(usr) <= (time_stamp - 300):
            x = random.randint(1, 5)
            primo_final = int(bot_database.wallet(usr)) + x
            pr = bot_database.update_wallet(usr, str(primo_final))
            c = str(x) + " Primos have been thrown at you!  " + str(pr) + ' is your new balance'
            bot_database.wish_timestamp_update(usr, time_stamp)
            await message.channel.send(c)
        else:
            await message.channel.send(" Have Patience!! , wish every 5 min")

    await bot.process_commands(message)

    #################################################################################################


# @bot.command()
# async def happy(ctx):
#     await ctx.send("Why bro?")


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
            user = str(msg.author)

            primo_final = x + int(bot_database.wallet(user))
            pr = bot_database.update_wallet(user, str(primo_final))
            if x < 0:
                c = 'Oh no! You lost ' + str(abs(x)) + ' primos!' + " Your new balance is now " + str(pr)
                await ctx.send(c)

            elif x >= 0:
                c = 'Congratulations you gained ' + str(x) + ' primos!' + " Your new balance is now " + str(pr)
                await ctx.send(c)

        else:
            await ctx.send("Then don't call me dumbo!")
    except:
        await ctx.send("Y u bully me")


# @bot.command(name="tf1")
# async def _command(ctx):
#     await ctx.send(f"yo")
#
#     # This will make sure that the response will only be registered if the following
#     # conditions are met:
#     def check(msg):
#         return msg.author == ctx.author and msg.channel == ctx.channel and \
#                msg.content.lower() in ["y", "n"]
#
#     msg = await bot.wait_for("message", check=check, timeout=10.0)
#     await ctx.send(msg.author)


bot.run(".")
