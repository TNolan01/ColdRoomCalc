![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

#### Project No.3 based on Code Institute template for deployment.

# Cold Room Calculation Software:

### Project Scope:
<p>The scope of this project is to create a simple command line driven program written in Python. I have written Python program to calculate the power requirement in kilowatts of the refrigeration equipment needed for cold and freezer storage rooms.</p>

<p>The program intakes a number of variables from the user to make this calculation. The following list main criteria required to work on the refrigeration duty.</p>

#### Inputs Values
<ul>
<li> Measurements of storage room, surface area and volume. </li> 
<li> Target/storage temperature of the room. </li>
<li> Quantity and temperature of product. </li>
</ul>

#### Output Values
<ul>
<li></li>

### Project Design:
<p>The project is a command line based program run running in a compact terminal window. As the program is designed to be functional and practical.
I have used colorama to add some color changes to the text.</p>
<p>In instances where the user has entered and invalid input the text which prompts them to enter a value of the correct type or inside the correct is red in color.</p>


### Project Structure:
<p>The program asks the user to entry data required to make the calcultaions necessary in a step ny step process.</p>
#### Data Required:
<span style="color: orange">Length, width and height of the walls:</span> 
<p>The dimensions of the refrigerated room are required in order to calculate the volume of the room and surface area of the walls.</p>
<br>
<span style="color: orange">Thickness of the insulated panel from which the room is constructed:</span> 
<p>The user has numerical choice 1 to 4 to choice the type of insulated panel from which the room is constructed. Each choice has an associated U valve for its insulation properites. The lower the thicker the insulation, the lower the U value and hence the lower the amount of energy required to achieve the rooms target temperature.</p>
<br>
<span style="color: orange">Target temperature:</span> 
<p>The target temperature is the temperature we want the room to achieve and hold. The temperature range for chill room is +2 to +4°C, the target temperature for a freezer room would be -18 to -20°C. For particular applications or storage the target temperature can span between those two figures. The lower the target temperature is the higher the required power duty will be.</p>
<br>
<span style="color: orange">Floor insulation:</span> 
<p>The user is offered a yes / no choice, is there insulation under the floor? If the floor has insulation it recieves a higher U value.</p>
<br>
<span style="color: orange">Quantity of product:</span> 
<p>The quantity of product entering the refrigerated room in a 24 hour period is necessary as it forms a large part of the heat load. This is numerical figure and represents the quantity in kilograms </p>
<br>
<span style="color: orange">Temperature of the product:</span> 
<p>The entry temperature of the product will form the largest heat input value. The higher the temperature of the product the harder the refrigeration equipment will be required to work and ergo the higher power required.</p>
<br>
<span style="color: orange">Are there people in the room?:</span> 
<p>Another potentially significant source of heat is the presence of people working inside the room walls and generating additional heat which needs to be countered.</p>
<br>
<span style="color: orange">Number of door openings:</span> 
<p>The greater the number of door openings the larger the number of air changes. Refrigerated air leaving the room during door openings will be replaced with warm ambient air which will need to be chilled to the meet the target temperature, this will effect the required. A refrigerated room which experiences multiple loadings and unloadings during the day will need to work harder to replace the lost cold air. </p>
<br>








Welcome TNolan01,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **August 17, 2021**

## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!