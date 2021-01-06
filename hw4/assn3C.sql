CREATE VIEW "view_c2"
AS SELECT P."Pname", D."Dname", COUNT(*), sum(W."Hours")
FROM "PROJECT" P 
JOIN "DEPARTMENT" D ON D."Dnumber" = P."Dnum"
JOIN "WORKS_ON" W ON P."Pnumber" = W."Pno"
GROUP BY P."Pname", D."Dname";
/*CREATE VIEW

Query returned successfully in 304 msec.*/

select view_c2.*
from view_c2