					 _     __              _   _  __ _           
					| |   /  |            | | (_)/ _(_)          
					| |__ `| | _ __   ___ | |_ _| |_ _  ___ _ __ 
					| '_ \ | || '_ \ / _ \| __| |  _| |/ _ \ '__|
					| | | || || | | | (_) | |_| | | | |  __/ |   
					|_| |_\___/_| |_|\___/ \__|_|_| |_|\___|_|   

						Author: Bour Mohamed Abdelhadi
							Version:1.0

## Abour h1notifier

h1notifier is a simple tool to fetch disclosed reports from hackerone. h1notifier should run periodically at fixed times. all the new reports will be sent to slack workspace with notification push.

## Installation and Configuration

```
git clone https://github.com/bscript/h1notifier.git
```

```
cd h1notifier

```

```
sudo pip3 install -r requirements.txt
``

## TODO

- [ ] Post on slack
- [ ] Retreive based on given element - example: ./h1notifier.py -p reporter,title ... ect
- [ ] ...

