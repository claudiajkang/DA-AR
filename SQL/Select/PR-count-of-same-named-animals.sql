SELECT NAME, COUNT(ANIMAL_ID) AS COUNT
FROM ANIMAL_INS
GROUP BY NAME
HAVING COUNT(NAME) > 1