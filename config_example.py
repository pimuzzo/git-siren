import logging

# Logging level
LEVEL = logging.INFO
# Your github token
GITHUB_TOKEN = 'xxxxxxxxx'
# API rate is 5000 calls per minute, ~70 calls per second
SLEEP_SECONDS = 60
# Light is on for x seconds
LIGHT_SECONDS = 2
# Couples <username, repository>
REPOSITORIES = [
    ('pimuzzo', 'test'),
]
