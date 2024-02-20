import discord
from discord.ext import commands

# Initialize & Command Prefix
bot = commands.Bot(command_prefix='!')

tasks = []

# Command: Add Task
@bot.command(name='addtask', help='Adds a new task to your to do list.')
async def add_task(ctx, *, task):
    tasks.append(task)
    await ctx.send(f"Added task: {task}")

# Token
bot.run('MTIwOTMwOTI2MzQ3OTA1MDI4Mw.GkdSo4.-a0kqCCzBhOWZ0Y4A4l6xxf43yVK05lG0EoeaQ')