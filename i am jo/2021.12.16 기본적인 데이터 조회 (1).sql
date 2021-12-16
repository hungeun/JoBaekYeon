/*
실습01 - 기본적인 데이터 조회 (1)
*/
####
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
select customer_name, customer_id, gender,phone,point
		from customer;



-- Q07) 모든 고객의 아이디, 이름, 지역, 성별, 이메일, 전화번호를 조회하세요.
select customer_id, customer_name, city, gender, email,phone
		from customer;


 
-- Q08) 모든 직원의 이름, 사원번호, 성별, 입사일, 전화번호를 조회하세요.
select employee_name, employee_id, gender, hire_date, phone
		from employee;


    
-- Q09) 이름이 '홍길동'인 고객의 이름, 아이디, 성별, 지역, 전화번호, 포인트를 조회하세요.
select customer_name, customer_id, gender, city, phone, point
		from customer
        where customer_name = '홍길동';



-- Q10) 여자 고객의 이름, 아이디, 성별, 지역, 전화번호, 포인트를 조회하세요.
select customer_name, customer_id, gender, city, phone, point
		from customer
        where gender = 'f';


-- Q11) '울산' 지역 고객의 이름, 아이디, 성별, 지역, 전화번호, 포인트를 조회하세요.
select customer_name, customer_id, gender, city, phone, point
		from customer
        where city = '울산';


-- Q12) 포인트가 500,000 이상인 고객의 이름, 아이디, 성별, 지역, 전화번호, 포인트를 조회하세요.
select customer_name, customer_id, gender, city, phone, point
		from customer
        where point >= '500000' ;


-- Q13) 이름에 공백이 들어간 고객의 이름, 아이디, 성별, 지역, 전화번호, 포인트를 조회하세요.
select customer_name, customer_id, gender, city, phone, point
		from customer
        where customer_name like '%';


-- Q14) 전화번호가 010으로 시작하지 않는 고객의 이름, 아이디, 성별, 지역, 전화번호, 포인트를 조회하세요.
select customer_name, customer_id, gender, city, phone, point
		from customer
        where phone not like '%010%';
 
 
-- Q15) 포인트가 500,000 이상 '서울' 지역 고객의 이름, 아이디, 성별, 지역, 전화번호, 포인트를 조회하세요.
select customer_name, customer_id, gender, city, phone, point
		from customer
        where point >= '500000' and city = '서울';


-- Q16) 포인트가 500,000 이상인 '서울' 이외 지역 고객의 이름, 아이디, 성별, 지역, 전화번호, 포인트를 조회하세요.
select customer_name, customer_id, gender, city, phone, point
		from customer
        where point >= '500000' and not city = '서울';



-- Q17) 포인트가 400,000 이상인 '서울' 지역 남자 고객의 이름, 아이디, 성별, 지역, 전화번호, 포인트를 조회하세요.
select customer_name, customer_id, gender, city, phone, point
		from customer
        where point >= '400000' and city = '서울' and gender = 'm';
 
# show tables; table 보기
#describe customer; customer테이블 구조 보기
#세미클론(;)
#마지막 행의 null은 무시
#이름에 공백 customer_name like '% %' : 한칸 띄기
#sql은 내가 원하는 것이 무엇인지를 젛의 가져오는것은 서버가 결정 -> where a = 'A' // where a in ('A')
#alter table order_detail 
#--change drder_id order_detail_id int; 테이블 수정 
        
        
select customer_name, customer_id, phone, ifnull(point,0) as add_point
		from customer
        where point is null and customer_id like 'an%';
   
#21   
select customer_name,register_date, point+10000 as sum_point
	from customer
    where (2021- year(register_date)) >= '4' 
    order by year(register_date);
   
 #22
select custmer_name, phone,point
	from customer
    where (2021- year(register_date)) >= '6';
    


