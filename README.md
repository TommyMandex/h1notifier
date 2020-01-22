						
		██╗  ██╗ ██╗███╗   ██╗ ██████╗ ████████╗██╗███████╗██╗███████╗██████╗ 
		██║  ██║███║████╗  ██║██╔═══██╗╚══██╔══╝██║██╔════╝██║██╔════╝██╔══██╗
		███████║╚██║██╔██╗ ██║██║   ██║   ██║   ██║█████╗  ██║█████╗  ██████╔╝
		██╔══██║ ██║██║╚██╗██║██║   ██║   ██║   ██║██╔══╝  ██║██╔══╝  ██╔══██╗
		██║  ██║ ██║██║ ╚████║╚██████╔╝   ██║   ██║██║     ██║███████╗██║  ██║
		╚═╝  ╚═╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝    ╚═╝   ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝
																			
 

						Author: Bour Mohamed Abdelhadi
							Version:1.0

## Abour h1notifier

h1notifier is a simple tool to fetch disclosed reports from hackerone. h1notifier should run periodically at fixed times. all the new reports will be sent to slack workspace with notification push.


![Screenshot at 2020-01-22 00-01-49](https://user-images.githubusercontent.com/43368124/72847056-726bdd80-3caa-11ea-91bf-f65299e3de0e.png)

## Why ?

Reading reports from other bug bounty hunters may help you to learn different aspects of security.This report https://hackerone.com/reports/745324 encourage me to start building this tool, it's funny to read a report and discover something new 

## Installation and Configuration


`git clone https://github.com/bscript/h1notifier.git`


`cd h1notifier`

`sudo pip3 install -r requirements.txt`

## TODO

- [ ] Post on slack
- [ ] Retreive based on given element - example: ./h1notifier.py -p reporter,title ... ect
- [ ] ...

