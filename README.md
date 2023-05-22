![](https://homebay.com/wp-content/uploads/2023/03/13d96670-27b2-11ed-b52d-a3f33977cd87-Shutterstock1324591286-1024x576.jpg)
# Project III - GEOmover

## Introduction

This project covers the following scenario:

As a data engineer your goal is to place the new company offices in the best area for the company to grow. You have to find a place that more or less covers the following requirements:

- There must be some nearby companies that also do design.
- 30% of the company staff have at least 1 child.
- It should be near successful tech startups that have raised at least US$1M.
- Executives like Starbucks A LOT.
- Account managers need to travel a lot.
- Everyone in the company is between 25 and 40, give them some place to go party.
- The CEO is vegan.
- If you want to make the maintenance guy happy, a basketball stadium must be around 10 Km.
- The office dog—"Dobby" needs a hairdresser every month. Ensure there's one not too far away.

## Description
### General search :compass:
The selected approach to this project was **OPTION A**, that consists in acquiring the office of an existing company in the database.

For business to thrive it is important to stay close and connected to design companies and startups so there could be potential exchange. So these are the top priorities:

:bangbang: Nearby design companies.

:bangbang: Nearby successful tech startups.

#### Where are these companies?
Searching through the Mongo db for these locations we have:

```python
# for DESIGN companies
query = {"category_code":"design"}
projection = {"name":1, "_id":0, "offices.city":1}
desing = list(c.find(query, projection))
```
There were only a few matches:
| City | # offices |
| ---- | :-----: |
| San Francisco | 1 |
| Collingwood   | 1 |
| Berlin        | 1 |
| Ellensburg    | 1 |
| Brooklyn      | 1 |
| London        | 1 |


```python
# for GAMING companies - competition/exchange
condition1 = {"category_code":"games_video"}
condition2 = {"funding_rounds.raised_amount":{"$gt": 1000000}}
query = {"$and":[condition1,condition2]}
projection = {"name":1, "_id":0, "offices.city":1}
games = list(c.find(query, projection))
```
Theses are the top matches:
| City | # offices |
| ---- | :-----: |
| San Francisco | 39 |
| New York      | 30 |
| Los Angeles   | 11 |
| Paris         | 8 |



```python
#WEB related companies 
condition1 = {"category_code":"web"}
condition2 = {"funding_rounds.raised_amount":{"$gt": 1000000}}
query = {"$and":[condition1,condition2]}
projection = {"name":1, "_id":0, "offices.city":1}
web = list(c.find(query, projection))
```
Theses are the top matches:
| City | # offices |
| ---- | :-----: |
| San Francisco | 71 |
| New York      | 65 |
| Palo Alto     | 22 |
| Seattle       | 20 |
| London       | 20 |

Analizing how the list of cities with design companies intersects with Gaming and Web companies, the most appropriate city for the office would be **SAN FRANCISCO**, even though there is a lot of **competiton**, there is also potential **talent available in the city** and other cities don't have design companies nearby.

### Search for an specific area within SAN FRANCISCO
In order to stay close to successfull startups that raised over US$1M, let's check out where these companies are located and how close they are to the DESIGN company.

![](image/Desired_area.jpg)
*The maps in this project are interactive but GitHub does not show them.


Marked with a circle is the desired area. Let's now see wich offices could make good matches to the new company and its 87 employees.

A quick query through the database shows the number of offices with adequate size:
``` python
condition1 = {"number_of_employees":{"$lt": 120}}
condition2 = {"number_of_employees":{"$gte": 90}}
condition3 = {"offices.city":"San Francisco"}
query = {"$and":[condition1,condition2,condition3]}

pipeline = [
    {"$match": query},
    {"$unwind": "$offices"},
    {"$match": {"offices.city": "San Francisco"}},
    {"$project": {"_id": 0, "name": 1, "latitude": "$offices.latitude", "longitude": "$offices.longitude", "address": "$offices.address1"}}
]
```
Let's check in the map:
![](image/possible_offices.jpg)


### Narrowing down the options
Now let's check the other demands from the staff.
1. Starbucks
2. Schools
3. Bars
4. Vegan places for eating 
5. Grooming places for pets

![](image/most_relevant_area_heatmap.jpg)


The heatmap shows that the area right bellow the location of the Design Company concentrates the most services that the employees deem important, narrowing the selection of possible offices to:
 - Exente: 685, Market Street
 - hi5: 55 Second Street
 - Twilio: 645, Harrison
 - eBuddy: 55, Post Street

### Choosing a location :pushpin:

When pinpointing all the venues to cover the staff requirements, it becomes evident that the EXENT office is the one that has the most services available in the shortest distances and is closest to second best rated vegan restaurant in the city. The location also is 2 blocks away from a Park, so staff could enjoy meals outdoors and relax. Acess to the San Francisco International Airport is facilitated by the train station. There is also a Ferry Station nearby if necessary.

To make the maintenace guy happy, a Basketball Stadium is within 2,5km as shown in the map.

![](image/final_plot.jpg)

## Conclusion

:white_check_mark: There must be some nearby companies that also do design.

:x: 30% of the company staff have at least 1 child. - The nearest school is several blocks away :pleading_face:

:white_check_mark: It should be near successful tech startups that have raised at least US$1M.

:white_check_mark: Executives like Starbucks A LOT.

:white_check_mark: Account managers need to travel a lot.

:white_check_mark: Everyone in the company is between 25 and 40, give them some place to go party.

:white_check_mark: The CEO is vegan.

:white_check_mark: If you want to make the maintenance guy happy, a basketball stadium must be around 10 Km.

:white_check_mark: The office dog—"Dobby" needs a hairdresser every month. Ensure there's one not too far away.

![](https://i.pinimg.com/originals/1c/b0/5e/1cb05ecc2f4f17013e6d574834044585.jpg)


### Coordinates
Exent -- 
latitude: 37.787646
longitude: -122.402759

## Technologies
For this project nine different libraries were used:
- Pymongo
- Pandas
- Getpass
- Dotenv
- OS module
- Requests
- Json
- Folium
- Time

## BONUS
For the bonus part of the project: Our offer to buy the Exent office space was rejected so in order to find another space, a Real State agent from JLL Properties was contacted. Keeping the search in the same previous area, here are the space available for rental and their squared footage.
![](image/Bonus.png)

Using the same criteria as before, the select office from JLL Properties chose was the California Federal Savings building with 2,000 sf. It is still very close the second best vegan restaurant in town, only a bit futher away from the park. 

### New coordinates
California Federal Savings Building: 37.78882, -122.40365