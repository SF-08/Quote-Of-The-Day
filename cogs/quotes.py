import discord
import random
from discord.ext import commands

#QUOTES

class quotes(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def love(self, ctx):
        love_quotes = [
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
            "Love is a friendship set to music. - Joseph Campbell",
            
        ]

        await ctx.send(random.choice(love_quotes))





# Cog Setup


def setup(client):
    client.add_cog(quotes(client))