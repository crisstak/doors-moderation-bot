import discord
from discord.ext import commands

TOKEN = "MTUzMDY1Mzk2NzM1NTQ3ODA5Nw.GLkK7M.QKj6mqYGO1Z_OgoMd0accsU64GgItsjK4egkEg"

OWNER_ROLE_ID = 1530251904238489741

ROLE_IDS = {
    "owner": 1530251904238489741,
    "member": 1530614638272581724,
    "hide": 1530247025722134548,
    "timothy": 1530247181980668024,
    "screech": 1530247699243466752,
    "rush": 1530248455643988059,
    "ambush": 1530248661492043877,
    "figure": 1530248961959530706,
    "seek": 1530249152133333195,
    "guidinglight": 1530249717445824542,
    "curiouslight": 1530250132413743234,
    "mischievouslight": 1530250442926325842,
    "a60": 1530251209716400188,
    "a90": 1530251401702412549,
    "a120": 1530251568996286564,
}

intents = discord.Intents.all()

bot = commands.Bot(
    command_prefix=";",
    intents=intents,
    help_command=None
)

def owner_only():
    async def predicate(ctx):
        return any(role.id == OWNER_ROLE_ID for role in ctx.author.roles)
    return commands.check(predicate)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")
  # =========================
# ROLE COMMAND
# =========================

@bot.command()
@owner_only()
async def role(ctx, role_name, member: discord.Member):
    role_name = role_name.lower().replace(" ", "")

    if role_name not in ROLE_IDS:
        return await ctx.send("❌ That role doesn't exist.")

    role = ctx.guild.get_role(ROLE_IDS[role_name])

    if role is None:
        return await ctx.send("❌ I couldn't find that role.")

    await member.add_roles(role)

    embed = discord.Embed(
        title="Role Added",
        description=f"✅ {member.mention} has been given the **{role.name}** role.",
        color=0x57F287
    )

    await ctx.send(embed=embed)

# =========================
# ROLE ALIASES
# =========================

@bot.command()
@owner_only()
async def owner(ctx, member: discord.Member):
    await role(ctx, "owner", member)

@bot.command()
@owner_only()
async def member(ctx, member: discord.Member):
    await role(ctx, "member", member)

@bot.command()
@owner_only()
async def hide(ctx, member: discord.Member):
    await role(ctx, "hide", member)

@bot.command()
@owner_only()
async def timothy(ctx, member: discord.Member):
    await role(ctx, "timothy", member)

@bot.command()
@owner_only()
async def screech(ctx, member: discord.Member):
    await role(ctx, "screech", member)

@bot.command()
@owner_only()
async def rush(ctx, member: discord.Member):
    await role(ctx, "rush", member)

@bot.command()
@owner_only()
async def ambush(ctx, member: discord.Member):
    await role(ctx, "ambush", member)

@bot.command()
@owner_only()
async def figure(ctx, member: discord.Member):
    await role(ctx, "figure", member)

@bot.command()
@owner_only()
async def seek(ctx, member: discord.Member):
    await role(ctx, "seek", member)

@bot.command(name="guidinglight")
@owner_only()
async def guidinglight(ctx, member: discord.Member):
    await role(ctx, "guidinglight", member)

@bot.command(name="curiouslight")
@owner_only()
async def curiouslight(ctx, member: discord.Member):
    await role(ctx, "curiouslight", member)

@bot.command(name="mischievouslight")
@owner_only()
async def mischievouslight(ctx, member: discord.Member):
    await role(ctx, "mischievouslight", member)

@bot.command()
@owner_only()
async def a60(ctx, member: discord.Member):
    await role(ctx, "a60", member)

@bot.command()
@owner_only()
async def a90(ctx, member: discord.Member):
    await role(ctx, "a90", member)

@bot.command()
@owner_only()
async def a120(ctx, member: discord.Member):
    await role(ctx, "a120", member)
