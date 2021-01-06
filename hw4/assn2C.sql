SELECT "Fname", "Lname"
FROM "EMPLOYEE" E
WHERE E."Super_ssn" IN (SELECT "Ssn" 
						FROM "EMPLOYEE" 
						WHERE "Super_ssn" = '888665555');