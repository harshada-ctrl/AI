SELECT  *,
MAX(salary) OVER()
FROM salaries
LIMIT 100


SELECT  *,
MAX(salary) OVER()
FROM salaries
WHERE salary<70000

SELECT *,
	d.dept_name,
	AVG(salary) OVER()
FROM salaries
JOIN dept_emp AS de USING (emp_no)
JOIN departments AS d USING (dept_no)


SELECT *,
	d.dept_name,
	AVG(salary) OVER(
	PARTITION BY d.dept_name
	)
FROM salaries
JOIN dept_emp AS de USING (emp_no)
JOIN departments AS d USING (dept_no)


SELECT *,
	AVG(salary) OVER(
	PARTITION BY d.dept_name
	)
FROM salaries
JOIN dept_emp AS de USING (emp_no)
JOIN departments AS d USING (dept_no)

