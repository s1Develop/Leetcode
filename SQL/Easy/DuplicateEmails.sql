-- SQL Schema
-- Pandas Schema
-- Table: Person

-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | id          | int     |
-- | email       | varchar |
-- +-------------+---------+
-- id is the primary key (column with unique values) for this table.
-- Each row of this table contains an email. The emails will not contain uppercase letters.
 

-- Write a solution to report all the duplicate emails. Note that it's guaranteed that the email field is not NULL.

-- Return the result table in any order.

-- The result format is in the following example.

 

-- Example 1:

-- Input: 
-- Person table:
-- +----+---------+
-- | id | email   |
-- +----+---------+
-- | 1  | a@b.com |
-- | 2  | c@d.com |
-- | 3  | a@b.com |
-- +----+---------+
-- Output: 
-- +---------+
-- | Email   |
-- +---------+
-- | a@b.com |
-- +---------+
-- Explanation: a@b.com is repeated two times.


-- # Write your MySQL query statement below

-- # The SELECT DISTINCT statement is used to return only distinct (different) values.
-- # 즉 DISTINCT하면 중복되는 애들 있으면 딱 한번씩만 나타나게 해주는 것.
SELECT DISTINCT p1.Email
FROM Person p1, Person p2
WHERE p1.EMail = p2.Email and p1.Id != p2.Id