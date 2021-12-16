/*
실습01 - 기본적인 데이터 조회 (1)
*/

-- 데이터베이스 연결
USE MyShop2019;


-- Q01) customer 테이블 모든 행과 열을 조회하고 어떤 열들이 있는지, 데이터 형식은 어떻게 되는지 살펴보세요.
select * from customer;


-- Q02) employee 테이블 모든 행과 열을 조회하고 어떤 열들이 있는지, 데이터 형식은 어떻게 되는지 살펴보세요.
select * from employee;


-- Q03) product 테이블 모든 행과 열을 조회하고 어떤 열들이 있는지, 데이터 형식은 어떻게 되는지 살펴보세요.
select * from product;


-- Q04) order_header 테이블 모든 행과 열을 조회하고 어떤 열들이 있는지, 데이터 형식은 어떻게 되는지 살펴보세요.
select * from order_header;


-- Q05) order_detail 테이블 모든 행과 열을 조회하고 어떤 열들이 있는지, 데이터 형식은 어떻게 되는지 살펴보세요.
select * from order_detail;


-- Q06) 모든 고객의 이름, 아이디, 성별, 지역, 전화번호, 포인트를 조회하세요.
select customer_name, customer_id, gender, city, phone, point from customer;


-- Q07) 모든 고객의 아이디, 이름, 지역, 성별, 이메일, 전화번호를 조회하세요.
select customer_id, customer_name, city, gender, email, phone from customer;
 
 
-- Q08) 모든 직원의 이름, 사원번호, 성별, 입사일, 전화번호를 조회하세요.
select employee_name, employee_id, gender, hire_date, phone from employee;

    
-- Q09) 이름이 '홍길동'인 고객의 이름, 아이디, 성별, 지역, 전화번호, 포인트를 조회하세요.
select customer_name, customer_id, gender, city, phone, point from customer where customer_name = '홍길동';


-- Q10) 여자 고객의 이름, 아이디, 성별, 지역, 전화번호, 포인트를 조회하세요.
select customer_name, customer_id, gender, city, phone, point from customer where gender = 'f';


-- Q11) '울산' 지역 고객의 이름, 아이디, 성별, 지역, 전화번호, 포인트를 조회하세요.
select customer_name, customer_id, gender, city, phone, point from customer where city = '울산';


-- Q12) 포인트가 500,000 이상인 고객의 이름, 아이디, 성별, 지역, 전화번호, 포인트를 조회하세요.
select customer_name, customer_id, gender, city, phone, point from customer where point >= 500000;


-- Q13) 이름에 공백이 들어간 고객의 이름, 아이디, 성별, 지역, 전화번호, 포인트를 조회하세요.
select customer_name, customer_id, gender, city, phone, point from customer where customer_name like "% %";


-- Q14) 전화번호가 010으로 시작하지 않는 고객의 이름, 아이디, 성별, 지역, 전화번호, 포인트를 조회하세요.
select customer_name, customer_id, gender, city, phone, point from customer where phone not like "010%";
 
 
-- Q15) 포인트가 500,000 이상 '서울' 지역 고객의 이름, 아이디, 성별, 지역, 전화번호, 포인트를 조회하세요.
select customer_name, customer_id, gender, city, phone, point from customer where point >= 500000 and city = '서울';


-- Q16) 포인트가 500,000 이상인 '서울' 이외 지역 고객의 이름, 아이디, 성별, 지역, 전화번호, 포인트를 조회하세요.
select customer_name, customer_id, gender, city, phone, point from customer where point >= 500000 and city <> '서울';


-- Q17) 포인트가 400,000 이상인 '서울' 지역 남자 고객의 이름, 아이디, 성별, 지역, 전화번호, 포인트를 조회하세요.
select customer_name, customer_id, gender, city, phone, point from customer where point >= 400000 and city = '서울' and gender = 'm';

-- q18) 포인트가 없는 고객의 이름, 아이디, 전화번호, 포인트를 조회하고 5000 point씩 주어라
select customer_name, customer_id, phone, coalesce(point, 5000) from customer where point is null;
-- q20)
select customer_id, coalesce(point, 0) from customer where customer_id like 'an%';

select point from customer where customer_name = '김아기';

-- q21 등록한지 4년이 지난 고객들을 조회하고 포인트를 10000씩 추가하라
select customer_name, point + 10000 as point, register_date from customer where (2021 - year(register_date)) >= 4;
-- q22 일한지 6년이 지난 직원의 이름과 전화번호를 조회하라alter
select employee_name, phone from employee where (2021 - year(hire_date)) >= 6;

-- q23 지역별 포인트 가장 많은 고객의 이름과 전화번호, 포인트를 출력하라.
select customer_name, phone, city, max(point) as '최고 고객' from customer group by city;
-- q24 이메일이 gmeil을 사용하는 고객의 이름과 이메일을 조회하라
select customer_name, email from customer where email like '%gmeil%';

-- 테이블 목록보기
show tables;

-- 테이블 구조 보기
DESCRIBE customer;