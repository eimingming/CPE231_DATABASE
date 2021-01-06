SELECT "Dname", COUNT (*)
FROM "DEPARTMENT" D
JOIN "EMPLOYEE" E ON D."Dnumber"=E."Dno"
WHERE E."Sex" = 'M' AND E."Dno" IN (SELECT E."Dno" 
									FROM "EMPLOYEE" E2 
									GROUP BY "Dname"
									HAVING AVG (E2."Salary") > 30000 )
GROUP BY "Dname";



/**
SELECT "Dname", COUNT (*)
FROM "DEPARTMENT" D
JOIN "EMPLOYEE" E ON D."Dnumber"=E."Dno"
WHERE E."Sex" = 'M' 
GROUP BY "Dname"
HAVING AVG (E."Salary") > 30000
**/