SELECT s.hacker_id, h.name
FROM Submissions as s
INNER JOIN Challenges as c ON s.challenge_id = c.challenge_id
INNER JOIN Difficulty as d ON c.difficulty_level = d.difficulty_level
INNER JOIN Hackers as h ON s.hacker_id = h.hacker_id
WHERE s.score = d.score AND c.difficulty_level = d.difficulty_level
GROUP BY h.hacker_id, h.name
HAVING COUNT(s.HACKER_ID) > 1
ORDER BY COUNT(s.HACKER_ID) DESC, s.HACKER_ID ASC;