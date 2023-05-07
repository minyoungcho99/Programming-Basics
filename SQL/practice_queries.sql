-- concat(), distinct, select ~ from ~ where ~, order by ~ (asc)/desc, '1999-08-13', order by lname, fname address like '%Houston%', '%aya_%', having

-- practiceQuery0
select bdate, address from employee where fname = 'John' and lname = 'Smith';

-- practiceQuery1
select fname, lname, address from employee where dno in (select dnumber from department where dname = 'Research');

-- practiceQuery2 ***
select pnumber, dnum, lname, address, bdate from project, department, employee 
where dnum = dnumber and mgrssn = ssn and plocation = 'Stafford';

-- practiceQuery3 ***
select * from employee join works_on on ssn = essn
where pno = all (select pnumber from project where dnum = 5) and pno not in (select pnumber from project where dnum != 5);

-- practiceQuery4 ***
(select pno from works_on, employee where essn = ssn and lname = 'Smith') union
(select pnumber from project, department, employee where dnum = dnumber and mgrssn = ssn and lname = 'Smith');

-- practiceQuery5
select fname, lname from employee where ssn 
in (select essn from dependent group by essn having count(*) >= 2);

-- practiceQuery6
select fname, lname from employee where ssn 
not in (select essn from dependent group by essn having count(*) > 1);

-- practiceQuery7
select fname, lname from employee where ssn in (select essn from dependent) and ssn in (select mgrssn from department);

-- practiceQuery8 ***
select A.fname as A_fname, A.lname as A_lname,
B.fname as B_fname, B.lname as B_lname 
from employee as A left outer join employee as B on A.superssn = B.ssn;

-- practiceQuery9
select ssn from employee;

-- practiceQuery10
select ssn, dname from employee, department;

-- practiceQuery11
select distinct(salary) from employee;

-- practiceQuery12
select fname, lname from employee where address like '%Houston%';

-- practiceQuery13 ***
select fname, lname, salary from employee where ssn not in (select essn from works_on where pno in 
(select pnumber from project where pname = 'ProductX'))
union
select fname, lname, salary + 0.1 * salary as salary from employee where ssn in (select essn from works_on where pno in 
(select pnumber from project where pname = 'ProductX'));

-- practiceQuery14
select * from employee where dno = 5 and salary between 30000 and 40000;

-- practiceQuery15
select dname, lname, fname, pname from employee, project, department, works_on where dno = dnumber and pno = pnumber and ssn = essn
order by dname, lname, fname;

select dname, lname, fname, pname from department, employee, works_on, project
where dnumber = dno and ssn = essn and pno = pnumber
order by dname, lname, fname;

-- practiceQuery16
select fname, lname from employee, dependent 
where ssn = essn and employee.fname = dependent.dependent_name and employee.sex = dependent.sex;

-- practiceQuery17
select ssn from employee where ssn in (select essn from works_on where pno = 1 or pno = 2 or pno = 3);

-- practiceQuery18
select fname, lname from employee where superssn IS NULL;

-- practiceQuery19
select sum(salary), max(salary), min(salary), avg(salary) from employee;

-- practiceQuery20
select sum(salary), max(salary), min(salary), avg(salary) from employee where dno in
(select dnumber from department where dname = 'Research');

-- practiceQuery21
select count(*) from employee;

-- practiceQuery22
select count(*) from employee where dno in
(select dnumber from department where dname = 'Research');

-- practiceQuery23
select count(distinct salary) from employee;

-- practiceQuery24
select dno as dnumber, count(*), avg(salary) from employee group by dno;

-- practiceQuery25
select pnumber, pname, count(distinct essn) from project, works_on where pnumber = pno group by pno;

-- practiceQuery36
select fname, lname from employee where superssn = 888665555;
-- practiceQuery37
select fname, lname from employee where salary >= (10000 + (select min(salary) from employee));
-- practiceQuery40
select 'Hello World!';

-- practiceQuery41
select 'Hello World!' as greeting;

-- practiceQuery42
select 4 + 6; 

-- practiceQuery43
select 4 + 6, 3 * 7, 9 - 5;

-- practiceQuery44 
select * from employee;

-- practiceQuery50
select fname, lname, address from employee;

-- practiceQuery51
select lname as 'Last Name', fname as 'First Name', address as 'Residence Location' from employee;

-- practiceQuery52
select concat(fname, ' ', lname) as 'Whole Name', address from employee;

-- practiceQuery53
select dno from employee;

-- practiceQuery54
select distinct dno from employee;

-- practiceQuery55
select salary, dno from employee;

-- practiceQuery56
select distinct salary, dno from employee;

-- practiceQuery60 
select fname, lname, address from employee where dno = 5;

-- practiceQuery61
select fname, lname, address from employee where not dno = 5;
-- select fname, lname, address from employee where dno != 5;

-- practiceQuery62
select fname, lname, address from employee where salary > 30000;

-- practiceQuery63
select fname, lname, address from employee where salary > 30000 or dno = 5;

-- practiceQuery64
select fname, lname, address from employee where salary > 30000 and dno = 5;

-- practiceQuery65
select fname, lname, address, bdate from employee where bdate > '1968-01-01';

-- practiceQuery66
select fname, lname, address, bdate from employee where bdate > '1964-01-01' and bdate < '1970-08-10';

-- practiceQuery67
select fname, lname, address from employee order by fname asc;

-- practiceQuery68
select fname, lname, address from employee order by lname desc;

-- practiceQuery69
select fname, address from employee order by lname desc;

-- practiceQuery70
select fname, lname, address from employee order by lname, fname;

-- practiceQuery71
select fname, lname, address from employee where address like '%Houston%'; 

-- practiceQuery72
select fname, lname, address from employee where address like '%Dallas%';

-- practiceQuery73
select fname, lname, address from employee where fname like 'J%';

-- practiceQuery74
select fname, lname, address from employee where lname like '%aya%';

-- practiceQuery75 ****
select fname, lname, address from employee where lname like '%aya_%';

-- practiceQuery80
select fname, lname, salary + 0.1 * salary as raise from employee where dno = 5;

-- practiceQuery81
select sum(salary) from employee where dno = 5;

-- practiceQuery82
select min(salary), max(salary) from employee where dno = 5;

-- practiceQuery83
select count(distinct salary) from employee;

-- practiceQuery84
select count(distinct superssn) from employee;

-- practiceQuery85
select count(*) from employee where superssn = 333445555;

-- practiceQuery86
select count(*) from employee where not superssn = 333445555;

-- practiceQuery87
select count(*) from employee;

-- practiceQuery88
select dno, min(salary), avg(salary), max(salary) from employee group by dno;

-- practiceQuery89
select dno, min(salary), avg(salary), max(salary) from employee group by dno having count(*) < 4;

-- practiceQuery100
select dno, count(*) from employee where salary > 25000 group by dno;

-- practiceQuery101 ***
select dno, count(*) from employee
where dno not in (select dnumber from department where dname = "Headquarters") and salary > 25000 group by dno;

-- practiceQuery102
select dno from employee group by dno having count(*) < 4;

-- practiceQuery103 ***
select dno, count(*) from employee
where salary > 25000 and dno in (select dno from employee group by dno having count(*) < 4) 
group by dno;

-- practiceQuery104
select fname, lname, address from employee where ssn in (select essn from dependent where relationship = "Daughter");

-- practiceQuery105 ***
select fname, lname, address from employee where ssn in (select essn from works_on where pno in (select pnumber from project where plocation = "Houston"));

-- practiceQuery106
select ssn from employee where salary > 25000 or ssn in (select essn from works_on where pno = 20);

-- practiceQuery107
select ssn from employee where salary > 25000 and ssn in (select essn from works_on where pno = 20);

-- practiceQuery108
select ssn from employee where salary > 25000 and ssn not in (select essn from works_on where pno = 20);

-- practiceQuery120
select fname, lname, address, dno, dnumber, dname from employee, department;

-- practiceQuery121 *** 
select fname, lname, address, dname, dno from employee, department where dno = dnumber;

-- practiceQuery122 
select fname, lname, address dname, dno from employee inner join department on dno = dnumber;

-- practiceQuery123 ***
select fname, lname, address, dname, dno from employee natural join (select dname, dnumber as dno from department) as temp;

-- practiceQuery124 ***
select worker.fname, worker.lname, worker.address, worker.superssn, supervisor.fname, supervisor.lname
from employee as worker left outer join employee as supervisor on worker.superssn = supervisor.ssn;

-- practiceQuery125
select d.dependent_name, d.bdate, e.fname, e.lname from dependent as d right outer join employee as e on e.ssn = d.essn; 

-- practiceQuery126
select fname, lname, dname, dnumber from employee join department on mgrssn = ssn;

-- practiceQuery127
select fname, lname, dno, dname from employee left outer join department on mgrssn = ssn;

-- practiceQuery128
select fname, lname, address, pname, plocation from employee join project 
on address like concat('%', plocation, '%');
select fname, lname, address, pname, plocation from employee join project
on locate(plocation,address) > 0;

-- practiceQuery129
select worker.fname, worker.lname, worker.bdate, supervisor.fname, supervisor.lname, supervisor.bdate
from employee as worker join employee as supervisor on worker.bdate < supervisor.bdate where supervisor.ssn in (select mgrssn from department);