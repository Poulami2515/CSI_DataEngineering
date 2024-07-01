 //1
 Select * from CITY;
 //2
 Select * from CITY where ID = 1661
 //3
 select name from Employee order by name;
 //4
 select * from CITY where COUNTRYCODE = 'JPN'
 //5
 select city,state from station;
 //6
 select distinct(city) from station where id%2=0;
 //7
 select count(*)-count(distinct(city)) from station;
 //8
 SELECT CITY, LENGTH(CITY) FROM STATION 
ORDER BY LENGTH(CITY) DESC 
LIMIT 1;
SELECT CITY, LENGTH(CITY) FROM STATION 
ORDER BY LENGTH(CITY), CITY ASC 
LIMIT 1;
 //9
 select floor(avg(population)) from city;
 //0
 select COUNTRY.Continent , floor(avg(CITY.Population)) from COUNTRY inner join CITY on COUNTRY.Code = CITY.CountryCode group by COUNTRY.Continent
