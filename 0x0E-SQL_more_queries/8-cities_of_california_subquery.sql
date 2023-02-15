-- Lists all the cities of California
--that can be found in the database hbtn_0d_usa
SELECT c.id AS id, name
  FROM cities AS c
 WHERE state_id IN (
    SELECT s.id
      FROM states AS s
     WHERE name = 'California')
 ORDER BY c.id;
