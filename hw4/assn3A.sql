CREATE VIEW "view_A"
AS SELECT "Dname", "Fname", "Lname", "Salary"
FROM "DEPARTMENT" D
JOIN "EMPLOYEE" E ON E."Dno" = D."Dnumber"
WHERE D."Mgr_ssn" = E."Ssn" 
/** CREATE VIEW

Query returned successfully in 52 msec.**/

select "view_A".*
from "view_A"