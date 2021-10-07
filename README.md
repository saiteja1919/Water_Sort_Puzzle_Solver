# Water_Sort_Puzzle_Solver
Solves Water Sort Puzzle game available at [Android](https://play.google.com/store/apps/details?id=com.gma.water.sort.puzzle), [IOS](https://apps.apple.com/us/app/water-sort-puzzle/id1514542157).

> Question: As soon as you start playing you'll see a number of glass tubes with a mixture of colorful water and others that are completely empty. Your mission here is to gradually pour the water from one glass to another until each glass contains a single color.

> Rules: 
* Water of one colour cannot go on top of other colour. The top colour of other tube water being transferred to should match with the colour being transferred in case of a non empty tube. 
* No glass tube overflows. The maximum quantity of glass tube is 4 units at any point of time.


> Expected input:
* Number of glass tubes(T)
* Number of colours(C)
* Next T lines contains 4 space separated colours corresponding to the colours in each glass tube(from top to bottom). Input empty line in case of an empty tube


> Output:

The steps in which the colours to transferred between the tubes(but in **reverse order).
The steps are also stored in "Solving_steps.txt" file in the same order as they are printed.

**There will be a extra space complexity of O(number of steps) if we need to print the steps in correct order.

> Solution: Backtracking <br />
This is a brute force solution and not optimised.

> Sample level:<br />

![alt text](https://github.com/saiteja1919/Water_Sort_Puzzle_Solver/blob/main/sample_level.jpeg)

> Sample Input: <br />

11 <br />
9 <br />
purple pink green deep_blue <br />
deep_blue deep_green purple blue <br />
orange green grey deep_blue <br />
blue orange orange pink <br />
pink red red grey <br />
green deep_green orange deep_blue <br />
blue purple red green <br />
deep_green red deep_green grey <br />
purple grey blue pink <br />
<br />
<br />


> Output:<br />

Printing transactions in reverse order <br />
**************************** <br />
Transfer grey color from 1 to 8 <br />
Transfer deep_green color from 8 to 4 <br />
Transfer deep_blue color from 6 to 11 <br />
Transfer orange color from 6 to 3 <br />
Transfer deep_green color from 6 to 4 <br />
Transfer pink color from 4 to 9 <br />
Transfer orange color from 4 to 3 <br />
Transfer deep_blue color from 3 to 11 <br />
Transfer grey color from 3 to 1 <br />
Transfer deep_blue color from 1 to 11 <br />
Transfer green color from 1 to 7 <br />
Transfer pink color from 1 to 9 <br />
Transfer blue color from 9 to 2 <br />
Transfer grey color from 9 to 3 <br />
Transfer green color from 3 to 7 <br />
Transfer red color from 7 to 10 <br />
Transfer purple color from 7 to 5 <br />
Transfer blue color from 7 to 2 <br />
Transfer green color from 6 to 3 <br />
Transfer orange color from 3 to 4 <br />
Transfer blue color from 4 to 2 <br />
Transfer purple color from 2 to 5 <br />
Transfer grey color from 5 to 9 <br />
Transfer red color from 5 to 10 <br />
Transfer purple color from 10 to 2 <br />
Transfer purple color from 9 to 2 <br />
Transfer deep_green color from 2 to 8 <br />
Transfer red color from 8 to 5 <br />
Transfer deep_green color from 8 to 2 <br />
Transfer pink color from 5 to 1 <br />
Transfer deep_blue color from 2 to 11 <br />
Transfer purple color from 1 to 10 <br />
**************************** <br />
Final values of tubes <br />
1 -- <br />
2 -- blue blue blue blue <br />
3 -- orange orange orange orange <br />
4 -- deep_green deep_green deep_green deep_green <br />
5 -- purple purple purple purple <br />
6 -- <br />
7 -- green green green green <br />
8 -- grey grey grey grey <br />
9 -- pink pink pink pink <br />
10 -- red red red red <br />
11 -- deep_blue deep_blue deep_blue deep_blue <br />

P. S. Games should be played for sole purpose of entertainment but not to just clear levels.
