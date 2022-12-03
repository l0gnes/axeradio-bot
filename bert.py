import discord
from discord import app_commands
from discord.ext import commands
from typing import List
from os import environ

class BertBot(commands.Bot):

    debug_servers : List[int]

    def __init__(self, *args, **kwargs) -> None:

        super().__init__(
            intents=discord.Intents.default(),
            command_prefix="." # Does nothing
        )

        self.debug_servers = (
            1020909558933237800,
        )

        self.auto_load_cogs = (
            "cogs.axeradio",
            #"cogs.test",
        )

    async def setup_hook(self) -> None:

        for cog in self.auto_load_cogs:

            try:
                await self.load_extension(cog)

            except Exception as err:
                print(err)


        for guild_id in self.debug_servers:

            gObj = discord.Object(
                    id = guild_id
                )

            self.tree.copy_global_to(
                guild = gObj
            )

            await self.tree.sync(guild=gObj)

        return await super().setup_hook()
    
if __name__ == "__main__":
    bert = BertBot()
    bert.run(
        environ.get("TOKEN")
    )