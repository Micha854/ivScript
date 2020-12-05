# ivScript

#### HELP ON DISCORD: https://discord.gg/QYcR4cu

### this is the multi branch. you can configure several channels. the script automatically distributes the messages in the correct channels

## Install requirements

`pip3 -r install requirements.txt`

## Config
`cp config_example.json config.json`

put in here your channels. for the geofence for your channels, you can use `http://geo.jasparke.net/` and save the json file. than you can copy/paste the coordinates part into your config.json file

## Start
`python3 iv-main.py`

optional, you can put the config parameter

`python3 iv-main.py myconfig.json`

## Notes

Limits on Telegram Channels are 30 Messages per second and for Groups 20 messages per minute

![example](https://raw.githubusercontent.com/Micha854/ivScript/master/example.png)
