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


# @bot.event
# async def on_message(message):
#     usr = str(message.author)
#     if message.author == bot.user:
#         return
#
#     if message.content == '$whoami':
#         await message.channel.send(message.author)
#
#     ######################################## database commads  ####################################
#
#     if message.content == '$register':
#         try:
#             bot_database.register(usr)
#         except:
#             print("U have already been registered$")
#         await message.channel.send(usr + " Have been registered!")
#
#     if message.content == '$wallet':
#         primo = str(bot_database.wallet(usr))
#         await message.channel.send("U have " + primo + " primo in your wallet!")
#
#     if message.content.startswith('$checkin'):
#         current_GMT = time.gmtime()
#         time_stamp = calendar.timegm(current_GMT)
#         if bot_database.wish_timestamp_get(usr) <= (time_stamp - 600):
#             x = random.randint(1, 5)
#             primo_final = int(bot_database.wallet(usr)) + x
#             pr = bot_database.update_wallet(usr, str(primo_final))
#             c = str(x) + " Primos have been thrown at you!  " + str(pr) + ' is your new balance'
#             bot_database.wish_timestamp_update(usr, time_stamp)
#             await message.channel.send(c)
#         else:
#             await message.channel.send(" Have Patience!! , checkin every 5 min")
#
#     await bot.process_commands(message)

    #################################################################################################


# @bot.command()
# async def happy(ctx):
#     await ctx.send("Why bro?")


@bot.command(name="gamble")
async def _command(ctx):
    if int(bot_database.wallet(str(ctx.author))) >= 100:
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
    else:
        await ctx.send("U dont have minimum 100 to gamble. BE RESPONSIBLE!!")





@bot.command()
async def starter(ctx):
    user = str(ctx.author)
    b = bot_database.inv_value(user)

    if all([ v == 0 for v in b ]) :
        await ctx.send('Select a character Amber, Kaeya, Lisa')

        def check(msg):
            return msg.author == user and msg.channel == ctx.channel and \
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

    else:
        await  ctx.send('You already have characters , Ehe Te Nandayo!')





@bot.command()
async def wish(ctx):
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


@bot.command()
async def whoami(ctx):
    user = str(ctx.author)
    await ctx.send(user)


@bot.command()
async def register(ctx):
    user = str(ctx.author)
    try:
        bot_database.register(user)
    except:
        print("U have already been registered$")
    await ctx.send(user + " Have been registered!")


@bot.command()
async def wallet(ctx):
    user = str(ctx.author)
    primo = str(bot_database.wallet(user))
    await ctx.send("U have " + primo + " primo in your wallet!")


@bot.command()
async def checkin(ctx):
    user = str(ctx.author)
    current_GMT = time.gmtime()
    time_stamp = calendar.timegm(current_GMT)
    if bot_database.wish_timestamp_get(user) <= (time_stamp - 600):
        x = random.randint(1, 5)
        primo_final = int(bot_database.wallet(user)) + x
        pr = bot_database.update_wallet(user, str(primo_final))
        c = str(x) + " Primos have been thrown at you!  " + str(pr) + ' is your new balance'
        bot_database.wish_timestamp_update(user, time_stamp)
        await ctx.send(c)
    else:
        await ctx.send(" Have Patience!! , checkin every 5 min")




@bot.command()
async def hunt(ctx):
    global user , stats ,char_selected,enemy
    user = str(ctx.author)
    enemy = "n"
    char_selected = "n"
    stats = [0,0,0]

    await ctx.send(f"Select one \n"
                   f"1:Starter Hunt \n"
                   f"2:Pro Hunt \n"
                   f"Once Selected you will have 5 seconds to type your counter character")

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and \
               msg.content #in ["1", "2"]

    try:
        msg = await bot.wait_for("message", check=check, timeout=15.0)
        if msg.content == "1":
            l = ["hilichurl" , "ruin_guard" , "eremite" , "treasure_hoarder"]

            enemy = random.choice(l)

            await ctx.send("A " + enemy + " has appeared")




        elif msg.content == "2":

            l = ["slime", "samachurl"]
            enemy = random.choice(l)

            await ctx.send(enemy)


        else:
            await ctx.send("Stop drinking with Venti")


    except:
        await ctx.send("U are too slow to hunt!")






    if enemy != "n":

        try:
            char_selected = await bot.wait_for("message", check=check, timeout=5.0)


            try:
                stats = bot_database.char_stat(char_selected.content)
                print(stats)
                b = bot_database.check_char(user,char_selected.content)
                print(b)
                if b[0] != 0:
                    await ctx.send("attacking")

    #################################################attacking func##########################################################


                else:
                    await ctx.send("U dont have the char")

            except:
                await ctx.send("Invalid char")









        except:
            await ctx.send("Too Slow! The enemy is attacking you")
            #logic













































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
