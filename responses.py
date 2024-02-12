from random import choice, randint
import praw

reddit = praw.Reddit(
    client_id="RSE6FqhanOIUEyo2ky69Uw",
    client_secret="q6lPCIQ5OfaeDf-1eZI0BKlCz5N0cQ",
    user_agent="scraper by u/ResentedPond",
)


jokes = ["What did the tree tell the annoying tree?\n||Please ***LEAF*** me alone||", 
         "I'm afraid for the calendar.\n||Its days are ***NUMBERED.***||", 
         "Why do fathers take an extra pair of socks when they go golfing?\n||In case they get a ***HOLE IN ONE!***||"]


def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == "":
        return "Someone's silent today..."
    
    elif "hello" in lowered:
        return "Hello there!!"
    
    elif "dice" in lowered:
        return f'Rolling... \n||You got {randint(1, 6)}||'
    
    elif "joke" in lowered:
        return choice(jokes)
    
    elif "reddit" in lowered:
        subreddit = reddit.subreddit(lowered.split(' ')[1])
        top_posts = subreddit.top(limit=1)
        for post in top_posts:
            return f"# *{post.title}*\n[__**>** *LINK* **<**__](<https://reddit.com{post.permalink}>)"

    # elif "" in lowered:
    #     return ""

    elif "help" in lowered:
        return """\
# Raven Bot\n
```ansi
[1;2m[1;32m[1;34m?help[0m[1;32m[0m - [1;31mGet this menu[0m

[1;34m?joke[0m - [1;31mGet a random number[0m

[1;34m?dice[0m - [1;31mDice roll (get a number between 1 and 6)[0m

[1;34m?hello[0m - [1;31mSay hello to Raven Bot![0m[0m

[1;2m[1;31m[0m[0m[1;2m[1;31m[1;34m?reddit[0m[1;31m[0m [1;35m<subreddit name>[0m - [1;31mGet the title and link of the top post on a subreddit of your choosing[0m
    [1;47m[1;47m[1;32m[4;32mEx:[0m[1;32m[1;47m ?reddit amitheasshole[0m[1;47m[0m[1;47m[0m
[0m[0;2m[0m
```
                """

    else:
        return choice(["Huh?", "What are you saying?", "Who let bro cook :skull:", "What??"])
