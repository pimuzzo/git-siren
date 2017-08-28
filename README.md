# Git Siren
The aim of this project is to turn on a REAL beacon light when a new urgent issue is created on github!

## What do you need:
- Raspberry Pi
- Micro USB cable
- Power converter DC 12V to DC 5V (e.g. http://www.dx.com/p/390976) (~ 3.50€)
- Power adapter DC 12V (e.g. http://www.dx.com/p/411920) (~ 3.50€)
- Relay module (e.g. http://www.dx.com/p/121354) (~ 2.00€)
- Emergency siren light 12V (e.g. http://www.ebay.it/itm/161668609157) (~ 10.00€)

## Schema:
![Schema](http://i.imgur.com/riv5JDl.png)

Wiring Raspberry Pi to relay depends by your Raspberry Pi GPIO schema and your relay schema, you can find them online.
You need 3 wires: GND, 5V and signal.
In my script signal is on pin 17.

## Configuration:
You need to take inspiration from `config_example.py` and create your own `config.py` file.

## Usage:
With `python siren.py [port]` you will manage the beacon light (default port is 8080).

With `python github_adapter.py` you will check for new issues and a POST request will be sent when a new issue will be found.

You can also use only `python siren.py [port]` and make a POST:

`http POST http://localhost:8080/light actor=my_test duration=3`

I manage it with [supervisord](http://supervisord.org/) on Raspbian.

## Still to do:
- Ansible script to install and configure supervisor
- recognise urgent from PR rather than from issue
- split the project in 2 parts

Any help (PR) is really appreciated
