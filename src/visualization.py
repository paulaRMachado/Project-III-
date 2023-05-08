import folium
from folium import Choropleth, Circle, Marker, Icon, Map
from folium.plugins import HeatMap
import pandas as pd
import json

def start_ups_map(df):
    """
    This function takes a dataFrame with startups locations and marks each location in the map
    arg:
    :df: dataframe with geodata and name os the companies.
    return:
    :map: map with locations plotted
    """
    map = folium.Map(location=[df.loc[0, 'latitude'], df.loc[0, 'longitude']], zoom_start=13,tiles='cartodbpositron', control_scale=True)

    for i, r in df.iterrows():
        tooltip2 = f"STARTUPS: {r['name']}"
        icon = Icon (color = "green", icon_color = "white", icon = "usd", prefix = "fa")
        folium.Marker([r['latitude'], r['longitude']], tooltip=tooltip2, icon=icon).add_to(map)
    
    # add the design company to the map
    icon2 = Icon (color = "beige", icon_color = "white", icon = "tint", prefix = "fa")
    folium.Marker([37.7955307, -122.4005983], tooltip="DESIGN COMPANY", icon=icon2).add_to(map)

    # circle desired area
    folium.Circle(location=[37.7804301,-122.4103305], fill_color='green', radius=3500, weight=2, color="green", popup="Desired Area").add_to(map)
    map.save('image/most_valued_startups.html')
    return map
    
def possible_venues_map(df):
    """
    This function takes a dataFrame with possible office locations marks each location in the map
    arg:
    :df: dataframe with geodata and name os the companies.
    return:
    :map: map with locations plotted
    """
    map = folium.Map(location=[df.loc[0, 'latitude'], df.loc[0, 'longitude']], zoom_start=13,tiles='cartodbpositron', control_scale=True)

    # iterate over the rows in the DataFrame and add a marker for each possible location
    for index, row in df.iterrows():
        tooltip = f"POSSIBLE ACQUISTION: {row['name']}: {row['address']}"
        icon = Icon (color = "blue", icon_color = "white", icon = "building", prefix = "fa")
        folium.Marker([row['latitude'], row['longitude']], tooltip=tooltip, icon=icon).add_to(map)

    # add the design company to the map
    icon2 = Icon (color = "beige", icon_color = "white", icon = "tint", prefix = "fa")
    folium.Marker([37.7955307, -122.4005983], tooltip="DESIGN COMPANY", icon=icon2).add_to(map)

    # circle desired area
    folium.Circle(location=[37.7804301,-122.4103305], fill_color='green', radius=3500, weight=2, color="green").add_to(map)
    map.save('image/possible_offices.html')
    return map
    
def separate_heatmaps(df):
    """
    This function uploads a collection of Json files and draws separated heatmaps for each type of venue 
    and with a dataFrame marks each location in the map. 
    arg:
    :df: dataframe with geodata and name os the companies.
    return:
    :map: map with locations plotted with individual heatmaps associated
    """
    # uploading all data gathered for the region.
    with open("data/pet.json", "r") as f:
        grooming_venues = json.load(f)
    with open("data/starbucks.json", "r") as f:
        starbucks_venues = json.load(f)
    with open("data/school.json", "r") as f:
        school_venues = json.load(f)
    with open("data/bars.json", "r") as f:
        bar_venues = json.load(f)
    with open("data/vegan.json", "r") as f:
        vegan_venues = json.load(f)

    map = folium.Map(location=[df.loc[0, 'latitude'], df.loc[0, 'longitude']],control_scale=True ,zoom_start=14,tiles='cartodbpositron')
    
    # create all the heatmaps for venues (PET, STARBUCKS, SCHOOLS, BARS, VEGAN RESTAURANTS)
    grooming_locations = [(venue['lat'], venue['lon']) for venue in grooming_venues]
    grooming_heatmap = HeatMap(grooming_locations, name='Pet Grooming')
    grooming_heatmap.add_to(map)

    starbucks_locations = [(venue['lat'], venue['lon']) for venue in starbucks_venues]
    starbucks_heatmap = HeatMap(starbucks_locations, name='Starbucks')
    starbucks_heatmap.add_to(map)

    school_locations = [(venue['lat'], venue['lon']) for venue in school_venues]
    school_heatmap = HeatMap(school_locations, name='School')
    school_heatmap.add_to(map)

    bar_locations = [(venue['lat'], venue['lon']) for venue in bar_venues]
    bar_heatmap = HeatMap(bar_locations, name='Bars')
    bar_heatmap.add_to(map)

    vegan_locations = [(venue['lat'], venue['lon']) for venue in vegan_venues]
    vegan_heatmap = HeatMap(vegan_locations, name='Vegan')
    vegan_heatmap.add_to(map)

    # add all possibel offices for takeover
    for index, row in df.iterrows():
        tooltip = f"{row['name']}: {row['address']}"
        icon = folium.Icon (color = "blue", icon_color = "white", icon = "building ", prefix = "fa")
        folium.Marker([row['latitude'], row['longitude']], tooltip=tooltip, icon=icon).add_to(map)
    
    # add the DESIGN company to the plot
    icon2 = Icon (color = "beige", icon_color = "white", icon = "tint", prefix = "fa")
    folium.Marker([37.7955307, -122.4005983], tooltip="DESIGN COMPANY", icon=icon2).add_to(map)
    
    # circle desired area
    folium.Circle(location=[37.7804301,-122.4103305], radius=3500, weight=2, color="green").add_to(map)

    folium.LayerControl().add_to(map)

    map.save('image/heatmap_separate_venues.html')
    return map

def condensed_heatmaps(df):
    """
    This function uploads a collection of Json files condenses them into ONE file and draws a heatmap. 
    And with a dataFrame marks each location in the map. 
    arg:
    :df: dataframe with geodata and name os the companies.
    return:
    :map: map with locations plotted with condensed heatmaps associated
    """
        # uploading all data gathered for the region.
    with open("data/pet.json", "r") as f:
        grooming_venues = json.load(f)
    with open("data/starbucks.json", "r") as f:
        starbucks_venues = json.load(f)
    with open("data/school.json", "r") as f:
        school_venues = json.load(f)
    with open("data/bars.json", "r") as f:
        bar_venues = json.load(f)
    with open("data/vegan.json", "r") as f:
        vegan_venues = json.load(f)

    all_venues = grooming_venues + bar_venues + starbucks_venues + school_venues + vegan_venues

    map = folium.Map(location=[df.loc[0, 'latitude'], df.loc[0, 'longitude']],control_scale=True ,zoom_start=14,tiles='cartodbpositron')
    
    # create all the heatmaps for venues (PET, STARBUCKS, SCHOOLS, BARS, VEGAN RESTAURANTS)
    all_locations = [(venue['lat'], venue['lon']) for venue in all_venues]
    all_locations = HeatMap(all_locations, name='All')
    all_locations.add_to(map)


    # add all possible offices for takeover
    for index, row in df.iterrows():
        tooltip = f"{row['name']}: {row['address']}"
        icon = folium.Icon (color = "blue", icon_color = "white", icon = "building ", prefix = "fa")
        folium.Marker([row['latitude'], row['longitude']], tooltip=tooltip, icon=icon).add_to(map)

    # add the DESIGN company to the plot
    icon2 = Icon (color = "beige", icon_color = "white", icon = "tint ", prefix = "fa")
    folium.Marker([37.7955307, -122.4005983], tooltip="DESIGN COMPANY", icon=icon2).add_to(map)
    
    # circle desired area
    folium.Circle(location=[37.7804301,-122.4103305], radius=3500, weight=2, color="green").add_to(map)

    folium.LayerControl().add_to(map)

    map.save('image/heatmap_CONDENSED_venues.html')
    return map

def short_list_map(df,coffee_near,club_near,bar_near):
    """
    This function ?????
    arg:
    :df: dataframe with geodata and name of selected the companies.
    :coffee_near:
    :club_near:
    :bar_near:
    return:
    :map: map with locations plotted with condensed heatmaps associated
    """
    map = folium.Map(location=[37.7903715,-122.4029651],control_scale=True ,zoom_start=14, tiles='openstreetmap')

    # add narrow list possibel offices for takeover
    for index in df:
        tooltip = f"{index['name']}"
        icon = folium.Icon (color = "blue", icon_color = "white", icon = "building", prefix = "fa")
        folium.Marker([index['latitude'], index['longitude']], tooltip=tooltip, icon=icon).add_to(map)

    # add starbucks
    for cup in coffee_near["results"]:
        icon2 = folium.Icon (
            color = "red",
            icon_color = "white",
            icon = "coffee ",
            prefix = "fa")
        folium.Marker([cup['geocodes']['main']['latitude'], cup['geocodes']['main']['longitude']], tooltip="STARBUCKS", icon=icon2).add_to(map)

    # add night clubs
    for night in club_near["results"]:
        icon3 = folium.Icon (
            color = "beige",
            icon_color = "white",
            icon = "music",
            prefix = "fa")
        folium.Marker([night['geocodes']['main']['latitude'], night['geocodes']['main']['longitude']], tooltip="Night Club", icon=icon3).add_to(map)

    # add night clubs
    for glass in bar_near["results"]:
        icon4 = folium.Icon (
            color = "beige",
            icon_color = "white",
            icon = "beer ",
            prefix = "fa")
        folium.Marker([glass['geocodes']['main']['latitude'], glass['geocodes']['main']['longitude']], tooltip="Bar", icon=icon4).add_to(map)

    # add the BAKETBALL stadium venues to the plot
    with open("data/basketball.json", "r") as f:
        basketball_stadium = json.load(f)
    
    for i in basketball_stadium:
        icon3 = folium.Icon (color = "green", icon_color = "white", icon = "dot-circle", prefix = "fa")
        folium.Marker([i['lat'], i['lon']], tooltip="BASKETBALL STADIUM", icon=icon3).add_to(map)
    
    # add the DESIGN company to the plot
    folium.Marker([37.7955307, -122.4005983], tooltip="DESIGN COMPANY", icon=Icon (color = "beige",icon_color = "white",icon = "tint",prefix = "fa")).add_to(map)
    # add the TOP VEGAN to the plot
    folium.Marker([37.787275, -122.398509], tooltip="Sweetgreen - Second greatest rating", icon=Icon (color = "red",icon_color = "white",icon = "leaf ",prefix = "fa")).add_to(map)
    # add the PET place to the plot
    folium.Marker([37.787963, -122.40664], tooltip="Grooming Spot", icon=Icon (color = "red",icon_color = "white",icon = "paw",prefix = "fa")).add_to(map)
    # add the FERRY TERMINAL  to the plot
    folium.Marker([37.794427, -122.3945625], tooltip="Ferry Terminal", icon=Icon (color = "red",icon_color = "white",icon = "ship",prefix = "fa")).add_to(map)
    # add the AIRPORT to the plot
    folium.Marker([37.7254473 ,-122.2167098], tooltip="International Airport", icon=Icon (color = "red",icon_color = "white",icon = "plane",prefix = "fa")).add_to(map)
    folium.Marker([37.6171039 ,-122.3856554], tooltip="International Airport", icon=Icon (color = "red",icon_color = "white",icon = "plane",prefix = "fa")).add_to(map)
    # add the TRAIN STATION to the plot
    folium.Marker([37.7782029 ,-122.3939985], tooltip="Train Station", icon=Icon (color = "red",icon_color = "white",icon = "train",prefix = "fa")).add_to(map)
    # add the PARK to the plot
    folium.Marker([37.7852176 ,-122.4025011], tooltip="PARK", icon=Icon (color = "darkgreen",icon_color = "white", icon = "tree",prefix = "fa")).add_to(map)

    folium.Circle(location=[37.787646,-122.402759], fill_color="green", radius=2550, weight=2, color="green").add_to(map)

    map.save('image/narrowing_venues.html')
    return map

# For the bonus

def bonus(df,coffee_near,club_near,bar_near):
    """
    This function ?????
    arg:
    :df: dataframe with geodata and name of selected the companies.
    :coffee_near:
    :club_near:
    :bar_near:
    return:
    :map: map with locations plotted with condensed heatmaps associated
    """
    map = folium.Map(location=[37.7903715,-122.4029651],control_scale=True ,zoom_start=14, tiles='openstreetmap')

    # add narrow list possibel offices for takeover
    for index, row in df.iterrows():
        tooltip = f"{row['title']}: {row['metric']}"
        icon = folium.Icon (color = "green", icon_color = "white", icon = "building", prefix = "fa")
        folium.Marker([row['latitude'],row['longitude']], tooltip=tooltip, icon=icon).add_to(map)

        # add starbucks
    for cup in coffee_near["results"]:
        icon2 = folium.Icon (
            color = "red",
            icon_color = "white",
            icon = "coffee ",
            prefix = "fa")
        folium.Marker([cup['geocodes']['main']['latitude'], cup['geocodes']['main']['longitude']], tooltip="STARBUCKS", icon=icon2).add_to(map)

        # add night clubs
        for night in club_near["results"]:
            icon3 = folium.Icon (
            color = "beige",
            icon_color = "white",
            icon = "music",
            prefix = "fa")
            folium.Marker([night['geocodes']['main']['latitude'], night['geocodes']['main']['longitude']], tooltip="Night Club", icon=icon3).add_to(map)

        # add night clubs
        for glass in bar_near["results"]:
            icon4 = folium.Icon (
                color = "beige",
                icon_color = "white",
                icon = "beer ",
                prefix = "fa")
            folium.Marker([glass['geocodes']['main']['latitude'], glass['geocodes']['main']['longitude']], tooltip="Bar", icon=icon4).add_to(map)

        # add the BAKETBALL stadium venues to the plot
        with open("data/basketball.json", "r") as f:
            basketball_stadium = json.load(f)
        
        for i in basketball_stadium:
            icon3 = folium.Icon (color = "green", icon_color = "white", icon = "dot-circle", prefix = "fa")
            folium.Marker([i['lat'], i['lon']], tooltip="BASKETBALL STADIUM", icon=icon3).add_to(map)
        
        # add the DESIGN company to the plot
        folium.Marker([37.7955307, -122.4005983], tooltip="DESIGN COMPANY", icon=Icon (color = "beige",icon_color = "white",icon = "tint",prefix = "fa")).add_to(map)
        # add the TOP VEGAN to the plot
        folium.Marker([37.787275, -122.398509], tooltip="Sweetgreen - Second greatest rating", icon=Icon (color = "red",icon_color = "white",icon = "leaf ",prefix = "fa")).add_to(map)
        # add the PET place to the plot
        folium.Marker([37.787963, -122.40664], tooltip="Grooming Spot", icon=Icon (color = "red",icon_color = "white",icon = "paw",prefix = "fa")).add_to(map)
        # add the FERRY TERMINAL  to the plot
        folium.Marker([37.794427, -122.3945625], tooltip="Ferry Terminal", icon=Icon (color = "red",icon_color = "white",icon = "ship",prefix = "fa")).add_to(map)
        # add the AIRPORT to the plot
        folium.Marker([37.7254473 ,-122.2167098], tooltip="International Airport", icon=Icon (color = "red",icon_color = "white",icon = "plane",prefix = "fa")).add_to(map)
        folium.Marker([37.6171039 ,-122.3856554], tooltip="International Airport", icon=Icon (color = "red",icon_color = "white",icon = "plane",prefix = "fa")).add_to(map)
        # add the TRAIN STATION to the plot
        folium.Marker([37.7782029 ,-122.3939985], tooltip="Train Station", icon=Icon (color = "red",icon_color = "white",icon = "train",prefix = "fa")).add_to(map)
        # add the PARK to the plot
        folium.Marker([37.7852176 ,-122.4025011], tooltip="PARK", icon=Icon (color = "darkgreen",icon_color = "white", icon = "tree",prefix = "fa")).add_to(map)

        map.save('image/bonus.html')
    return map