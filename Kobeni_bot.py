import discord
from discord.ext import commands
import re
Kobeni = commands.Bot(command_prefix="^", intents=discord.Intents.all())

yo = re.compile(r'\byo\b', re.IGNORECASE)

@Kobeni.event
async def on_ready():
    print("Armada y preparada")
    
@Kobeni.command()
async def gap(ctx):
    await ctx.send("Jg gap")

@Kobeni.tree.command(name="ping", description="Primer comando solo de prueba")
async def ping(interaction: discord.Interaction):
   await interaction.response.send_message('pong')

@Kobeni.command()
async def sincronizar(ctx):
    await Kobeni.tree.sync()
    await ctx.send('Lista!')    
    
    
@Kobeni.event
async def on_message(message):
    # Asegurémonos de que el autor no sea Kobeni para evitar un bucle de saludos
    if message.author == Kobeni.user:
        return
   
    # Si la palabra "Hola" está en el mensaje, saludar al autor del mensaje
    if "hola" in message.content.lower():
        await message.channel.send(f"Hola {message.author.name}!")
        await message.channel.send("https://media1.giphy.com/media/h3GQNJfBgmqIsEYw94/giphy.gif")
    
    # Verifica si la mención está presente en el mensaje
    if Kobeni.user.mention in message.content:
        await message.channel.send(f"¡Hola! Me mencionaste? {message.author.mention}.")

    if "negro" in message.content.lower():
        await message.channel.send(f"Tu eres el Negro {message.author.name}!")

    if "negra" in message.content.lower():
        await message.channel.send(f"Tu eres la Negra {message.author.name}!")

    # Verificar si "yo" está presente y no está rodeado por otras letras
    if re.search(r'\b(?:yo)\b', message.content.lower()) and not re.search(r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/', message.content):
        await message.channel.send("¡Sí, eres amigui >.<!")

    if "matalo" in message.content.lower():
        await message.channel.send("https://tenor.com/view/ahmet-sonmez-ahmet-s%c3%b6nmez-kledistan-malphite-durdurulamaz-gif-25384645")

    if "jg gap" in message.content.lower():
        await message.channel.send("https://www.youtube.com/watch?v=onY9eHi_eco")
        
        
    # Este comando se encarga de asegurarse de cerrar este bloque de función y que todo funcione como debería
    await Kobeni.process_commands(message)

Kobeni.run("MTE1NDgyMDM1MTYzMzY2NjExOQ.GYVVbx.lV6T-BpL8EaLf59pDGsGk34gCQNoZ66l8Wdb-8")
