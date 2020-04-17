SELECT CEILING(AVG(Salary) - AVG(CAST(REPLACE(CAST(Salary as char(100)), '0', '') AS unsigned)))
FROM EMPLOYEES