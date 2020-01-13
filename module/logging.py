#!/usr/bin/env python3

import datetime


def logging_main(message):
    now = datetime.datetime.now()
    with open ("log/discord/%s.log" % now.strftime('%Y-%m-%d'), 'a') as logfile:
        data = "[%s, %s, %s] %s, %s\n" % (now.strftime('%Y-%m-%d %H:%M:%S'), message.guild, message.channel, message.author, message.author.display_name)
        data += "%s\n\n" % message.content
        logfile.write(data)