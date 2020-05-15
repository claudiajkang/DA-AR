SELECT IF(g.grade < 8, NULL, s.Name), g.Grade, s.Marks
FROM Students s
         JOIN Grades g on s.Marks BETWEEN g.Min_Mark and g.Max_Mark
ORDER BY g.Grade desc, s.name