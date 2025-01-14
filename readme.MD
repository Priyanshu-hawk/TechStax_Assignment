# ML Engineer Task

For the [ML Engineer task](https://www.notion.so/ML-Engineer-Task-09beba3065934e8485db8ce418e18710?pvs=21), we will be using the dataset from [Road Accidents](https://drive.google.com/file/d/1edKrdWNOcgbAo2JtckX-PEyM0FdEq4EG/view?usp=drive_link). This dataset provides information about traffic accidents that occurred in the United States.

The ML Engineer task will involve analyzing and processing this dataset to gain insights into various aspects of traffic accidents. This may include tasks such as data cleaning, feature engineering, exploratory data analysis, and building machine learning models.

By leveraging the US Accidents dataset, ML Engineers will have the opportunity to develop models that can **predict accident severity**, identify factors contributing to accidents, or even propose strategies to mitigate accidents based on historical data. This task requires a combination of data processing skills, statistical analysis, and machine learning expertise.

Throughout the ML Engineer task, it is crucial to ensure the accuracy and reliability of the models built. Rigorous testing, validation, and fine-tuning of the models should be conducted to achieve the best possible performance and predictive capabilities.

By working with the Accidents dataset, ML Engineers can contribute to improving road safety, developing intelligent transportation systems, and making data-driven decisions to prevent accidents and minimize their impact.

Outcome Expected:

1. Jupyter notebook with Data Cleaning & Processing 
2. ML Model to **Predict Accident Severity** (Split Data into train-75%, validate-15% & test-10%)
3. Recommendations on the research

Data Description,

| **#** | **Attribute** | **Description** | **Nullable** |
| --- | --- | --- | --- |
| 1 | ID | This is a unique identifier of the accident record. | No |
| 2 | Severity | Shows the severity of the accident, a number between 1 and 4, where 1 indicates the least impact on traffic (i.e., short delay as a result of the accident) and 4 indicates a significant impact on traffic (i.e., long delay). | No |
| 3 | Start_Time | Shows start time of the accident in local time zone. | No |
| 4 | End_Time | Shows end time of the accident in local time zone. End time here refers to when the impact of accident on traffic flow was dismissed. | No |
| 5 | Start_Lat | Shows latitude in GPS coordinate of the start point. | No |
| 6 | Start_Lng | Shows longitude in GPS coordinate of the start point. | No |
| 7 | End_Lat | Shows latitude in GPS coordinate of the end point. | Yes |
| 8 | End_Lng | Shows longitude in GPS coordinate of the end point. | Yes |
| 9 | Distance(mi) | The length of the road extent affected by the accident. | No |
| 10 | Description | Shows natural language description of the accident. | No |
| 11 | Number | Shows the street number in address field. | Yes |
| 12 | Street | Shows the street name in address field. | Yes |
| 13 | Side | Shows the relative side of the street (Right/Left) in address field. | Yes |
| 14 | City | Shows the city in address field. | Yes |
| 15 | County | Shows the county in address field. | Yes |
| 16 | State | Shows the state in address field. | Yes |
| 17 | Zipcode | Shows the zipcode in address field. | Yes |
| 18 | Country | Shows the country in address field. | Yes |
| 19 | Timezone | Shows timezone based on the location of the accident (eastern, central, etc.). | Yes |
| 20 | Airport_Code | Denotes an airport-based weather station which is the closest one to location of the accident. | Yes |
| 21 | Weather_Timestamp | Shows the time-stamp of weather observation record (in local time). | Yes |
| 22 | Temperature(F) | Shows the temperature (in Fahrenheit). | Yes |
| 23 | Wind_Chill(F) | Shows the wind chill (in Fahrenheit). | Yes |
| 24 | Humidity(%) | Shows the humidity (in percentage). | Yes |
| 25 | Pressure(in) | Shows the air pressure (in inches). | Yes |
| 26 | Visibility(mi) | Shows visibility (in miles). | Yes |
| 27 | Wind_Direction | Shows wind direction. | Yes |
| 28 | Wind_Speed(mph) | Shows wind speed (in miles per hour). | Yes |
| 29 | Precipitation(in) | Shows precipitation amount in inches, if there is any. | Yes |
| 30 | Weather_Condition | Shows the weather condition (rain, snow, thunderstorm, fog, etc.) | Yes |
| 31 | Amenity | A [POI](https://wiki.openstreetmap.org/wiki/Points_of_interest) annotation which indicates presence of [amenity](https://wiki.openstreetmap.org/wiki/Key:amenity) in a nearby location. | No |
| 32 | Bump | A POI annotation which indicates presence of speed bump or hump in a nearby location. | No |
| 33 | Crossing | A POI annotation which indicates presence of [crossing](https://wiki.openstreetmap.org/wiki/Key:crossing) in a nearby location. | No |
| 34 | Give_Way | A POI annotation which indicates presence of [give_way](https://wiki.openstreetmap.org/wiki/Tag:highway%3Dgive_way) in a nearby location. | No |
| 35 | Junction | A POI annotation which indicates presence of [junction](https://wiki.openstreetmap.org/wiki/Key:junction) in a nearby location. | No |
| 36 | No_Exit | A POI annotation which indicates presence of [no_exit](https://wiki.openstreetmap.org/wiki/Key:noexit) in a nearby location. | No |
| 37 | Railway | A POI annotation which indicates presence of [railway](https://wiki.openstreetmap.org/wiki/Key:railway) in a nearby location. | No |
| 38 | Roundabout | A POI annotation which indicates presence of [roundabout](https://wiki.openstreetmap.org/wiki/Tag:junction%3Droundabout) in a nearby location. | No |
| 39 | Station | A POI annotation which indicates presence of [station](https://wiki.openstreetmap.org/wiki/Key:station) in a nearby location. | No |
| 40 | Stop | A POI annotation which indicates presence of [stop](https://wiki.openstreetmap.org/wiki/Key:stop) in a nearby location. | No |
| 41 | Traffic_Calming | A POI annotation which indicates presence of [traffic_calming](https://wiki.openstreetmap.org/wiki/Key:traffic_calming) in a nearby location. | No |
| 42 | Traffic_Signal | A POI annotation which indicates presence of [traffic_signal](https://wiki.openstreetmap.org/wiki/Tag:highway%3Dtraffic_signals) in a nearby loction. | No |
| 43 | Turning_Loop | A POI annotation which indicates presence of [turning_loop](https://wiki.openstreetmap.org/wiki/Tag:highway%3Dturning_loop) in a nearby location. | No |
| 44 | Sunrise_Sunset | Shows the period of day (i.e. day or night) based on sunrise/sunset. | Yes |
| 45 | Civil_Twilight | Shows the period of day (i.e. day or night) based on [civil twilight](https://en.wikipedia.org/wiki/Twilight#Civil_twilight). | Yes |
| 46 | Nautical_Twilight | Shows the period of day (i.e. day or night) based on [nautical twilight](https://en.wikipedia.org/wiki/Twilight#Nautical_twilight). | Yes |
| 47 | Astronomical_Twilight | Shows the period of day (i.e. day or night) based on [astronomical twilight](https://en.wikipedia.org/wiki/Twilight#Astronomical_twilight). | Yes |