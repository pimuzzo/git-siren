# -*- coding: utf-8 -*-

import logging
import sys
import time

import github3
from gpiozero import DigitalOutputDevice

from config import LEVEL, GITHUB_TOKEN, SLEEP_SECONDS, LIGHT_SECONDS, REPOSITORIES

gh = github3.login(token=GITHUB_TOKEN)
urgent_tickets = set()
tmp_urgent_tickets = set()


# supervisord -c /etc/supervisord.conf
# sudo supervisorctl -c /etc/supervisord.conf reload


def check_and_hit_syren(urgent_ticket):
    tmp_urgent_tickets.add(urgent_ticket)
    if urgent_ticket not in urgent_tickets:
        # hit the syren
        logging.info('New urgent ticket found: ' + urgent_ticket)
        relay = DigitalOutputDevice(17)
        relay.on()
        time.sleep(LIGHT_SECONDS)
        relay.off()
        relay.close()


if __name__ == '__main__':
    log_format = '%(asctime)s - %(levelname)s - %(message)s'
    logging.basicConfig(stream=sys.stdout, level=LEVEL, format=log_format)

    while True:
        for username, repository in REPOSITORIES:
            issues = gh.issues_on(username, repository, state='open', labels='urgent')
            for issue in issues:
                # if the ticket wasn't in `urgent_tickets` hit the syren
                urgent_ticket = username + '/' + repository + '#' + str(issue.number)
                check_and_hit_syren(urgent_ticket)
        urgent_tickets = tmp_urgent_tickets.copy()
        tmp_urgent_tickets.clear()
        logging.info(urgent_tickets)
        time.sleep(SLEEP_SECONDS)
