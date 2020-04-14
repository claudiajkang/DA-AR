select s.submission_id, s.hacker_id, s.challenge_id, s.score as sscore, c.difficulty_level, d.score
from submissions s join challenges c on s.challenge_id = c.challenge_id
                   join difficulty d on c.difficulty_level = d.difficulty_level
where s.score = d.score
order by challenge_id, score desc