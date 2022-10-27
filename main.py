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

_token = bot_database.token()


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
        try:
            bot_database.register(usr)
        except:
            print("U have already been registered$")
        await message.channel.send(usr + " Have been registered!")

    if message.content == '$wallet':
        primo = str(bot_database.wallet(usr))
        await message.channel.send("U have " + primo + " primo in your wallet!")

    if message.content.startswith('$checkin'):
        current_GMT = time.gmtime()
        time_stamp = calendar.timegm(current_GMT)
        if bot_database.wish_timestamp_get(usr) <= (time_stamp - 600):
            x = random.randint(1, 5)
            primo_final = int(bot_database.wallet(usr)) + x
            pr = bot_database.update_wallet(usr, str(primo_final))
            c = str(x) + " Primos have been thrown at you!  " + str(pr) + ' is your new balance'
            bot_database.wish_timestamp_update(usr, time_stamp)
            await message.channel.send(c)
        else:
            await message.channel.send(" Have Patience!! , checkin every 5 min")

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


@bot.command(name="starter")
async def _command(ctx):
    await ctx.send('Select a character Amber, Kaeya, Lisa')

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and \
               msg.content.lower() in ["amber", "kaeya", "lisa"]

    try:
        msg = await bot.wait_for("message")
        if msg.content.lower() == "amber":
            character = 'amber'
        elif msg.content.lower() == "kaeya":
            character = 'kaeya'
        elif msg.content.lower() == "lisa":
            character = 'lisa'

        user = str(msg.author)
        bot_database.starter(user, character)

        await ctx.send('Congratulation you have selected ' + character + ' as your starter character! Good Luck on '
                                                                         'your adventures!')
    except:
        await  ctx.send('You spelled it wrong!')


@bot.command(name="wish")
async def _command(ctx):
    user = str(ctx.author)
    if (int(bot_database.wallet(user)) >= 160):
        character_list = 'amber', 'kaeya', 'lisa', 'barbara', 'diluc', 'jean', 'razor', 'klee', 'bennett', 'noelle', 'fischl', 'sucrose', 'mona', 'diona', 'albedo', 'rosaria', 'eula', 'venti'
        x = random.choice(character_list)
        primo_final = int(bot_database.wallet(user)) - 160
        pr = bot_database.update_wallet(user, str(primo_final))
        bot_database.wish_character(user, x)
        await ctx.send("Congratulations! You have received " + x + "!\n")
        await ctx.send("You now have " + str(pr) + " primos left.")

    else:
        await ctx.send("It looks like you do not have enough primos. Please earn at least 160 before you can wish!")


@bot.command()
async def inventory(ctx):
    user = str(ctx.author)
    a = bot_database.inv_name(user)
    b = bot_database.inv_value(user)
    x = 0
    c =[]

    while x < len(b):
        if b[x] != 0:
             v = str(a[x][0]) +" Level " + str(b[x])
             c.append(v)


        x = x + 1
    await ctx.send(" , ".join(c))


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


bot.run(_token)
