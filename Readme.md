{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "⚠️ This project is mandatory for certification bloc #1."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "![Kayak](https://seekvectorlogo.com/wp-content/uploads/2018/01/kayak-vector-logo.png)\n",
    "\n",
    "# Plan your trip with Kayak \n",
    "\n",
    "## Company's description 📇\n",
    "\n",
    "<a href=\"https://www.kayak.com\" target=\"_blank\">Kayak</a> is a travel search engine that helps user plan their next trip at the best price.\n",
    "\n",
    "The company was founded in 2004 by Steve Hafner & Paul M. English. After a few rounds of fundraising, Kayak was acquired by <a href=\"https://www.bookingholdings.com/\" target=\"_blank\">Booking Holdings</a> which now holds: \n",
    "\n",
    "* <a href=\"https://booking.com/\" target=\"_blank\">Booking.com</a>\n",
    "* <a href=\"https://kayak.com/\" target=\"_blank\">Kayak</a>\n",
    "* <a href=\"https://www.priceline.com/\" target=\"_blank\">Priceline</a>\n",
    "* <a href=\"https://www.agoda.com/\" target=\"_blank\">Agoda</a>\n",
    "* <a href=\"https://Rentalcars.com/\" target=\"_blank\">RentalCars</a>\n",
    "* <a href=\"https://www.opentable.com/\" target=\"_blank\">OpenTable</a>\n",
    "\n",
    "With over \\$300 million revenue a year, Kayak operates in almost all countries and all languages to help their users book travels accros the globe. "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Project 🚧\n",
    "\n",
    "The marketing team needs help on a new project. After doing some user research, the team discovered that **70% of their users who are planning a trip would like to have more information about the destination they are going to**. \n",
    "\n",
    "In addition, user research shows that **people tend to be defiant about the information they are reading if they don't know the brand** which produced the content. \n",
    "\n",
    "Therefore, Kayak Marketing Team would like to create an application that will recommend where people should plan their next holidays. The application should be based on real data about:\n",
    "\n",
    "* Weather \n",
    "* Hotels in the area \n",
    "\n",
    "The application should then be able to recommend the best destinations and hotels based on the above variables at any given time. "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Goals 🎯\n",
    "\n",
    "As the project has just started, your team doesn't have any data that can be used to create this application. Therefore, your job will be to: \n",
    "\n",
    "* Scrape data from destinations \n",
    "* Get weather data from each destination \n",
    "* Get hotels' info about each destination\n",
    "* Store all the information above in a data lake\n",
    "* Extract, transform and load cleaned data from your datalake to a data warehouse"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Scope of this project 🖼️\n",
    "\n",
    "Marketing team wants to focus first on the best cities to travel to in France. According <a href=\"https://one-week-in.com/35-cities-to-visit-in-france/\" target=\"_blank\">One Week In.com</a> here are the top-35 cities to visit in France: \n",
    "\n",
    "```python \n",
    "[\"Mont Saint Michel\",\n",
    "\"St Malo\",\n",
    "\"Bayeux\",\n",
    "\"Le Havre\",\n",
    "\"Rouen\",\n",
    "\"Paris\",\n",
    "\"Amiens\",\n",
    "\"Lille\",\n",
    "\"Strasbourg\",\n",
    "\"Chateau du Haut Koenigsbourg\",\n",
    "\"Colmar\",\n",
    "\"Eguisheim\",\n",
    "\"Besancon\",\n",
    "\"Dijon\",\n",
    "\"Annecy\",\n",
    "\"Grenoble\",\n",
    "\"Lyon\",\n",
    "\"Gorges du Verdon\",\n",
    "\"Bormes les Mimosas\",\n",
    "\"Cassis\",\n",
    "\"Marseille\",\n",
    "\"Aix en Provence\",\n",
    "\"Avignon\",\n",
    "\"Uzes\",\n",
    "\"Nimes\",\n",
    "\"Aigues Mortes\",\n",
    "\"Saintes Maries de la mer\",\n",
    "\"Collioure\",\n",
    "\"Carcassonne\",\n",
    "\"Ariege\",\n",
    "\"Toulouse\",\n",
    "\"Montauban\",\n",
    "\"Biarritz\",\n",
    "\"Bayonne\",\n",
    "\"La Rochelle\"]\n",
    "```\n",
    "\n",
    "Your team should focus **only on the above cities for your project**. \n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Helpers 🦮\n",
    "\n",
    "To help you achieve this project, here are a few tips that should help you\n",
    "\n",
    "### Get weather data with an API \n",
    "\n",
    "*   Use https://nominatim.org/ to get the gps coordinates of all the cities (no subscription required) Documentation : https://nominatim.org/release-docs/develop/api/Search/\n",
    "\n",
    "*   Use https://openweathermap.org/appid (you have to subscribe to get a free apikey) and https://openweathermap.org/api/one-call-api to get some information about the weather for the 35 cities and put it in a DataFrame\n",
    "\n",
    "*   Determine the list of cities where the weather will be the nicest within the next 7 days For example, you can use the values of daily.pop and daily.rain to compute the expected volume of rain within the next 7 days... But it's only an example, actually you can have different opinions on a what a nice weather would be like 😎 Maybe the most important criterion for you is the temperature or humidity, so feel free to change the rules !\n",
    "\n",
    "*   Save all the results in a `.csv` file, you will use it later 😉 You can save all the informations that seem important to you ! Don't forget to save the name of the cities, and also to create a column containing a unique identifier (id) of each city (this is important for what's next in the project)\n",
    "\n",
    "*   Use plotly to display the best destinations on a map\n",
    "\n",
    "### Scrape Booking.com \n",
    "\n",
    "Since BookingHoldings doesn't have aggregated databases, it will be much faster to scrape data directly from booking.com \n",
    "\n",
    "You can scrap as many information asyou want, but we suggest that you get at least:\n",
    "\n",
    "*   hotel name,\n",
    "*   Url to its booking.com page,\n",
    "*   Its coordinates: latitude and longitude\n",
    "*   Score given by the website users\n",
    "*   Text description of the hotel\n",
    "\n",
    "\n",
    "### Create your data lake using S3 \n",
    "\n",
    "Once you managed to build your dataset, you should store into S3 as a csv file. \n",
    "\n",
    "### ETL \n",
    "\n",
    "Once you uploaded your data onto S3, it will be better for the next data analysis team to extract clean data directly from a Data Warehouse. Therefore, create a SQL Database using AWS RDS, extract your data from S3 and store it in your newly created DB. "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Deliverable 📬\n",
    "\n",
    "To complete this project, your team should deliver:\n",
    "\n",
    "* A `.csv` file in an S3 bucket containing enriched information about weather and hotels for each french city\n",
    "\n",
    "* A SQL Database where we should be able to get the same cleaned data from S3 \n",
    "\n",
    "* Two maps where you should have a Top-5 destinations and a Top-20 hotels in the area. You can use plotly or any other library to do so. It should look something like this: \n",
    "\n",
    "![Map](https://full-stack-assets.s3.eu-west-3.amazonaws.com/images/Kayak_best_destination_project.png)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
