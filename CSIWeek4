#1
Select distinct(city) from station where left(city,1) in ('a', 'e', 'i', 'o', 'u') and right(city,1) in ('a', 'e', 'i', 'o', 'u');
#2
select max(population)-min(population) from city;
#3
select
truncate(sqrt(pow(min(lat_n)-max(lat_n),2) + pow(min(long_w) - max(long_w),2)),4)
from station;
#4
with total_rank as (
select lat_n, 
row_number() over(order by lat_n asc) as rnk, count(*) over() as total_count
from station)
select round(avg(lat_n),4) as median
from total_rank
WHERE rnk IN (FLOOR((total_count + 1) / 2), FLOOR((total_count + 2) / 2));
#5
SELECT CITY.NAME FROM CITY JOIN COUNTRY ON CITY.COUNTRYCODE = COUNTRY.CODE WHERE COUNTRY.CONTINENT = "AFRICA";
#6
SELECT CITY.NAME FROM CITY JOIN COUNTRY ON CITY.COUNTRYCODE = COUNTRY.CODE WHERE COUNTRY.CONTINENT = "AFRICA";
#7
select name, grade, marks from students join grades on marks >= min_mark and marks <= max_mark where grade >= 8 order by grade desc, name;
select "NULL", grade, marks from students join grades on marks >= min_mark and marks <= max_mark where grade < 8 order by grade desc , marks;

#8
select h.hacker_id,h.name from hackers h join (select s.hacker_id,s.challenge_id from submissions s where exists (select d.score,c.challenge_id from difficulty d join challenges c on d.difficulty_level=c.difficulty_level where c.challenge_id=s.challenge_id and d.score=s.score)) p on h.hacker_id= p.hacker_id
group by h.hacker_id,h.name having count(p.challenge_id)>1 order by count(p.challenge_id) desc,h.hacker_id asc ;

#9
select w.id, wp.age, x.coins_needed, w.power from (select wp.code, w.power, min(w.coins_needed) coins_needed from wands w join wands_property wp on w.code = wp.code group by wp.code, w.power) x left join wands w on w.code = x.code and w.coins_needed = x.coins_needed and w.power = x.power left join wands_property wp on x.code = wp.code where is_evil = 0 order by w.power desc, wp.age desc;

#0
select h.hacker_id, h.name , sum(s.marks) as total from hackers h left join (select hacker_id,challenge_id,max(score) as marks from submissions group by hacker_id,challenge_id) s on h.hacker_id=s.hacker_id group by h.hacker_id,h.name having total > 0 order by total desc, h.hacker_id asc ;
