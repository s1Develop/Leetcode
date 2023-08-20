-- SQL Schema
-- Pandas Schema
-- Table: Person

-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | personId    | int     |
-- | lastName    | varchar |
-- | firstName   | varchar |
-- +-------------+---------+
-- personId is the primary key (column with unique values) for this table.
-- This table contains information about the ID of some persons and their first and last names.
 

-- Table: Address

-- +-------------+---------+
-- | Column Name | Type    |
-- +-------------+---------+
-- | addressId   | int     |
-- | personId    | int     |
-- | city        | varchar |
-- | state       | varchar |
-- +-------------+---------+
-- addressId is the primary key (column with unique values) for this table.
-- Each row of this table contains information about the city and state of one person with ID = PersonId.

-- Write your MySQL query statement below
-- Person contains personId, lastName, firstName
-- Address contains addressId, personId, city, state
-- left join 하는거는 대충 (P-A)+(P∩A) 한거

select firstName, lastName, city, state
from Person left join Address
on Person.personId = Address.personId
;
