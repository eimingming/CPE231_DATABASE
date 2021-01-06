SELECT E."Fname", E."Lname"
FROM "EMPLOYEE" E
JOIN "DEPENDENT" D 
ON E."Ssn" = D."Essn" 
WHERE "Fname" = "Dependent_name"
					
SELECT E."Fname", E."Lname"
FROM "EMPLOYEE" E
WHERE EXISTS ( SELECT D."Essn" 
				  	FROM "DEPENDENT" D
					WHERE "Fname" = "Dependent_name" )
					
					
					
select E."Fname", E."Lname"
from  "EMPLOYEE" E, "DEPENDENT" D
where E."Ssn" = d."Essn"
and  "Fname" = "Dependent_name"





