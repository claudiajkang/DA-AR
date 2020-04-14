SELECT IF(G.Grade < 8, NULL, S.NAME), G.Grade, S.MARKS
FROM Students S
         JOIN Grades G ON S.MARKS BETWEEN G.Min_Mark and G.Max_Mark
ORDER BY G.Grade desc, S.Name, S.marks