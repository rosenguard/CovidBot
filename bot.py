import discord
from discord.ext import commands
import deutschland_tageszahlen
import get_state
from datetime import datetime

# define all needed variables
token = "YOUR_TOKEN_HERE"

all_states = open("states.txt")
all_states = all_states.read()
all_cities = open("cities.txt", encoding="utf8")
all_cities = all_cities.read()
bot = Bot(
    command_prefix=prefix,
    description="Bot for Corona-Numbers in Germany",
    intents=discord.Intents.all(),
    help_command=None
)

german = deutschland_tageszahlen.Deutschland()
states = deutschland_tageszahlen.Bundeslaender()
cities = deutschland_tageszahlen.Staedte()


# Debug and startmessage in console:
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game("bot.jusen.dev | !help"))

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.channel.send("Du hast ein Argument zu dem Befehl vergessen. \n" +
                               'Wenn du nicht weißt, wie der Befehl aufgebaut ist benutzte "!help" um eine Liste aller Befehle zu bekommen.')


# All commands:
@bot.command()
async def help(ctx):
    embedv = discord.Embed(title="Alle Befehle", color=discord.Colour.dark_blue())
    embedv.add_field(name="!inzidenz [...]", value="Zur Ausgabe der COVID-19-Inzidenzwerte für Deutschland, Bundesländer oder Städte. Der Standort wird nach dem eigentlichen Befehl angegeben.", inline=False)
    embedv.add_field(name="!rwert", value="Zur Ausgabe des COVID-19-Reproduktionsfaktors für ganz Deutschland.", inline=False)
    embedv.add_field(name="!allefälle [...]", value="Zur Ausgabe der Anzahl der an COVID-19 infizierten Personen. Der Standort wird nach dem eigentlichen Befehl angegeben.", inline=False)
    embedv.add_field(name="!alletode [...]", value="Zur Ausgabe der Anzahl der an COVID-19 verstorbenen Personen in Deutschland, Bundesländern oder Städten. Der Standort wird nach dem eigentlichen Befehl angegeben.", inline=False)
    embedv.add_field(name="!impfung [...]", value="Zur Ausgabe von unterschiedlichen Infos zu Impfungen in Deutschland oder Bundesländern. Der Standort wird nach dem eigentlichen Befehl angegeben.", inline=False)
    embedv.add_field(name="!genesen [...]", value="Zur Ausgabe der Anzahl an Genesenen in Deutschland oder Bundesländern. Der Standort wird nach dem eigentlichen Befehl angegeben.", inline=False)
    embedv.add_field(name="!impftermin", value="Um so schnell wie mögluch einen Impftermin in deiner Umgebung zu bekommen.", inline=False)
    embedv.add_field(name="!inzidenzkarte", value="Ausgabe einer Karte mit farblicher Markierung von Inzidenzen für jede Region deutschlands", inline=False)
    await ctx.send(embed=embedv)


@bot.command()
async def inzidenz(ctx, location: None):
    now = datetime.now()

    if location.lower() in all_states.lower():
        new_location = get_state.change_state(location)
        inzidenzwert = float(states.wocheninzidenz(new_location))
        if inzidenzwert == "error".lower():
            await ctx.channel.send("Du hast etwas falsch eingegeben versuche es erneut.")
            return

    if location.lower() in all_cities.lower():
        inzidenzwert = cities.wocheninzidenz(location)
        if inzidenzwert == "error".lower():
            await ctx.channel.send("Du hast etwas falsch eingegeben versuche es erneut.")
            return

    elif location.lower() == "deutschland" or location == "" or None:
        inzidenzwert = german.wocheninzidenz()
        if inzidenzwert == "error".lower():
            await ctx.channel.send("Du hast etwas falsch eingegeben versuche es erneut.")
            return

    else:
        if datetime.time(0, 0) < now < datetime.time(1, 45):
            await ctx.channel.send("Die Werte Aktualisieren sich gerade versuche es in einigen Minuten erneut.")
        else:
            await ctx.channel.send("Du hast etwas falsch eingegeben versuche es erneut.")
        return

    str_loc = location.capitalize()
    str1 = str(inzidenzwert) + " Infizierte pro 100k Einwohner"

    if inzidenzwert <= 50.00:
        msg_color = discord.Color.green()
    elif inzidenzwert <= 100.00:
        msg_color = discord.Color.orange()
    else:
        msg_color = discord.Color.red()

    # Embed Nachricht
    embedmsg = discord.Embed(title=f"Inzidenz in {str_loc}", color=msg_color)
    embedmsg.add_field(name="Inzidenz:", value=str1, inline=False)
    await ctx.channel.send(embed=embedmsg)


@bot.command()
async def rwert(ctx):
    r_wert = german.rwert()

    str2 = "Der Reproduktionsfaktor in Deutschland liegt bei " + str(r_wert) + "."

    if r_wert <= 0.5:
        msg_color = discord.Color.green()
    elif r_wert <= 1.3:
        msg_color = discord.Color.orange()
    else:
        msg_color = discord.Color.red()

    embedmsg = discord.Embed(title='R-Wert:', color=msg_color)
    embedmsg.add_field(name="R-Wert:", value=str2, inline=False)
    await ctx.channel.send(embed=embedmsg)


@bot.command()
async def alle_faelle(ctx, location):
    if location.lower() in all_cities.lower():
        all_cases = cities.allefaelle(location)
    elif location.lower() in all_states.lower():
        new_location = get_state.change_state(location)
        all_cases = states.allefaelle(new_location)
    elif location.lower() == "deutschland":
        all_cases = german.allefaelle()
    else:
        ctx.channel.send("Bitte gebe einen gültigen Standort ein.")
        return

    str3 = f"In {str(location)} gabe es bis jetzt {str(all_cases)} infizierte Personen."

    msg_color = discord.Color.purple()

    embedmsg = discord.Embed(title="Alle Infektionen:", color=msg_color)
    embedmsg.add_field(name="Anzahl an Infektionen:", value=str3, inline=False)
    await ctx.channel.send(embed=embedmsg)


@bot.command()
async def alle_tode(ctx, location):
    if location.lower() in all_cities.lower():
        all_cases = cities.todesfaelle(location)
    elif location.lower() in all_states.lower():
        new_location = get_state.change_state(location)
        all_cases = states.todesfaelle(new_location)
    elif location.lower() == "deutschland":
        all_cases = german.todesfaelle()
    else:
        ctx.channel.send("Bitte gebe einen gültigen Standort ein.")
        return

    str3 = f"In {str(location)} sind bis jetzt {str(all_cases)} Personen an COVID-19 gestorben."


    msg_color = discord.Color.purple()

    embedmsg = discord.Embed(title="Alle Todesfälle:", color=msg_color)
    embedmsg.add_field(name="Anzahl an Todesfällen:", value=str3, inline=False)
    await ctx.channel.send(embed=embedmsg)


@bot.command()
async def impfung(ctx, location):
    if location.lower() in all_states.lower():
        new_location = get_state.change_state(location)
        first_vacc = states.geimpft(new_location)
        sec_vacc = states.vollgeimpft(new_location)
        quote = states.impfquote(new_location)

    elif location.lower() == "deutschland":
        first_vacc = german.geimpft(location)
        sec_vacc = german.vollgeimpft(location)
        quote = german.impfquote(location)

    else:
        ctx.channel.send("Bitte gebe einen gültigen Standort ein.")
        return

    str1 = f"In {location}, wurden bis jetzt {first_vacc} Personen das erste Mal geimpft."
    str2 = f"In {location}, wurden bis jetzt {sec_vacc} Personen das zweite Mal geimpft."
    str3 = f"Die Impfquote in {location}, liegt bei {quote}."

    msg_color = discord.Color.purple()

    embedmsg = discord.Embed(title='Infos über Impfungen', color=msg_color)

    embedmsg.add_field(name="Anzahl an erst Geimpften:", value=str1, inline=False)
    embedmsg.add_field(name="Anzahl an zweit Geimpften:", value=str2, inline=False)
    embedmsg.add_field(name="Impfquote:", value=str3, inline=False)
    await ctx.channel.send(embed=embedmsg)


@bot.command()
async def genesen(ctx, location):
    if location.lower() in all_states.lower():
        new_location = get_state.change_state(location)
        recovered = states.genesen(new_location)

    elif location.lower() == "deutschland":
        recovered = german.genesen(location)

    else:
        await ctx.channel.send("Bitte gebe einen gültigen Standort ein.")
        return

    str1 = f"In {location} sind bis jetzt {recovered} Personen von COVID-19 genesen."

    msg_color = discord.Color.purple()

    embedmsg = discord.Embed(title="Infos über Genesene", color=msg_color)

    embedmsg.add_field(name="Anzahl an Genesenen:", value=str1, inline=False)
    await ctx.channel.send(embed=embedmsg)


@bot.command()
async def impftermin(ctx):
    str1 = "Nach Angabe von PLZ und E-Mail wirst du von sofort-impfen.de benachrichtigt, sobald eine Impfdosis " \
           "übergeblieben ist. "
    str2 = "Auf dieser Seite kannst du einen festen Termin für deine Impfung machen."

    msg_color = discord.Color.magenta()

    embedmsg = discord.Embed(title="Websites um einen Impftermin zu bekommen", color=msg_color)

    embedmsg.add_field(name="sofort-impfen.de", value=str1, inline=False)
    embedmsg.add_field(name="impfterminservice.de", value=str2, inline=False)
    await ctx.channel.send(embed=embedmsg)


@bot.command()
async def inzidenz_karte(ctx):
    await ctx.channel.send("https://api.corona-zahlen.org/map/districts")


bot.run(token)
