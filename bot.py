import discord
import requests
from random import randint
from discord.ext import commands

intents = discord.Intents.default()


bot = commands.Bot(command_prefix='=', intents=intents)

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

async def check_url_image(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            if response.headers['content-type'].startswith('image'):
                return True
            else:
                return False
        else:
            return False
    except:
        print('Error: failed to validate user avatar_url.')
        return False

@commands.cooldown(1, 30, commands.BucketType.user)
@bot.command()
async def haram(ctx):
    for _ in range(3): 
        await ctx.send('https://tenor.com/view/haram-gif-19585782')

@commands.cooldown(1, 30, commands.BucketType.user)
@bot.command(name='8ball')
async def eight_ball(ctx):
    args = ctx.message.content.split(' ')
    if len(args) == 1:
        await ctx.send('Try asking an actual question, dumbass.')
    responses = [
        'Not today. Well... not ever.', 
        'Obviously, the answer is yes.', 
        'Yes.', 
        'No',
        'Not looking good. But you\'re used to that aren\'t you?', 
        'Most definitely', 
        'You\'re stupid for asking.',
        ' Maybe. Maybe one day you\'ll accomplish something. Who knows?', 
        'I wouldn\'t be so sure.'
    ]
    idx = randint(0, len(responses))
    await ctx.send(responses[idx])

@commands.cooldown(1, 10, commands.BucketType.user)
@bot.command()
async def avatar(ctx):
    args = ctx.message.content.split(' ')
    if len(args) > 1 and await check_url_image(ctx.message.mentions[0].avatar_url):
        await ctx.send(ctx.message.mentions[0].avatar_url)

@commands.cooldown(1, 10, commands.BucketType.user)
@bot.command()
async def jizzon(ctx):
    res = ':ok_hand:         :joy:\n' + \
    ':eggplant: :zzz: :necktie: :eggplant:\n' + \
    '              :oil:     :nose:\n' + \
    '              :zap:  8=:punch:= :smile: :sweat_drops:\n' + \
    '        :trumpet:     :eggplant:                       :sweat_drops:\n' + \
    '          :boot:     :boot:                              :persevere:{}\n'.format(ctx.message.mentions[0].mention)
    await ctx.send(res)

@bot.commands.cooldown(1, 10, commands.BucketType.user)
@bot.command()
async def tc(ctx):
    args = ctx.message.content
    user_data = {
        'leetcoins' : args
    }
    user_leetcoins = int(user_data['leetcoins'])

    try:
        user_tc = (user_leetcoins + 2) * 3.141592
        await ctx.send(f'{ctx.message.author}\'s estimated TC is {round(user_tc):,}k, roughly {round(user_tc/12):,}k after tax.')
    except:
        await ctx.send('Go back to elementary school and learn some algorithms and data structures.')

@commands.cooldown(1, 30, commands.BucketType.user)
@bot.command()
async def bassfx(ctx): 
    await ctx.send('https://cdn.discordapp.com/attachments/832736860886663170/997248777016594462/attachment.gif') 

@commands.cooldown(1, 30, commands.BucketType.user)
@bot.command()
async def dark(ctx): 
    await ctx.send('''https://media.discordapp.net/attachments/966368180723400786/1006982434472067153/IMG_2664.png?width=565&height=524
    **Hey guys, dark here. 8 years ago I said "One Day". Today, I get to say "Day One".
    I'm happy to announce that today I landed my dream job as a junior software engineer at Google where I'll be working with some of the smartest people in the world.
    I would like to thank my mom, my dad, and my discord friends for the support throughout the years.
    I couldn't have done this without you guys**''')

@commands.cooldown(1, 30, commands.BucketType.user)
@bot.command()
async def laz(ctx): 
    await ctx.send('https://media.discordapp.net/attachments/940294974539448360/990038597677744128/attachment.gif')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f'This command is on cooldown, you can use it in {round(error.retry_after, 2)}')

bot.run('') # add key here
