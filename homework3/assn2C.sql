SELECT E."Fname", E."Lname"
FROM "EMPLOYEE" E
JOIN "EMPLOYEE" E2
ON  E."Super_ssn" = E2."Ssn"
WHERE E2."Fname" = 'Franklin' AND E2."Lname" ='Wong'

SELECT E."Fname", E."Lname"
FROM (SELECT E."Fname", E."Lname", E."Ssn" From "EMPLOYEE" E) as E2
JOIN "EMPLOYEE" E ON E2."Ssn" = E."Super_ssn"
WHERE E2."Fname" = 'Franklin' AND E2."Lname" ='Wong'

SELECT E."Fname", E."Lname"
FROM "EMPLOYEE" E, "EMPLOYEE" S
WHERE E."Super_ssn" = S."Ssn" AND S."Fname" = 'Franklin' AND S."Lname" ='Wong'

