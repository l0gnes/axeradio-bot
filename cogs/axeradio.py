from discord.ext import commands
import discord
from discord import app_commands

class AxeRadioModule(commands.Cog):

    def __init__(self, client : commands.Bot):
        self.client = client

    @app_commands.command(
        name = "axeradio",
        description = "Attempt to tune into AxeRadio"
    )
    async def axeradio_cmd(self, interaction : discord.Interaction):

        # This whole chunk just checks to see if there is a voice client
        # associated with the user
        author_voice = interaction.user.voice
        if author_voice is None:

            return await interaction.response.send_message(
                "You aren't in a voice channel!",
                ephemeral=True
            )

        # Grabs the user's channel
        chan = interaction.user.voice.channel

        # Connects the voice client to the channel the user is in
        voice_client = await chan.connect()

        # Super secret AxeRadio livestream link
        source = discord.FFmpegPCMAudio(
            "http://n03.radiojar.com/433gq6uurhruv.m4a?rj-ttl=4&1670081639=&rj-tok=AAABhNiqVj0AaXNwHDssHfUUKg",
            before_options = "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5",
            options= "-vn"
        )

        # Plays that audio stream
        voice_client.play(source)

async def setup(client : commands.Bot):
    await client.add_cog(
        AxeRadioModule(client)
    )