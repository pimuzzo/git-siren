# -*- coding: utf-8 -*-

import logging
import sys
import time

import web
from gpiozero import DigitalOutputDevice

from config import LEVEL

web.config.debug = False
urls = (
    '/light', 'light'
)


# supervisord -c /etc/supervisord.conf
# sudo supervisorctl -c /etc/supervisord.conf reload


class light:
    def POST(self):
        i = web.input()
        return turn_on_the_light(i.duration, i.actor)


def turn_on_the_light(duration, actor):
    logging.info('New light request by {} for {} seconds'.format(actor, duration))
    relay = DigitalOutputDevice(17)
    relay.on()
    time.sleep(float(duration))
    relay.off()
    relay.close()


if __name__ == "__main__":
    log_format = '%(asctime)s - %(levelname)s - %(message)s'
    logging.basicConfig(stream=sys.stdout, level=LEVEL, format=log_format)

    app = web.application(urls, globals())
    app.run()
