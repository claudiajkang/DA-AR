SELECT ANIMAL_OUTS.ANIMAL_ID, ANIMAL_OUTS.ANIMAL_TYPE, ANIMAL_OUTS.NAME
FROM ANIMAL_OUTS JOIN ANIMAL_INS ON ANIMAL_OUTS.ANIMAL_ID = ANIMAL_INS.ANIMAL_ID
WHERE ANIMAL_INS.SEX_UPON_INTAKE IN ('Intact Male', 'Intact Female') and NOT ANIMAL_OUTS.SEX_UPON_OUTCOME IN ('Intact Male', 'Intact Female')
