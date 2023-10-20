# CovidBot

[CovidBot](https://justinr.de/bot.html) is a Discord Bot made in [Python](https://python.org).
The Bots useage is to show information about COVID-19 in Germany on your Discord server.


## All commands

!inzidenz [...]
- To output the COVID-19 incidence values for Germany, federal states or cities. The location is given after the actual command.

!rwert
- To output the COVID-19 reproduction factor for all of Germany.

!allefälle [...]
- To display the number of people infected with COVID-19. The location is given after the actual command.

!alletode [...]
- To output the number of people who died of COVID-19 in Germany, federal states or cities. The location is given after the actual command.

!impfung [...]
- For the output of different information about vaccinations in Germany or federal states. The location is given after the actual command.

!genesen [...]
- To output the number of people who have recovered in Germany or federal states. The location is given after the actual command.

!impftermin
- To get a vaccination appointment in your area as soon as possible.

!inzidenzkarte
- Issue of a map with color coding of incidences for each region of Germany.

## Installation

Clone the GitHub repository:

```bash
  git clone https://github.com/rosenguard/covidBot.git
  cd covidBot
```

Open the bot.py file in the IDE of your choise and add the token of your Discord Bot.
In case you do not have a Token get yours here: [discord.com](https://discord.com/developers)
by creating a new Application. For more information go to the 
[Discord developers documentation](https://discord.com/developers/docs/intro).

After you did this start the Discord bot:
```bash
    python3 bot.py
```

Now the Bot should run without any problems :D 
    
## Authors

- [Justin Rosengart | justinrDEV](https://www.github.com/justinrDEV)
- [Niklas Brockner | NiiklasDEV](https://www.github.com/NiiklasDEV)
