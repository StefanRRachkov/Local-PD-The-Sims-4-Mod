# Local PD The Sims 4 Mod
 Create a Police Station venue in your world and your detective sim will go there instead of the default one
 <p align="center"><img src="https://github.com/StefanRRachkov/Local-PD-The-Sims-4-Mod/assets/25185815/a99d7616-978c-43bc-92e1-39d8c5d554d1" /></p>
 
# Quick Notes
 There are some things that should be clarified.
 1. Zone is the lot in the world (Buildible zone)
 2. World is actually a collection of a few Zones
 3. Region is the city, or collection of a few Worlds
 4. Venue is the type of the Zone (Park, Residential, Police Station etc.)

# Code
Firstly we have the utility injector.py which is holding some basic helper functions that are making possible to alter the code of the existing classes in that case the class CareerEvent and the method on_career_event_requested.
The main functionality is in main.py and it is taking the player's home zone via the household class, from the zone we can check which region is the home one and from region we can cycle all the available zones from all the available worlds.
If there is Police Station among them we are replacing the required_zone from the CareerEvent class with the one from the home region. If there isn't one, we are using the default one from the game itself.

# How to use
 1. Compile the python scripts with python 3.7 (The version is important)
 2. Zip the newly created .pyc files
 3. Rename the archive from .zip to .ts4script
 4. Place the script into the Mods folder of your game

# Additional Requirements
 1. You should have The Sims 4: Get to Work EP in order to have Police Venues and Detective career
 2. You should have the Police Station venue option in your venue list, which can be opted with Venue List mod or by editing the Region Tuning and Venue Tuning files from Sims 4 Studio

# Easy Use
Just download the mod from here:
https://www.curseforge.com/sims4/mods/local-police-departments
