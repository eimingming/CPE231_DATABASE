CREATE VIEW manger_info
AS SELECT "Dname", "Fname", "Lname", "Salary"
FROM "DEPARTMENT" D
JOIN "EMPLOYEE" E ON E."Dno" = D."Dnumber"
WHERE D."Mgr_ssn" = E."Ssn" 