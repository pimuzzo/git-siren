# Git Siren

The aim of this project is to turn on a REAL emergency siren light when a new urgent issue is created!

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

I manage it with supervisord on Raspbian.

## Still to do:
- Ansible script to install and configure supervisor
- recognise urgent from PR rather than from issue
- virtual env / pip freeze

Any help (PR) is really appreciated
