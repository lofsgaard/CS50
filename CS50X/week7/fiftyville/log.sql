-- Keep a log of any SQL queries you execute as you solve the mystery.


-- Check Humphrey street
select * from crime_scene_reports where street like 'Humphrey Street' and id like '295';

--Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery.
--Interviews were conducted today with three witnesses who were present at the time – each of their interview transcripts mentions the bakery.

-- check bakery_security_logs for the correct day

select * from bakery_security_logs where day like '28' and license_plate like '94KL13X' or license_plate like '1106N58' or license_plate like '4328GD8';

-- entry 10:08 R3G7486
-- entry 10:14 13FNH73
-- entry 10:

-- 28.07

-- suspect Bruke and Tayloer. Both entered and left right after the robbery. More bruce as he left 3 minutes after robbery. Luca also left 10:19

-- licence plate exit 11J91FW

--check entry

select name, transcript from interviews where name like 'Teresa';

-- check interviews for mentions of bakery
select * from interviews where transcript like '%bakery%';

-- Everything is from the 28th july
-- Ruth: 10 minutes after robbery, check security logs:
-- Eugene: Recognized, check ATM same day. Withdraw money
-- Raymond: Calling as they were leaving, less than 1 min earlies flight the day after.

| 258 | 2021 | 7     | 28  | 10   | 8      | entrance | R3G7486       |
| 259 | 2021 | 7     | 28  | 10   | 14     | entrance | 13FNH73       |
| 260 | 2021 | 7     | 28  | 10   | 16     | exit     | 5P2BI95       |
| 261 | 2021 | 7     | 28  | 10   | 18     | exit     | 94KL13X       |
| 262 | 2021 | 7     | 28  | 10   | 18     | exit     | 6P58WS2       |
| 263 | 2021 | 7     | 28  | 10   | 19     | exit     | 4328GD8       |
| 264 | 2021 | 7     | 28  | 10   | 20     | exit     | G412CB7       |
| 265 | 2021 | 7     | 28  | 10   | 21     | exit     | L93JTIZ       |
| 266 | 2021 | 7     | 28  | 10   | 23     | exit     | 322W7JE       |
| 267 | 2021 | 7     | 28  | 10   | 23     | exit     | 0NTHK55       |
| 268 | 2021 | 7     | 28  | 10   | 35     | exit     | 1106N58

-- check ATM log for Humphrey Street

select account_number, transaction_type, amount
from atm_transactions
where atm_location like 'Leggett Street' and transaction_type like 'withdraw' and day like '28';

-- check bank acccounts

select account_number, person_id, people.name, people.passport_number, people.license_plate, people.phone_number
from bank_accounts
inner join people on people.id = bank_accounts.person_id
where account_number in
(select account_number
from atm_transactions
where atm_location like 'Leggett Street' and transaction_type like 'withdraw' and day like '28') and
people.license_plate like '94KL13X' or license_plate like '1106N58' or license_plate like '4328GD8';

| account_number | person_id | creation_year |
+----------------+-----------+---------------+
| 49610011       | 686048    | 2010          |
| 26013199       | 514354    | 2012          |
| 16153065       | 458378    | 2012          |
| 28296815       | 395717    | 2014          |
| 25506511       | 396669    | 2014          |
| 28500762       | 467400    | 2014          |
| 76054385       | 449774    | 2015          |
| 81061156       | 438727    | 2018

select * from atm_transactions where atm_location like 'Leggett Street' and transaction_type like 'withdraw' and day like '28'

| id  | account_number | year | month | day |  atm_location  | transaction_type | amount |
+-----+----------------+------+-------+-----+----------------+------------------+--------+
| 246 | 28500762       | 2021 | 7     | 28  | Leggett Street | withdraw         | 48     |
| 264 | 28296815       | 2021 | 7     | 28  | Leggett Street | withdraw         | 20     |
| 266 | 76054385       | 2021 | 7     | 28  | Leggett Street | withdraw         | 60     |
| 267 | 49610011       | 2021 | 7     | 28  | Leggett Street | withdraw         | 50     |
| 269 | 16153065       | 2021 | 7     | 28  | Leggett Street | withdraw         | 80     |
| 288 | 25506511       | 2021 | 7     | 28  | Leggett Street | withdraw         | 20     |
| 313 | 81061156       | 2021 | 7     | 28  | Leggett Street | withdraw         | 30     |
| 336 | 26013199       | 2021 | 7     | 28  | Leggett Street | withdraw         | 35

-- check flights

select * from flights where day like '29';

-- earliest time 9:20 destination 4

select * from airports where id like '4';

-- destination New York City

-- call log from same day, lasting less than 60 seconds

select *
from phone_calls
where day like '28' and duration < '60' and caller like '(367) 555-5533' or caller like '(389) 555-5198' or caller like '(286) 555-6063';

-- Bruce called (375) 555-8161 for 45 sec same day
-- Taylor called (676) 555-6554 for 43 sec same day


select * from people where phone_number like '(375) 555-8161' or phone_number like '(676) 555-6554';

-- Might be taylor because Robin that bruce called has no passport. Making James the accomplice?
-- wrong
select * from passengers where flight_id like '36'; -- taylor is in seat 6c. 6D =  8294398571
select * from flights where day like '29';


9878712108 8496433585

select * from people where passport_number like '9878712108' or passport_number like '8496433585';

-- Trying Bruce and Robin, said earlier that Robin has no passport. But you dont need one to fly inside USA.