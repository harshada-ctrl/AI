CREATE TABLE account(

	user_id SERIAL PRIMARY KEY,
	username VARCHAR(50) UNIQUE NOT NULL,
	password VARCHAR (50) NOT NULL,
	email VARCHAR(250)UNIQUE NOT NULL,
	created_on TIMESTAMP NOT NULL,
	last_login TIMESTAMP
)

CREATE TABLE job(
	job_id SERIAL PRIMARY KEY,
	JOB_NAME VARCHAR(200) UNIQUE NOT NULL
)

CREATE TABLE account_job (
    user_id INTEGER REFERENCES account(user_id),
    job_id INTEGER REFERENCES job(job_id),
    hire_date TIMESTAMP
);


SELECT * FROM account

INSERT INTO account(username,password,email,created_on)
VALUES
('jose','password','jose@mail.com',CURRENT_TIMESTAMP)

SELECT * FROM account

INSERT INTO job(job_name)
VALUES
('Astronaut')

SELECT * FROM job

INSERT INTO job(job_name)
VALUES
('President')

SELECT * FROM job

SELECT * FROM account_job


INSERT INTO account_job(user_id,job_id,hire_date)
VALUES
(1,1,CURRENT_TIMESTAMP)

SELECT * FROM account_job

INSERT INTO account_job(user_id,job_id,hire_date)
VALUES
(10,10,CURRENT_TIMESTAMP)---ERROR



INSERT INTO account(username,password,email,created_on)
VALUES
('ram','root','ram1@sanjivani.org.in',CURRENT_TIMESTAMP)

SELECT * FROM account


INSERT INTO account(username,password,email,created_on)
VALUES
('ram1','root','ram1@sanjivani.org.in',CURRENT_TIMESTAMP)


INSERT INTO job(job_name)
VALUES
('Data Scientist')

SELECT * FROM job

--insert 
SELECT * FROM account


UPDATE account
SET last_login = CURRENT_TIMESTAMP

SELECT * FROM account

UPDATE account
SET last_login = created_on

SELECT * FROM account


SELECT * FROM account_job

UPDATE account_job
SET hire_date = account.created_on
FROM account
WHERE account_job.user_id = account.user_id

SELECT * FROM account_job


UPDATE account
SET last_login = CURRENT_TIMESTAMP
RETURNING email,created_on,last_login


SELECT * FROM job

INSERT INTO job(job_name)
VALUES
('Cowboy')
SELECT * FROM job


DELETE FROM job
WHERE job_name = 'Cowboy'
RETURNING job_id,job_name

SELECT * FROM job

--alter

CREATE TABLE information(
	info_id SERIAL PRIMARY KEY,
	titte VARCHAR(500) NOT NULL,
	person VARCHAR(50) NOT NULL UNIQUE
)

SELECT * FROM information

ALTER TABLE information
RENAME TO new_info

SELECT * FROM information--error

SELECT * FROM new_info

ALTER TABLE new_info
RENAME COLUMN person TO people

SELECT * FROM new_info

INSERT INTO new_info (title)
VALUES ('some new title');

ALTER TABLE new_info
ALTER COLUMN people DROP NOT NULL

INSERT INTO new_info(title)
VALUES
('some new title')

SELECT * FROM new_info

ALTER TABLE new_info
DROP COLUMN people


SELECT * FROM new_info

ALTER TABLE new_info
DROP COLUMN people


ALTER TABLE new_info
DROP COLUMN IF EXISTS people

--CHECK

CREATE TABLE employees(
	emp_id SERIAL PRIMARY KEY,
	first_name VARCHAR(50) NOT NULL,
	last_name VARCHAR(50) NOT NULL,
	birthdate DATE CHECK (birthdate > '1900-01-01'),
	hire_date DATE CHECK (hire_date > birthdate),
	salary INTEGER CHECK (salary > 0)
	)

INSERT INTO employees(
first_name,
	last_name,
	birthdate,
	hire_date,
	salary
)
VALUES
('Jose' ,
'Portilla',
'1990-11-03',
'2010-01-01',
100
)

INSERT INTO employees(
first_name,
	last_name,
	birthdate,
	hire_date,
	salary
)
VALUES
('Jose' ,
'Portilla',
'1990-11-03',
'2010-01-01',
-100
)


INSERT INTO employees(
first_name,
	last_name,
	birthdate,
	hire_date,
	salary
)
VALUES
('sammy' ,
'smith',
'1990-11-03',
'2010-01-01',
-100
)



INSERT INTO employees(
first_name,
	last_name,
	birthdate,
	hire_date,
	salary
)
VALUES
('sammy' ,
'smith',
'1990-11-03',
'2010-01-01',
100
)