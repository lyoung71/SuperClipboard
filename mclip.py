#! python3
# mclip.py - A multi-clipboard program
import sys, pyperclip


TEXT = {"potential": """Hi ____, it's a pleasure to meet you! I saw that you
        were interested in taking classes with me and I was wondering
        if you had any questions.""",

        "new": """Hi ____, it's a pleasure to meet you!
        I was just wondering if you had any questions for
        me before our class on ____.""",

        'vacation': """Hey, hope you're doing well.
        I just wanted to let you know that I will be
        going on vacation from ____ - ____, so we will
        need to reschedule our classes during that time.
        Take a look at my schedule and see if you can
        find something that works for you.Thanks!"""
        }


keyphrase = input("enter keyphrase: ")

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print(f'Text for {keyphrase} copied to clipboard.')
else:
    print(f'There is no text for {keyphrase}.')
