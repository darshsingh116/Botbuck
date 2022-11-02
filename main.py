import discord
import random
import asyncio
from discord.ext import commands
import bot_database
import calendar
import time
import math





intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(intents=intents, command_prefix='$')

_token = bot_database.token()


@bot.event
async def on_ready():
    print("Logged in as {0.user}".format(bot))
    await bot.change_presence(activity=discord.Game(name="$howtoplay for help"))


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

    if all([v == 0 for v in b]):
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
    c = []

    while x < len(b):
        if b[x] != 0:
            v = str(a[x][0]) + " Level " + str(math.ceil(b[x]))
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
    global user, stats, char_selected, enemy,element
    user = str(ctx.author)
    enemy = "n"
    char_selected = "n"
    stats = [0, 0, 0]
    print(user)

    await ctx.send(f"Select one \n"
                   f"1:Starter Hunt \n"
                   f"2:Pro Hunt \n"
                   f"Once Selected you will have 5 seconds to type your counter character")

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and \
               msg.content  # in ["1", "2"]

    try:
        msg = await bot.wait_for("message", check=check, timeout=15.0)
        if msg.content == "1":
            l = ["hilichurl", "ruin_guard", "eremite", "treasure_hoarder"]

            enemy = random.choice(l)

            await ctx.send(f"A {enemy} has appeared")




        elif msg.content == "2":

            l = ["slime", "samachurl"]
            elements= ["pyro","cryo","ameno","electro","dendro","hydro","geo"]
            #elements = ["electro"]
            enemy = random.choice(l)
            element = random.choice(elements)

            await ctx.send(f"A {element} {enemy} has appeared")


        else:
            await ctx.send("Stop drinking with Venti")


    except:
        await ctx.send("U are too slow to hunt!")

    if enemy != "n" and msg.content == "1":

        try:
            char_selected = await bot.wait_for("message", check=check, timeout=5.0)

            try:
                stats = bot_database.char_stat(char_selected.content)
                print(stats)
                lvl = bot_database.check_char(user, char_selected.content)[0]
                print(lvl)
                if lvl != 0:
                    await ctx.send("attacking")

                    await attacking(ctx, user, stats, char_selected.content, enemy, lvl,4)

                #################################################attacking func##########################################################

                else:
                    await ctx.send("U dont have the char")

            except:
                await ctx.send("Invalid char")

        except:
            await ctx.send("You are Too Slow to be a hunter!")
            # if lvl > 0.33:
            #     bot_database.update_char_starter(str(user), str(char_selected.content))
            #     await ctx.send("Hp decreased by 33%.. CHECK $inventory TO SEE IF LEVEL DECREASED OR NOT")
            # else:
            #     bot_database.kill_char(str(user), str(char_selected.content))
            #     await ctx.send("Not enough HP, character died")



    if enemy != "n" and msg.content == "2":

        try:
            char_selected = await bot.wait_for("message", check=check, timeout=5.0)

            try:
                stats = bot_database.char_stat(char_selected.content)
                print(stats)
                lvl = bot_database.check_char(user, char_selected.content)[0]
                print(lvl)
                if element != stats[0]:
                    if lvl != 0:
                        await ctx.send("attacking")

                        await attacking(ctx, user, stats, char_selected.content, enemy, lvl, 5)

                    #################################################attacking func##########################################################

                    else:
                        await ctx.send("U dont have the char")
                else:
                    if lvl > 1:
                        bot_database.update_char_immune(str(user), str(char_selected.content))
                        await ctx.send("ENEMY IS IMMUNE! Hp decreased by 100%.. CHECK $inventory TO SEE IF LEVEL DECREASED OR NOT")
                    else:
                        bot_database.kill_char(str(user), str(char_selected.content))
                        await ctx.send("ENEMY IS IMMUNE! Not enough HP, character died")

            except:
                await ctx.send("Invalid char")

        except:
            await ctx.send("You are Too Slow to be a hunter!")
            # if lvl > 0.33:
            #     bot_database.update_char_starter(str(user), str(char_selected.content))
            #     await ctx.send("Hp decreased by 33%.. CHECK $inventory TO SEE IF LEVEL DECREASED OR NOT")
            # else:
            #     bot_database.kill_char(str(user), str(char_selected.content))
            #     await ctx.send("Not enough HP, character died")


# @bot.command()
# async def test(ctx):
#     await ctx.send("yes")
#
#     def check(msg):
#         return msg.author == ctx.author and msg.channel == ctx.channel and \
#                msg.content
#
#     msg = await bot.wait_for("message", check=check, timeout=15.0)
#     # if msg.content == "no":


# @bot.command()
# async def lol(ctx):
#     message = await ctx.send('test')
#     emoji = '\N{THUMBS UP SIGN}'
#     print(emoji)
#     await message.add_reaction("\U0001F1E6")


# @bot.event
# async def on_reaction_add(reaction, user):
#     global rex
#     rex = reaction.emoji
#     print(rex)
#     print(reaction.message)
#     print(reaction.message.id)
#     print(reaction.message.author.id)

async def attacking(ctx, usr, stats, char_selected, enemy, lvl,base):
    global user_input
    global emojis
    global loose
    global time_stamp1



    user_input = []
    emoji_list = ["\U0001F1E6", "\U0001F1E7", "\U0001F1E8", "\U0001F1E9", "\U0001F1EA", "\U0001F1EB", "\U0001F1EC",
                  "\U0001F1ED", "\U0001F1EE", "\U0001F1EF", "\U0001F1F0", "\U0001F1F1", "\U0001F1F2", "\U0001F1F3",
                  "\U0001F1F4", "\U0001F1F5", "\U0001F1F6", "\U0001F1F7", "\U0001F1F8", "\U0001F1F9", "\U0001F1FA",
                  "\U0001F1FB", "\U0001F1FC", "\U0001F1FD", "\U0001F1FE", "\U0001F1FF"]

    emojis = random.sample(emoji_list, 5)

    message = await ctx.send('game')
    botmsgid = message.id

    for x in range(5):
        await message.add_reaction(emojis[x])

    current_GMT1 = time.gmtime()
    time_stamp1 = calendar.timegm(current_GMT1)





    @bot.event
    async def on_reaction_add(reaction, user):
        rex = reaction.emoji
        if botmsgid == reaction.message.id:
            user_input.append(rex)


        current_GMT2 = time.gmtime()
        time_stamp2 = calendar.timegm(current_GMT2)
        if len(user_input) == 5:
            if user_input[0] < user_input[1] < user_input[2] < user_input[3] < user_input[4] and (time_stamp2 - time_stamp1 ) <= 10:
                print(user_input)
                reward = lvl * int(base)
                await ctx.send(f"Enemies Defeated! Rewarded {math.ceil(reward)} primos!")
                primo_final = int(bot_database.wallet(str(user))) + math.ceil(reward)
                bot_database.update_wallet(str(user),str(primo_final))
            else:
                print(user_input)
                if lvl > 0.33:
                    bot_database.update_char_starter(str(user),str(char_selected))
                    await ctx.send("You Suck, Hp decreased by 33%.. CHECK $inventory TO SEE IF LEVEL DECREASED OR NOT")
                else:
                    bot_database.kill_char(str(user),str(char_selected))
                    await ctx.send("Not enough HP, character died")




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

@bot.command()
async def howtoplay(ctx):
    await ctx.send(file=discord.File("Instruction.txt"))

bot.run(_token)
