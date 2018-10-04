# text-input-game
### A Finite state Machine based Game of Thrones game on the console using Python.

The project consists of the following components

1. Game
2. Statistics
3. Evidences and Testing
4. Folder Structure


## 1. Game :

The game has been coded as a .py file and can be run from an IDE like PyCharm or the command line
FileName : GameOfThrones.py
Instructions to run the game :
1. Download the Zip file and Unzip it
2. Open the command prompt and go to the TextChoiceGame
3. Run the following command

python GameOfThrones.py

P.S.: The game has a background score which I believe you will like. So if you are in a Silent Zone, then play the game with your headphone connected


#### Game Rules and Mission :

Welcome to the Game of Thrones!!!
This is a fun game where the aim is to Win the Iron Throne!
Winter has come and its waiting for you to jump into the Royal and fierce Battle
Are you excited to play?

A bit background of the tasks you need to perform in order to Win this game.
There are 5 enemies in the game
1. Cersei Lannister
2. Ramsay Bolton
3. Petyr Baelish
4. Jon Snow
5. Night King

The following is a list of places which you will visit. few of the places hav a specilaity weapon and a eneny present. Make a note of this.
1. Winterfell
2. Casterly Rock
3. King's Landing
4. Iron Islands
5. Dragon Stone
6. River run
7. North of the Wall

The following weapons will be available to fight your enemies
1. Sword
2. Arya's Needle
3.Dragons
4.Wildfire
5. Dragon glass
6. Cross Bow
7. Knife


Each enemy can be killed with a specific weapon and at a specific place. Below are the details:
1. Jon Snow > Sword > Winterfell
2. Cersei Lannister > Cross Bow > King’s Landing
3. Ramsay Bolton > Wildfire > Riverrun
4. Petyr Baelish > Dragons > The Iron Islands
5. Night King > Dragon glass > North of the Wall

In order to Win and cherish the Iron Throne, you need to achieve the following tasks as optimally (minimum number of moves) as possible
1. Collect only the required weapons and go to places strategically
2. You need to kill Cersei Lannister and 2 other enemies with the weapons which are their weaknesses
3. You need to complete the task in minimum number of moves
4. There are many distractions in the game which may lead to dead-ends. So BEWARE!!!

## 2. Statistics:

Stats have been plotted and shown as a Jupyter Notebook

The game writes Statistics to a file : stats.txt which is present in the Statistics folder
The game writes the States of the User to a file : states_passed.txt which is present in the Statistics folder


Instructions to access the Stats: 
1. Open a command prompt and go to the Statistics folder
2. Run Jupyter Notebook (COMMAND : jupyter notebook)
3. Open the Stats_TextChoiceGame_GOT.ipynb or you can directly have a look at the previous stats by opening the HTML page : Stats_TextChoiceGame_GOT.slides.html

## 3. Evidences and Testing

The End to End game flow and Testing results can be found in the Evidences and Testing folder

## 4. Folder Structure

- Evidences and Testing
        Game Screenshots.docx
        Testing Evidences.docx
- TextChoiceGame
        GameOfThrones.py
- Statistics
        states-passed.txt
        stats.txt
        Stats_TextChoiceGame_GOT.ipynb
        Stats_TextChoiceGame_GOT.slides.html
- Resources
        games_of_thrones.mp3
readme.md
