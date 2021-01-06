/*A*/
INSERT INTO "EMPLOYEE"
VALUES ('Robert',
		'F',
		'Scott',
		'943775543',
		'1972/06/21',
		'2365 Newcastle Rd, Bellaire, TX',
		'M',58000,
		'888665555',
		1);
/*ERROR:  value too long for type character varying(30)*/

/*B*/		
INSERT INTO "PROJECT"
VALUES ('ProductA',
		'4',
		'Bellaire',
		2);
/*
ERROR:  insert or update on table "PROJECT" violates foreign key constraint "PROJECT_Dnum_fkey"
DETAIL:  Key (Dnum)=(2) is not present in table "DEPARTMENT".
*/

/*C*/
INSERT INTO "DEPARTMENT"
VALUES ('Production',
		4,
		'943775543',
		'2007-10-01');
/*ERROR:  duplicate key value violates unique constraint "DEPARTMENT_pkey"
DETAIL:  Key ("Dnumber")=(4) already exists.*/

/*D*/
INSERT INTO "WORKS_ON"
VALUES ('677678989',
		NULL,
		'40.0');
/*ERROR:  null value in column "Pno" violates not-null constraint
DETAIL:  Failing row contains (677678989, null, 40.0)*/

/*E*/
INSERT INTO "DEPENDENT"
VALUES ('453453453',
		'John',
		'M',
		'1990-12-12',
		'spouse');
/*INSERT 0 1   (Don't Error)*/

/*F*/
Delete From "WORKS_ON"
Where "Essn"='333445555';
/*DELETE 4   (Don't Error)*/

/*G*/
Delete From "EMPLOYEE"
Where "Ssn" = '987654321';
/*ERROR:  update or delete on table "EMPLOYEE" violates foreign key constraint "DEPARTMENT_Mgr_ssn_fkey" on table "DEPARTMENT"
DETAIL:  Key (Ssn)=(987654321) is still referenced from table "DEPARTMENT".*/

/*H*/
Delete From "PROJECT"
Where "Pname" = 'ProductX';
/*ERROR:  update or delete on table "PROJECT" violates foreign key constraint "WORK_ON_Pno_fkey" on table "WORKS_ON"
DETAIL:  Key (Pnumber)=(1) is still referenced from table "WORKS_ON".*/

/*I*/
UPDATE "DEPARTMENT"
SET "Mgr_ssn" = '123456789', "Mgr_start_date"= '2007-10-01'
WHERE "Dnumber" = 5;
/*UPDATE 1    (Don't Error)*/

/*J*/
UPDATE "EMPLOYEE"
SET "Super_ssn" = '943775543'
WHERE "Ssn" = '999887777';
/*UPDATE 1    (Don't Error)*/

/*K*/
UPDATE "WORKS_ON"
SET "Hours" = '5'
WHERE "Essn" = '999887777' AND "Pno"= 10;
/*UPDATE 1    (Don't Error)*/