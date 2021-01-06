SELECT "Fname", "Lname"
FROM "EMPLOYEE" E
WHERE E."Dno" IN (SELECT "Dno"
				   FROM "EMPLOYEE" E2
			 	   WHERE E2."Salary" IN (SELECT max("Salary")
										 FROM "EMPLOYEE"));

