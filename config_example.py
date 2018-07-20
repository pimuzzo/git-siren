import logging

# Logging level
LEVEL = logging.INFO
# Your github token
GITHUB_TOKEN = 'xxxxxxxxx'
# API rate is 5000 calls per minute, ~70 calls per second
SLEEP_SECONDS = 60
# Light is on for x seconds
LIGHT_SECONDS = 2
# Base URL
BASE_URL = 'http://localhost:8080'
# Comma-separated list of default label names (AND filter)
DEFAULT_LABELS = 'urgent'
# Object containing informations about repositories
REPOSITORIES = [
    {'username': 'pimuzzo', 'repository': 'git-siren'},
    {'username': 'pimuzzo', 'repository': 'another-repo', 'labels': 'bug'},
]
