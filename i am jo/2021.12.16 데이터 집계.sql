/*
실습03 - 데이터 집계
*/

-- 데이터베이스 연결
USE myshop2019;

    
-- Q01) 고객의 포인트 합을 조회하세요.
select sum(point) as tot_point
	from customer;


-- Q02) '서울' 지역 고객의 포인트 합을 조회하세요.
select sum(point) as tot_point
	from customer
    where city = '서울';
    

-- Q03) '서울' 지역 고객의 수를 조회하세요.
select count(customer_id) as cutomer_cnt
	from customer
    where city = '서울';


-- Q04) '서울' 지역 고객의 포인트 합과 평균을 조회하세요.
 select sum(point) as tot_point, avg(point) as avg_point
	from customer
    where city = '서울';


    
-- Q05) '서울' 지역 고객의 포인트 합, 평균, 최댓값, 최솟값을 조회하세요.
select sum(point) as tot_point, avg(point) as avg_point, max(point) as max_point, min(point) as min_point
	from customer
    where city = '서울';



-- Q06) 남녀별 고객의 수를 조회하세요.
select gender, count(*) as customer_cnt
	from customer
	group by gender;
    

-- Q07) 지역별 고객의 수를 조회하세요.
--      단, 지역 이름을 기준으로 오름차순 정렬해서 조회하세요.
select city, count(*) as customer_cnt
	from customer
	group by city
    order by city asc;
    
 
 
-- Q08) 지역별 고객의 수를 조회하세요.
--      단, 고객의 수가 10명 이상인 행만 지역 이름을 기준으로 오름차순 정렬해서 조회하세요.
select city, count(*) as customer_cnt
	from customer
	group by city
	having count(*) >= 10
    order by city asc;
    
    
    
-- Q09) 남녀별 포인트 합을 조회하세요.
    select gender, sum(point) as tot_point
	from customer
	group by gender;
    


-- Q10) 지역별 포인트 합을 조회하세요.
--      단, 지역 이름을 기준으로 오름차순 정렬해서 조회하세요.
select city, sum(point) as tot_point
	from customer
	group by city
    order by city asc;


-- Q11) 지역별 포인트 합을 조회하세요.
--      단, 포인트 합이 1,000,000 이상인 행만 포인트 합을 기준으로 내림차순 정렬해서 조회하세요.
select city, sum(point) as tot_point
	from customer
	group by city
    having sum(point) >= 1000000
    order by sum(point) desc;

   
   
-- Q12) 지역별 포인트 합을 조회하세요.
--      단, 포인트 합을 기준으로 내림차순 정렬해서 조회하세요.
    select city, sum(point) as tot_point
		from customer
		group by city
		order by sum(point) desc;


-- Q13) 지역별 고객의 수, 포인트 합을 조회하세요. 
--      단, 지역 이름을 기준으로 오름차순 정렬해서 조회하세요.
select city, count(*) as customer_cnt, sum(point) as tot_point
	from customer
	group by city
    order by city asc;
    


-- Q14) 지역별 포인트 합, 포인트 평균을 조회하세요.
--      단, 포인트가 NULL이 아닌 고객을 대상으로 하며, 지역 이름을 기준으로 오름차순 정렬해서 조회하세요.
select city,sum(point) as tot_point, avg(point) as avg_point
	from customer
    where point is not null
	group by city
    order by city asc;
    


-- Q15) '서울', '부산', '대구' 지역 고객의 지역별, 남녀별 포인트 합과 평균을 조회하세요. ##############몰라
--      단, 지역 이름을 기준으로 오름차순, 같은 지역은 성별을 기준으로 오름차순 정렬해서 조회하세요.
    select city,gender, sum(point) as tot_point, avg(point) as avg_point
	from customer
    where city in('서울','부산','대구','광주')
    group by city, gender
    order by city asc, gender asc;




-- Q16) 2019년 1월 주문에 대하여 고객아이디별 전체금액 합을 조회하세요. ###
select customer_id, sum(total_due) as total_due
	from order_header
    where order_date between '2019.01.01' and '2019.01.31'
    group by customer_id
    order by customer_id asc;


-- Q17) 다음 구문을 실행하여 YEAR, MONTH, DAY 함수 기능을 확인하고, 이후 쿼리문 작성 시 활용하세요.

SELECT order_date, YEAR(order_date) AS order_year, MONTH(order_date) AS order_month, 
       DAY(order_date) AS order_day, total_due
	FROM order_header;


-- Q18) 주문연도별 전체금액 압을 조회하세요.
select year(order_date) as order_year, total_due
	   from order_header
       where total_due
       group by year(order_date);

-- Q19) 2019.01 ~ 2019.06 기간 주문에 대하여 주문연도별, 주문월별 전체금액 합을 조회하세요.
select year(order_date) as order_year, month(order_date) as order_month, sum(total_due) as total_due
	   from order_header
       where order_date between '2019.01.01' and '2019.06.30'
       group by order_year, order_month;


 #Q20) 2019.01 ~ 2019.06 기간 주문에 대하여 주문연도별, 주문월별 전체금액 합과 평균을 조회하세요.
    select year(order_date) as order_year, month(order_date) as order_month, sum(total_due) as total_due, avg(total_due) as avg_total_due
	   from order_header
       where order_date between '2019.01.01' and '2019.06.30'
       group by order_year,order_month;


#날짜 함수 select year('2021.01.01');
#쿼리 처리 순서 - 1.from 2.where
#null 값과 집계 함수 
#where 은 집계 전 having은 집계 후
#having 별칭: 비추(mysql만 가능)
#지역별, 남녀별 : group by city, gender
####
