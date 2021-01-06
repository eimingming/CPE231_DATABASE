SELECT distinct E."Fname", P."Pname"
From "EMPLOYEE" E

Join "PROJECT" P
	ON E."Dno" = P."Dnum"
	
Join "WORKS_ON" W
	ON P."Pnumber" = W."Pno"
	
Where E."Dno" = 5 AND W."Hours" > 10 AND P."Pname" = 'ProductX';


Select emp."Fname", emp."Lname" 
from "EMPLOYEE" emp, "WORKS_ON" w, "PROJECT" p 
where emp."Dno" = 5 and emp."ssn" = w."Essn" and w."Pno" = p."pnumber" and p."pname" = ‘ProductX’
and w."Hours">10
Result:
John Smith
Joyce English


SELECT E."Fname", P."Pname"
From "EMPLOYEE" E
Join "PROJECT" P
 ON E."Dno" = P."Dnum"
Join "WORKS_ON" W
 ON E."Ssn" = W."Essn" AND P."Pnumber" = W."Pno"
 


Where E."Dno" = 5 AND W."Hours" > 10 AND P."Pname" = 'ProductX';