# Auto-Split-Editor
Overview

	A Python script for editing Auto-split thresholds by automating the renaming of image files. 
	
	Auto-Split was developed by Toufool (https://github.com/Toufool/Auto-Split) for automatically splitting in 
	livesplit for speedrunning. Unfortunately renaming all my reference images all the time in order to verify runs on SRC became
	annoying, so I wrote this to speed up the process.
	
	I hope this tool will be useful for both moderators and runners. 
	
What are thresholds and why do I need to change them?

	Thresholds are the percentage of similarity Auto-Split needs to see between your capture and the reference image in order to 
	execute the command tied to said reference image. 

	In Auto-Split we can define a custom threshold for each comparison  image to allow for greater accuracy. Custom thresholds require 
	the that the threshold be defined in the filename. You can see this as the number between parentheses. For ex, (0.85) represents
	an 85% threshold. 
	
	If the quality of your capture differs from the reference images you're using, you will likely need to change some of these 
	thresholds for the auto-splitter to work as intended. If Auto-Split gets stuck and doesn't split, lower the threshold. If it splits 
	early, then raise the threshold. If all else fails, you may need to take new screenshots and copy the filenames over. I plan to add 
	that functionality to this scripty eventually. 

Initial Setup

  	1. Download and install Python (https://www.python.org/)

Usage

	1. Run the script. In windows go to the folder with the script, right click in the folder while holding shift then 
	   click "run powershell window here". Then run 'Python Auto-Split-Editor.py' in powershell. 
	3. The first time the script is run, it will create a folder called 'images' if one does not already exist. This is where you put
	   images you want to rename. 
  	2. Select 1 for editing thresholds. 
  	3. Enter threshold values one at a time. S to skip, Q to quit. Enter thresholds as integers between 1 and 99. 

Prerequisites

    [Python] (https://www.python.org/)

Version

	Version 1.0

Authors

	earllgray aka Nick Furlo

License

	The GNU General Public License v3.0
