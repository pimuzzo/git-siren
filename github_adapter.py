# -*- coding: utf-8 -*-

import logging
import sys
import time

import github3
import requests

from config import LEVEL, GITHUB_TOKEN, SLEEP_SECONDS, LIGHT_SECONDS, BASE_URL, DEFAULT_LABELS, REPOSITORIES

gh = github3.login(token=GITHUB_TOKEN)


def check_and_send_light_request(new_tickets, old_tickets):
    for ticket in new_tickets - old_tickets:
        # request to beacon light
        logging.info('New ticket found: {}'.format(ticket))
        payload = {'actor': 'github_adapter', 'duration': LIGHT_SECONDS}
        requests.post(BASE_URL + '/light', json=payload)


def main():
    old_tickets = set()
    new_tickets = set()
    while True:
        try:
            for repository_data in REPOSITORIES:
                username = repository_data.get('username')
                repository = repository_data.get('repository')
                labels = repository_data.get('labels') or DEFAULT_LABELS
                issues = gh.issues_on(username, repository, state='open', labels=labels)
                for issue in issues:
                    ticket = username + '/' + repository + '#' + str(issue.number)
                    new_tickets.add(ticket)
            check_and_send_light_request(new_tickets, old_tickets)
            old_tickets = new_tickets.copy()
            logging.info(old_tickets)
            new_tickets.clear()
        except (requests.exceptions.RequestException, github3.exceptions.ServerError) as e:
            logging.error(e)
        time.sleep(SLEEP_SECONDS)


if __name__ == '__main__':
    log_format = '%(asctime)s - %(levelname)s - %(message)s'
    logging.basicConfig(stream=sys.stdout, level=LEVEL, format=log_format)
    main()
