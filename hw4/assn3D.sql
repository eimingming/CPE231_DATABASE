CREATE VIEW "view_d" 
AS SELECT P."Pname", D."Dname", COUNT(*)
FROM "PROJECT" P 
JOIN "DEPARTMENT" D ON D."Dnumber" = P."Dnum"
JOIN "WORKS_ON" W ON P."Pnumber" = W."Pno"
GROUP BY P."Pname", D."Dname"
HAVING COUNT(*) > 1;
/**CREATE VIEW

Query returned successfully in 140 msec.**/

select view_d.*
from view_d 