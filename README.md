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
### General search
The select approach to this project was **OPTION A**, that consists in acquiring the office of an existing company in the database.

For the business to thrive it is important to stay close and connected to design companies and startups so there could be potential exchange.
Search in Mongo for these locations were:

```python
#DESIGN companies
query = {"category_code":"design"}
projection = {"name":1, "_id":0, "offices.city":1}
desing = list(c.find(query, projection))
```
The number of matches were:
- San Francisco    1
- Collingwood      1
- Berlin           1
- Ellensburg       1
- Brooklyn         1
- London           1


```python
#GAMING companies - competition/exchange
condition1 = {"category_code":"games_video"}
condition2 = {"funding_rounds.raised_amount":{"$gt": 1000000}}
query = {"$and":[condition1,condition2]}
projection = {"name":1, "_id":0, "offices.city":1}
```
Top 3 gaming cities:
- San Francisco has 39 companies;
- New York has 30;
- Los Angeles has 11.

```python
#WEB related companies 
condition1 = {"category_code":"web"}
condition2 = {"funding_rounds.raised_amount":{"$gt": 1000000}}
query = {"$and":[condition1,condition2]}
projection = {"name":1, "_id":0, "offices.city":1}
```
Top 3 web cities:
- San Francisco has 71 companies;
- New York has 65;
- Palo Alto 22.

Analizing how the list of cities with design companies intersects with Gaming and Web companies, the most appropriate city for the office would be SAN FRANCISCO, eventhough there is a lot of **competiton**, there is also potential **talent available in the city**.

### Search for an specific area within SAN FRANCISCO
In order to stay close to successfull startups that raised over US$1M, let's check out where these companies are located and how close they are to the DESIGN company.

![map_allvenues](image/Desired_area.jpg)

## Technologies
For this project eight different libraries were used:
- Pymongo
- Pandas
- Getpass
- Dotenv
- OS module
- Requests
- Json
- Folium