# $`\textcolor{blue}{\text{Visualizations}}`$
A set of scripts and files illustrating data visualization techniques.
Richard Ay (February 2024, *updated February 2024*)

## $`\textcolor{blue}{\text{Table of Contents}}`$
* [Setup](#setup)
* [Environment](#environment)
* [Usage](#Usage)
* [References](#references)
* [File List](#file-list)
* [Technologies and Imports](#Technologies-and-Imports)
* [Images](#Images)

## Setup

*To use this program, activate the 'virtual environment' "VisualEnv".  

## Environment
A virtual environment is created so that the installation of matplotlib and plotly
remain local to this subdirectory, and do not affect the rest of the machine.

The virtual environment can be setup using the command: 
**'python -m venv "VisualEnv" --upgrade-deps --prompt="VisualEnv"'**

To start/stop the virtual environment, use the commands: **'VisualEnv\scripts\activate'** 
or **'deactivate'**. Once activated, the virtual environment will change the (terminal) 
prompt from (PS) to (VisualnEnv).

After starting the virtual environment, matplotlib and plotly (and pandas) can be installed 
with the commands:  
**'python -m pip install matplotlib'**  
**'python -m pip install plotly'**  
**'python -m pip install pandas'**  

Subsequently the installations can be verified with the command:   
**'python -m pip show matplotlib'**  
**'python -m pip show plotly'**  
**'python -m pip show pandas'** 


## Usage
From VSCode, by issuing the commands (note the suffix ".py' is required)  
- 'python squares_plot.py'  
- 'python scatter_plot.py'  
- 'python random_walk_plot.py'   
- 'python die_visual.py'  


## References
1. Python Crash Course, Eric Matthes, No Starch Press, 2023. Chapters 12-14.  


## File List
**die.py** - a script to manage the "dice" class.  
**die_visual.py** - a script to roll dice and display the results.  
**random_walk_plot.py** - the script to product the 'random-walk' images.  
**random_walk.py** - a class module that creates the data points for random-walk_plot.   
**scatter_plot.py** - a script that generates a scatter plot of squared numbers.   
**squares_plot.py**  - a script that generates a line plot of squared numbers.  1


**/images** - a subdirectory with script images  


## Technologies and Imports
The following modules are necessary imports (imported in the .py files):  
- matplotlib  
- plotly
- pandas
 

## Images
The images below show the resulting visualizations generated by the scripts:  

The 'squares' plot:    
![Squares Plot](https://github.com/CaptainRich/Visualizations/blob/main/images/squares_plot.png)  

The 'scatter' plot:  
![Scatter Plot](https://github.com/CaptainRich/Visualizations/blob/main/images/scatter_plot.png)  

The 'random walk' plot:  
![Random Walk Plot](https://github.com/CaptainRich/Visualizations/blob/main/images/random_walk.png)  

The 'die roll' plot:  
![Die Roll Plot](https://github.com/CaptainRich/Visualizations/blob/main/images/die_roll_results.png)  



