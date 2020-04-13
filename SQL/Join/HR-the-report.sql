select IF(g.grade < 8, NULL, s.name), g.grade, s.marks
from students s
         inner join grades g on s.marks between g.min_mark and g.max_mark
order by g.grade DESC, s.name, s.marks;