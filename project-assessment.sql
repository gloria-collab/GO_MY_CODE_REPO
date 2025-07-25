/*QUESTION 1 Write a query to retrieve the names of employees who are assigned to more than one project, 
including the total number of projects for each employee.*/
SELECT
    e.name AS name,
    e.num_e AS num_e,
    COUNT(p.employee_num_E) AS num_of_projects
FROM
    employee e
    LEFT JOIN employee_project p ON e.num_e = p.employee_num_E
GROUP BY
    e.name,
    e.num_e
HAVING
    COUNT(p.employee_num_E) > 1;

/*QUESTION 2 Write a query to retrieve the list of projects managed by each department, 
including the department label and manager’s name.*/
SELECT
    d.num_s AS department_label,
    p.title,
    d.manager_name,
    RANK() OVER (
        PARTITION BY
            d.num_s
        ORDER BY
            d.num_s
    ) AS list_of_projects
FROM
    department d
    LEFT JOIN project P ON d.num_s = p.department_num_s
    /*QUESTION 3 Write a query to retrieve the names of employees working on the project 
    "Website Redesign," including their roles in the project.*/
SELECT
    e.name,
    p.role
FROM
    employee e
    LEFT JOIN employee_project p ON e.num_e = p.employee_num_e
WHERE
    p.project_num_p = 201;

/*QUESTION 4 Write a query to retrieve the department with the highest number of employees, 
including the department label, manager name, and the total number of employees.*/
SELECT
    e.department_num_s AS department_label,
    d.manager_name,
    COUNT(*) AS total_num_employeee
FROM
    employee e
    LEFT JOIN department d ON e.department_num_s = d.num_s
GROUP BY
    e.department_num_s,
    d.manager_name;

/*QUESTION 5 Write a query to retrieve the names and positions of employees earning a salary greater than 60,000, 
including their department names.*/
SELECT
    e.name,
    e.position,
    e.salary,
    d.label
FROM
    employee e
    LEFT JOIN department d ON e.department_num_s = d.num_s
WHERE
    e.salary > 60000.00;

/*QUESTION 6 Write a query to retrieve the number of employees assigned to each project,
including the project title.
 */
SELECT
    p.title AS project_tite,
    COUNT(e.employee_num_e) no_of_emp
FROM
    employee_project e
    LEFT JOIN project p ON e.project_num_p = p.num_p
GROUP BY
    p.title;

/*QUESTION 7 Write a query to retrieve a summary of roles employees have across different projects, 
including the employee name, project title, and role.*/
SELECT
    e.name AS employee_name,
    p.title AS project_title,
    ep.role AS role
FROM
    employee e
    LEFT JOIN employee_project ep ON e.num_e = ep.employee_num_e
    LEFT JOIN project p ON ep.project_num_p = p.num_p;

/ QUESTION 8 * Write a query to retrieve the total salary expenditure for each department,
including the department label
and manager name.* /
SELECT
    d.label AS department_label,
    d.manager_name AS manager_name,
    SUM(e.salary) AS total_expenditure
FROM
    department d
    LEFT JOIN employee e ON d.num_s = e.department_num_s
GROUP BY
    d.label,
    d.manager_name;