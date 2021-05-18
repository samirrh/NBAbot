# NBAbot
![alt text](https://github.com/samirrh/NBAbot/blob/master/example.gif?raw=true)
Anyone that knows me knows I love to play and watch basketball.

I was on a couple basketabll servers on discord and i noticed that there wasn't a player of the week command on any of the bots. <br/>
So I made NBAbot - a discord bot that provides unique player of the week information by scraping and parsing through realgm.com with Beautiful Soup. <br/> 
I noticed a pattern in the urls based on the player names on basketball-reference.com so I restructured scraped data to get corresponding player image
(I may make a player image api since I was not able to find one while making this). <br/>
The bot creates and sends discord embeds to a channel using Discord.py and OOP.


## Commands
<ul>
<li>$NBApow - players of the weeks for both confrences</li> 
<li>$ECpow - player of the week for Eastern Conference</li> 
<li>$WCpow - player of the week for Western Conference</li>  
</ul>

For $ECpow or $WCpow you can specify a number for approximate weeks ago as an argument to get POW from a previous week
<br/>
*This is usually accurate but can be disrupted since the NBA skips a POW sometimes.
<br/>
Includes player image, name, position, and age, and link to full table.
