/*
실습03 - 데이터 집계
*/

-- 데이터베이스 연결
USE myshop2019;

    
-- Q01) 고객의 포인트 합을 조회하세요.
select sum(point) as tot_point


-- Q02) '서울' 지역 고객의 포인트 합을 조회하세요.

select sum(point) as tot_point from customer where city = '서울';
    

-- Q03) '서울' 지역 고객의 수를 조회하세요.
select count(*) as  customer_cnt from customer where city = '서울';


-- Q04) '서울' 지역 고객의 포인트 합과 평균을 조회하세요.
 select sum(point) as tot_point, avg(point) as avg_point from customer where city = '서울';

    
-- Q05) '서울' 지역 고객의 포인트 합, 평균, 최댓값, 최솟값을 조회하세요.
select sum(point) as tot_point, avg(point) as avg_point, max(point) as max_point, min(point) as min_point from customer where city = '서울';


-- Q06) 남녀별 고객의 수를 조회하세요.
select gender, count(*) as customer_cnt from customer group by gender;


-- Q07) 지역별 고객의 수를 조회하세요.
--      단, 지역 이름을 기준으로 오름차순 정렬해서 조회하세요.
select city, count(*) as customer_cnt from customer group by city order by city;
 
 
-- Q08) 지역별 고객의 수를 조회하세요.
--      단, 고객의 수가 10명 이상인 행만 지역 이름을 기준으로 오름차순 정렬해서 조회하세요.
select city, count(*) as customer_cnt from customer group by city having count(*) >= 10 order by city;
    
    
-- Q09) 남녀별 포인트 합을 조회하세요.
select gender, sum(point) as tot_point from customer group by gender;


-- Q10) 지역별 포인트 합을 조회하세요.
--      단, 지역 이름을 기준으로 오름차순 정렬해서 조회하세요.
select city, sum(point) as tot_point from customer group by city order by city;


-- Q11) 지역별 포인트 합을 조회하세요.
--      단, 포인트 합이 1,000,000 이상인 행만 포인트 합을 기준으로 내림차순 정렬해서 조회하세요.
select city, sum(point) as tot_point from customer group by city having tot_point >= 1000000 order by tot_point desc;
   
   
-- Q12) 지역별 포인트 합을 조회하세요.
--      단, 포인트 합을 기준으로 내림차순 정렬해서 조회하세요.
select city, sum(point) as tot_point from customer group by city order by tot_point desc;    


-- Q13) 지역별 고객의 수, 포인트 합을 조회하세요.
--      단, 지역 이름을 기준으로 오름차순 정렬해서 조회하세요.
select city, count(*) as customer_cnt, sum(point) as tot_point from customer group by city order by city;


-- Q14) 지역별 포인트 합, 포인트 평균을 조회하세요.
--      단, 포인트가 NULL이 아닌 고객을 대상으로 하며, 지역 이름을 기준으로 오름차순 정렬해서 조회하세요.
select city, sum(point) as tot_point, avg(point) as avg_point from customer where point is not null group by city order by city;


-- Q15) '서울', '부산', '대구' 지역 고객의 지역별, 남녀별 포인트 합과 평균을 조회하세요.
--      단, 지역 이름을 기준으로 오름차순, 같은 지역은 성별을 기준으로 오름차순 정렬해서 조회하세요.
    select city, gender, sum(point) as tot_point, avg(point) as avg_point
    from customer
    where city in ('서울', '부산', '대구') 
    group by city, gender
    order by city, gender;

-- Q16) 2019년 1월 주문에 대하여 고객아이디별 전체금액 합을 조회하세요.
select customer_id, sum(total_due) as total_due from order_header where order_date like '2019-01%' group by customer_id;







-- Q17) 다음 구문을 실행하여 YEAR, MONTH, DAY 함수 기능을 확인하고, 이후 쿼리문 작성 시 활용하세요.



-- Q18) 주문연도별 전체금액 압을 조회하세요.
select year(order_date) as order_year, sum(total_due) as total_due from order_header group by order_year;


-- Q19) 2019.01 ~ 2019.06 기간 주문에 대하여 주문연도별, 주문월별 전체금액 합을 조회하세요.
select year(order_date) as order_year, month(order_date) as order_month, sum(total_due) from order_header where order_date between '2019-01-01' and '2019-06-30' group by order_year, order_month;


select * from order_header;
-- Q20) 2019.01 ~ 2019.06 기간 주문에 대하여 주문연도별, 주문월별 전체금액 합과 평균을 조회하세요.
select year(order_date) as order_year, month(order_date) as order_month, sum(total_due), avg(total_due) as avg_t from order_header where order_date between '2019-01-01' and '2019-06-30' group by order_year, order_month;

