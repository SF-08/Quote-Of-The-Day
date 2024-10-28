import discord
from discord.ext import commands
import random

TOKEN = 'MTMwMDIyOTI4ODY1Mzc1MDQxNA.Gkf3Vi.TAkB7ltEWTlW47yusffrmxD2LQJ-wfCoSbMlUY'

intents = discord.Intents.default()
intents.message_content = True  

# Initialize the bot
bot = commands.Bot(command_prefix='!', intents=intents)

quotes = {
    "motivational": [
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Success is not how high you have climbed, but how you make a positive difference to the world. - Roy T. Bennett",
        "It always seems impossible until it's done. - Nelson Mandela"
    ],
    "funny": [
        "I am so clever that sometimes I don't understand a single word of what I am saying. - Oscar Wilde",
        "I'm not arguing, I'm just explaining why I'm right.",
        "I finally realized that people are prisoners of their phones... that's why it's called a 'cell' phone."
    ],
    "inspirational": [
        "Believe you can and you're halfway there. - Theodore Roosevelt",
        "Act as if what you do makes a difference. It does. - William James",
        "What lies behind us and what lies before us are tiny matters compared to what lies within us. - Ralph Waldo Emerson"
    ],
    "love": [
        "Love is composed of a single soul inhabiting two bodies. - Aristotle", 
        "Being deeply loved by someone gives you strength, while loving someone deeply gives you courage - Lao Tzu",
        "You can't blame gravity for falling in love. - Albert Einstein",
        "At the touch of love everyone becomes a poet. - Plato",
        "There is more pleasure in loving than in being beloved. - Thomas Fuller",
        "Love is a mutual self-giving which ends in self-recovery. - Fulton J. Sheen",
        "Where there is love there is life. - Mahatma Gandhi",
        "Who so loves believes the impossible. - Elizabeth Barrett Browning",
        "A flower cannot blossom without sunshine, and man cannot live without love. - Max Muller",
        "The best thing to hold onto in life is each other. - Audrey Hepburn",
        "Love is the flower you've got to let grow. - John Lennon",
        "Love is not only something you feel, it is something you do. - David Wilkerson",
        "We loved with a love that was more than love. - Edgar Allan Poe",
        "Love is a friendship set to music. - Joseph Campbell"
    ]
}


@bot.command(name="motivational")
async def motivational_quote(ctx):
    quote = random.choice(quotes["motivational"])
    await ctx.send(quote)


@bot.command(name="funny")
async def funny_quote(ctx):
    quote = random.choice(quotes["funny"])
    await ctx.send(quote)


@bot.command(name="inspirational")
async def inspirational_quote(ctx):
    quote = random.choice(quotes["inspirational"])
    await ctx.send(quote)


@bot.command(name="love")
async def love_quote(ctx):
    quote = random.choice(quotes["love"])
    await ctx.send(quote)


@bot.command(name="categories")
async def list_categories(ctx):
    category_list = ', '.join(quotes.keys())
    await ctx.send(f"Available quote categories: {category_list}")


@bot.command(name="quote")
async def random_quote(ctx, category: str = None):
    if category in quotes:
        quote = random.choice(quotes[category])
        await ctx.send(quote)
    elif category is None:
        all_quotes = sum(quotes.values(), [])  
        quote = random.choice(all_quotes)
        await ctx.send(quote)
    else:
        await ctx.send("Invalid category! Use `!categories` to see available options.")

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


bot.run('MTMwMDIyOTI4ODY1Mzc1MDQxNA.Gkf3Vi.TAkB7ltEWTlW47yusffrmxD2LQJ-wfCoSbMlUY')