-- ============================================================
-- PERSONAL HOUSEHOLD EXPENSE MANAGEMENT & ANALYSIS
-- THREE-MONTH ANALYSIS
-- Months: June, July, August 2026
-- ============================================================



CREATE TABLE expense_categories (
    category_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    category_name VARCHAR(80) NOT NULL UNIQUE
);
-- Inference: The category table provides a structured master list for 
--classifying expenses.

CREATE TABLE expense_subcategories (
    subcategory_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    category_id INTEGER NOT NULL REFERENCES expense_categories(category_id),
    subcategory_name VARCHAR(80) NOT NULL UNIQUE
);
--Inference: This establishes a category–subcategory relationship and 
--helps maintain referential integrity.

CREATE TABLE family_members (
    member_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    member_name VARCHAR(80) NOT NULL UNIQUE
);
--Inference: Each expense can be associated with a specific family member.

CREATE TABLE payment_methods (
    payment_method_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    method_name VARCHAR(50) NOT NULL UNIQUE
);
--Inference: Payment information can be stored consistently and reused across 
--expense records.

CREATE TABLE vendors (
    vendor_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    vendor_name VARCHAR(120) NOT NULL UNIQUE,
    vendor_type VARCHAR(80)
);
--Inference: Vendor details can be maintained separately and referenced by 
--expenses.

CREATE TABLE expenses (
    expense_id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    expense_date DATE NOT NULL,
    subcategory_id INTEGER NOT NULL REFERENCES expense_subcategories(subcategory_id),
    member_id INTEGER NOT NULL REFERENCES family_members(member_id),
    vendor_id INTEGER REFERENCES vendors(vendor_id),
    payment_method_id INTEGER NOT NULL REFERENCES payment_methods(payment_method_id),
    amount NUMERIC(12,2) NOT NULL CHECK (amount > 0),
    quantity NUMERIC(10,2) NOT NULL DEFAULT 1 CHECK (quantity > 0),
    bill_number VARCHAR(50) UNIQUE,
    description TEXT,
    is_recurring BOOLEAN NOT NULL DEFAULT FALSE,
    due_date DATE,
    paid_status VARCHAR(20) NOT NULL DEFAULT 'Paid'
        CHECK (paid_status IN ('Paid','Pending')),
    essential BOOLEAN NOT NULL DEFAULT TRUE,
    location VARCHAR(120)
);
--Inference: The table centralizes expense transactions and uses constraints 
--to improve data validity.

INSERT INTO expense_categories (category_name) VALUES
('Food & Grocery'), ('Utilities'), ('Transportation'),
('Healthcare'), ('Education'), ('Housing');
--Inference: The database is populated with six major expense categories.

INSERT INTO expense_subcategories (category_id, subcategory_name) VALUES
(1,'Grocery'), (1,'Vegetables'), (1,'Milk'), (1,'Eating Outside'),
(2,'Electricity'), (2,'WiFi'), (2,'Mobile Recharge'),
(3,'Petrol'), (3,'Car EMI'),
(4,'Medical'),
(5,'Class Fees'),
(6,'House Maintenance');
--Inference: The expense classification becomes more detailed and organized.

INSERT INTO family_members (member_name) VALUES ('Harshada'), ('Husband');
--Inference: Expense ownership can be tracked member-wise.


INSERT INTO payment_methods (method_name) VALUES
('Cash'), ('UPI'), ('Debit Card'), ('Bank Transfer');
--Inference: Expenses can be analyzed according to how they were paid.

INSERT INTO vendors (vendor_name, vendor_type) VALUES
('Airtel','Internet/WiFi service provider'),
('Jio','Mobile service provider'),
('VI','Mobile service provider'),
('AIgenius','Class/education fee provider'),
('Sai Automobiles','Car EMI/service provider'),
('Blackstone Hotel','Restaurant/hotel'),
('D-Mart','Grocery store'),
('Medicos','Medical store'),
('Corporation','Utility service'),
('HP Petrol Pump','Fuel station'),
('Local Vegetables Vendor','Vegetable vendor'),
('Test Vendor','Temporary vendor');
--Inference: Vendor-wise expense tracking becomes possible.

INSERT INTO expenses (expense_date,subcategory_id,member_id,vendor_id,payment_method_id,amount,quantity,description,is_recurring,paid_status,essential,location) 
VALUES ('2026-08-02',1,1,7,2,800,1,'Grocery expense for April 2026',FALSE,'Paid',TRUE,'Nearby supermarket');
--Inference: The expense is recorded as a paid and essential grocery transaction.

INSERT INTO expenses (expense_date,subcategory_id,member_id,vendor_id,payment_method_id,amount,quantity,description,is_recurring,paid_status,essential,location) 
VALUES ('2026-08-10',1,1,7,1,650,1,'Grocery expense for April 2026',FALSE,'Paid',TRUE,'Nearby supermarket');

INSERT INTO expenses (expense_date,subcategory_id,member_id,vendor_id,payment_method_id,amount,quantity,description,is_recurring,paid_status,essential,location) 
VALUES ('2026-08-22',1,1,7,2,550,1,'Grocery expense for April 2026',FALSE,'Paid',TRUE,'Nearby supermarket');

INSERT INTO expenses (expense_date,subcategory_id,member_id,vendor_id,payment_method_id,amount,quantity,description,is_recurring,paid_status,essential,location) 
VALUES ('2026-08-02',2,1,NULL,1,80,1,'Vegetables expense for April 2026',FALSE,'Paid',TRUE,'Home');

INSERT INTO expenses (expense_date,subcategory_id,member_id,vendor_id,payment_method_id,amount,quantity,description,is_recurring,paid_status,essential,location) 
VALUES ('2026-08-10',2,1,NULL,2,70,1,'Vegetables expense for April 2026',FALSE,'Paid',TRUE,'Home');

INSERT INTO expenses (expense_date,subcategory_id,member_id,vendor_id,payment_method_id,amount,quantity,description,is_recurring,paid_status,essential,location) 
VALUES ('2026-08-22',2,1,NULL,1,50,1,'Vegetables expense for April 2026',FALSE,'Paid',TRUE,'Home');

INSERT INTO expenses (expense_date,subcategory_id,member_id,vendor_id,payment_method_id,amount,quantity,description,is_recurring,paid_status,essential,location) 
VALUES ('2026-08-02',3,2,NULL,1,100,1,'Milk expense for April 2026',FALSE,'Paid',TRUE,'Home');

INSERT INTO expenses (expense_date,subcategory_id,member_id,vendor_id,payment_method_id,amount,quantity,description,is_recurring,paid_status,essential,location) 
VALUES ('2026-08-10',3,2,NULL,1,100,1,'Milk expense for April 2026',FALSE,'Paid',TRUE,'Home');

INSERT INTO expenses (expense_date,subcategory_id,member_id,vendor_id,payment_method_id,amount,quantity,description,is_recurring,paid_status,essential,location) 
VALUES ('2026-08-22',3,2,NULL,2,100,1,'Milk expense for April 2026',FALSE,'Paid',TRUE,'Home');

INSERT INTO expenses (expense_date,subcategory_id,member_id,vendor_id,payment_method_id,amount,quantity,description,is_recurring,paid_status,essential,location) 
VALUES ('2026-08-05',5,2,9,2,500,1,'Electricity expense for April 2026',TRUE,'Paid',TRUE,'Utility office');

INSERT INTO expenses (expense_date,subcategory_id,member_id,vendor_id,payment_method_id,amount,quantity,description,is_recurring,paid_status,essential,location) 
VALUES ('2026-08-07',6,2,1,2,700,1,'WiFi expense for April 2026',TRUE,'Paid',TRUE,'Online');

INSERT INTO expenses (expense_date,subcategory_id,member_id,vendor_id,payment_method_id,amount,quantity,description,is_recurring,paid_status,essential,location) 
VALUES ('2026-08-08',7,1,2,2,400,1,'Mobile Recharge expense for April 2026',TRUE,'Paid',TRUE,'Online');

INSERT INTO expenses (expense_date,subcategory_id,member_id,vendor_id,payment_method_id,amount,quantity,description,is_recurring,paid_status,essential,location) 
VALUES ('2026-08-23',7,1,2,2,450,1,'Mobile Recharge expense for April 2026',TRUE,'Paid',TRUE,'Online');

INSERT INTO expenses (expense_date,subcategory_id,member_id,vendor_id,payment_method_id,amount,quantity,description,is_recurring,paid_status,essential,location) 
VALUES ('2026-08-08',8,2,10,2,300,1,'Petrol expense for April 2026',FALSE,'Paid',TRUE,'Nearby petrol pump');

INSERT INTO expenses (expense_date,subcategory_id,member_id,vendor_id,payment_method_id,amount,quantity,description,is_recurring,paid_status,essential,location)
VALUES ('2026-08-23',8,2,10,3,300,1,'Petrol expense for April 2026',FALSE,'Paid',TRUE,'Nearby petrol pump');

INSERT INTO expenses (expense_date,subcategory_id,member_id,vendor_id,payment_method_id,amount,quantity,description,is_recurring,paid_status,essential,location) 
VALUES ('2026-08-12',10,1,8,1,500,1,'Medical expense for April 2026',FALSE,'Paid',TRUE,'Local medical store');

INSERT INTO expenses (expense_date,subcategory_id,member_id,vendor_id,payment_method_id,amount,quantity,description,is_recurring,paid_status,essential,location) 
VALUES ('2026-08-10',11,1,4,4,20000,1,'Class Fees expense for April 2026',TRUE,'Paid',TRUE,'Online');

INSERT INTO expenses (expense_date,subcategory_id,member_id,vendor_id,payment_method_id,amount,quantity,description,is_recurring,paid_status,essential,location) 
VALUES ('2026-08-15',12,2,NULL,4,12000,1,'House Maintenance expense for April 2026',TRUE,'Paid',TRUE,'Home');

INSERT INTO expenses (expense_date,subcategory_id,member_id,vendor_id,payment_method_id,amount,quantity,description,is_recurring,paid_status,essential,location) 
VALUES ('2026-08-20',9,2,5,4,20000,1,'Car EMI expense for April 2026',TRUE,'Paid',TRUE,'Local service center');

INSERT INTO expenses (expense_date,subcategory_id,member_id,vendor_id,payment_method_id,amount,quantity,description,is_recurring,paid_status,essential,location) 
VALUES ('2026-08-08',4,1,6,2,600,1,'Eating Outside expense for April 2026',FALSE,'Paid',FALSE,'Local hotel');

INSERT INTO expenses (expense_date,subcategory_id,member_id,vendor_id,payment_method_id,amount,quantity,description,is_recurring,paid_status,essential,location) 
VALUES ('2026-08-23',4,1,6,1,400,1,'Eating Outside expense for April 2026',FALSE,'Paid',FALSE,'Local hotel');

INSERT INTO expenses (expense_date,subcategory_id,member_id,vendor_id,payment_method_id,amount,quantity,description,is_recurring,paid_status,essential,location) 
VALUES ('2026-07-02',1,1,7,2,800,1,'Grocery expense for May 2026',FALSE,'Paid',TRUE,'Nearby supermarket');

INSERT INTO expenses (expense_date,subcategory_id,member_id,vendor_id,payment_method_id,amount,quantity,description,is_recurring,paid_status,essential,location) 
VALUES ('2026-07-10',1,1,7,1,650,1,'Grocery expense for May 2026',FALSE,'Paid',TRUE,'Nearby supermarket');

INSERT INTO expenses (expense_date,subcategory_id,member_id,vendor_id,payment_method_id,amount,quantity,description,is_recurring,paid_status,essential,location) 
VALUES ('2026-07-22',1,1,7,2,550,1,'Grocery expense for May 2026',FALSE,'Paid',TRUE,'Nearby supermarket');

INSERT INTO expenses (expense_date,subcategory_id,member_id,vendor_id,payment_method_id,amount,quantity,description,is_recurring,paid_status,essential,location) 
VALUES ('2026-07-02',2,1,NULL,1,80,1,'Vegetables expense for May 2026',FALSE,'Paid',TRUE,'Home');

INSERT INTO expenses (expense_date,subcategory_id,member_id,vendor_id,payment_method_id,amount,quantity,description,is_recurring,paid_status,essential,location) 
VALUES ('2026-07-10',2,1,NULL,2,70,1,'Vegetables expense for May 2026',FALSE,'Paid',TRUE,'Home');

INSERT INTO expenses (expense_date,subcategory_id,member_id,vendor_id,payment_method_id,amount,quantity,description,is_recurring,paid_status,essential,location) 
VALUES ('2026-07-22',2,1,NULL,1,50,1,'Vegetables expense for May 2026',FALSE,'Paid',TRUE,'Home');

INSERT INTO expenses (expense_date,subcategory_id,member_id,vendor_id,payment_method_id,amount,quantity,description,is_recurring,paid_status,essential,location) 
VALUES ('2026-07-02',3,2,NULL,1,100,1,'Milk expense for May 2026',FALSE,'Paid',TRUE,'Home');

INSERT INTO expenses (expense_date,subcategory_id,member_id,vendor_id,payment_method_id,amount,quantity,description,is_recurring,paid_status,essential,location) 
VALUES ('2026-07-10',3,2,NULL,1,100,1,'Milk expense for May 2026',FALSE,'Paid',TRUE,'Home');

INSERT INTO expenses (expense_date,subcategory_id,member_id,vendor_id,payment_method_id,amount,quantity,description,is_recurring,paid_status,essential,location) 
VALUES ('2026-07-22',3,2,NULL,2,100,1,'Milk expense for May 2026',FALSE,'Paid',TRUE,'Home');

INSERT INTO expenses (expense_date,subcategory_id,member_id,vendor_id,payment_method_id,amount,quantity,description,is_recurring,paid_status,essential,location) 
VALUES ('2026-07-05',5,2,9,2,500,1,'Electricity expense for May 2026',TRUE,'Paid',TRUE,'Utility office');

INSERT INTO expenses (expense_date,subcategory_id,member_id,vendor_id,payment_method_id,amount,quantity,description,is_recurring,paid_status,essential,location) 
VALUES ('2026-07-07',6,2,1,2,700,1,'WiFi expense for May 2026',TRUE,'Paid',TRUE,'Online');

INSERT INTO expenses (expense_date,subcategory_id,member_id,vendor_id,payment_method_id,amount,quantity,description,is_recurring,paid_status,essential,location) 
VALUES ('2026-07-08',7,1,2,2,400,1,'Mobile Recharge expense for May 2026',TRUE,'Paid',TRUE,'Online');

INSERT INTO expenses (expense_date,subcategory_id,member_id,vendor_id,payment_method_id,amount,quantity,description,is_recurring,paid_status,essential,location) 
VALUES ('2026-07-23',7,1,2,2,450,1,'Mobile Recharge expense for May 2026',TRUE,'Paid',TRUE,'Online');

INSERT INTO expenses (expense_date,subcategory_id,member_id,vendor_id,payment_method_id,amount,quantity,description,is_recurring,paid_status,essential,location) 
VALUES ('2026-07-08',8,2,10,2,300,1,'Petrol expense for May 2026',FALSE,'Paid',TRUE,'Nearby petrol pump');

INSERT INTO expenses (expense_date,subcategory_id,member_id,vendor_id,payment_method_id,amount,quantity,description,is_recurring,paid_status,essential,location) 
VALUES ('2026-07-23',8,2,10,3,300,1,'Petrol expense for May 2026',FALSE,'Paid',TRUE,'Nearby petrol pump');

INSERT INTO expenses (expense_date,subcategory_id,member_id,vendor_id,payment_method_id,amount,quantity,description,is_recurring,paid_status,essential,location) 
VALUES ('2026-07-12',10,1,8,1,500,1,'Medical expense for May 2026',FALSE,'Paid',TRUE,'Local medical store');

INSERT INTO expenses (expense_date,subcategory_id,member_id,vendor_id,payment_method_id,amount,quantity,description,is_recurring,paid_status,essential,location)
VALUES ('2026-07-10',11,1,4,4,20000,1,'Class Fees expense for May 2026',TRUE,'Paid',TRUE,'Online');

INSERT INTO expenses (expense_date,subcategory_id,member_id,vendor_id,payment_method_id,amount,quantity,description,is_recurring,paid_status,essential,location) 
VALUES ('2026-07-15',12,2,NULL,4,12000,1,'House Maintenance expense for May 2026',TRUE,'Paid',TRUE,'Home');

INSERT INTO expenses (expense_date,subcategory_id,member_id,vendor_id,payment_method_id,amount,quantity,description,is_recurring,paid_status,essential,location) 
VALUES ('2026-07-20',9,2,5,4,20000,1,'Car EMI expense for May 2026',TRUE,'Paid',TRUE,'Local service center');

INSERT INTO expenses (expense_date,subcategory_id,member_id,vendor_id,payment_method_id,amount,quantity,description,is_recurring,paid_status,essential,location)  
VALUES ('2026-07-08',4,1,6,2,600,1,'Eating Outside expense for May 2026',FALSE,'Paid',FALSE,'Local hotel');

INSERT INTO expenses (expense_date,subcategory_id,member_id,vendor_id,payment_method_id,amount,quantity,description,is_recurring,paid_status,essential,location) 
VALUES ('2026-07-23',4,1,6,1,400,1,'Eating Outside expense for May 2026',FALSE,'Paid',FALSE,'Local hotel');

INSERT INTO expenses (expense_date,subcategory_id,member_id,vendor_id,payment_method_id,amount,quantity,description,is_recurring,paid_status,essential,location) 
VALUES ('2026-06-02',1,1,7,2,800,1,'Grocery expense for June 2026',FALSE,'Paid',TRUE,'Nearby supermarket');

INSERT INTO expenses (expense_date,subcategory_id,member_id,vendor_id,payment_method_id,amount,quantity,description,is_recurring,paid_status,essential,location) 
VALUES ('2026-06-10',1,1,7,1,650,1,'Grocery expense for June 2026',FALSE,'Paid',TRUE,'Nearby supermarket');

INSERT INTO expenses (expense_date,subcategory_id,member_id,vendor_id,payment_method_id,amount,quantity,description,is_recurring,paid_status,essential,location) 
VALUES ('2026-06-22',1,1,7,2,550,1,'Grocery expense for June 2026',FALSE,'Paid',TRUE,'Nearby supermarket');

INSERT INTO expenses (expense_date,subcategory_id,member_id,vendor_id,payment_method_id,amount,quantity,description,is_recurring,paid_status,essential,location) 
VALUES ('2026-06-02',2,1,NULL,1,80,1,'Vegetables expense for June 2026',FALSE,'Paid',TRUE,'Home');

INSERT INTO expenses (expense_date,subcategory_id,member_id,vendor_id,payment_method_id,amount,quantity,description,is_recurring,paid_status,essential,location) 
VALUES ('2026-06-10',2,1,NULL,2,70,1,'Vegetables expense for June 2026',FALSE,'Paid',TRUE,'Home');

INSERT INTO expenses (expense_date,subcategory_id,member_id,vendor_id,payment_method_id,amount,quantity,description,is_recurring,paid_status,essential,location) 
VALUES ('2026-06-22',2,1,NULL,1,50,1,'Vegetables expense for June 2026',FALSE,'Paid',TRUE,'Home');

INSERT INTO expenses (expense_date,subcategory_id,member_id,vendor_id,payment_method_id,amount,quantity,description,is_recurring,paid_status,essential,location) 
VALUES ('2026-06-02',3,2,NULL,1,100,1,'Milk expense for June 2026',FALSE,'Paid',TRUE,'Home');

INSERT INTO expenses (expense_date,subcategory_id,member_id,vendor_id,payment_method_id,amount,quantity,description,is_recurring,paid_status,essential,location)
VALUES ('2026-06-10',3,2,NULL,1,100,1,'Milk expense for June 2026',FALSE,'Paid',TRUE,'Home');

INSERT INTO expenses (expense_date,subcategory_id,member_id,vendor_id,payment_method_id,amount,quantity,description,is_recurring,paid_status,essential,location) 
VALUES ('2026-06-22',3,2,NULL,2,100,1,'Milk expense for June 2026',FALSE,'Paid',TRUE,'Home');

INSERT INTO expenses (expense_date,subcategory_id,member_id,vendor_id,payment_method_id,amount,quantity,description,is_recurring,paid_status,essential,location) 
VALUES ('2026-06-05',5,2,9,2,500,1,'Electricity expense for June 2026',TRUE,'Paid',TRUE,'Utility office');

INSERT INTO expenses (expense_date,subcategory_id,member_id,vendor_id,payment_method_id,amount,quantity,description,is_recurring,paid_status,essential,location) 
VALUES ('2026-06-07',6,2,1,2,700,1,'WiFi expense for June 2026',TRUE,'Paid',TRUE,'Online');

INSERT INTO expenses (expense_date,subcategory_id,member_id,vendor_id,payment_method_id,amount,quantity,description,is_recurring,paid_status,essential,location) 
VALUES ('2026-06-08',7,1,2,2,400,1,'Mobile Recharge expense for June 2026',TRUE,'Paid',TRUE,'Online');

INSERT INTO expenses (expense_date,subcategory_id,member_id,vendor_id,payment_method_id,amount,quantity,description,is_recurring,paid_status,essential,location) 
VALUES ('2026-06-23',7,1,2,2,450,1,'Mobile Recharge expense for June 2026',TRUE,'Paid',TRUE,'Online');

INSERT INTO expenses (expense_date,subcategory_id,member_id,vendor_id,payment_method_id,amount,quantity,description,is_recurring,paid_status,essential,location) 
VALUES ('2026-06-08',8,2,10,2,300,1,'Petrol expense for June 2026',FALSE,'Paid',TRUE,'Nearby petrol pump');

INSERT INTO expenses (expense_date,subcategory_id,member_id,vendor_id,payment_method_id,amount,quantity,description,is_recurring,paid_status,essential,location) 
VALUES ('2026-06-23',8,2,10,3,300,1,'Petrol expense for June 2026',FALSE,'Paid',TRUE,'Nearby petrol pump');

INSERT INTO expenses (expense_date,subcategory_id,member_id,vendor_id,payment_method_id,amount,quantity,description,is_recurring,paid_status,essential,location) 
VALUES ('2026-06-12',10,1,8,1,500,1,'Medical expense for June 2026',FALSE,'Paid',TRUE,'Local medical store');

INSERT INTO expenses (expense_date,subcategory_id,member_id,vendor_id,payment_method_id,amount,quantity,description,is_recurring,paid_status,essential,location) 
VALUES ('2026-06-10',11,1,4,4,20000,1,'Class Fees expense for June 2026',TRUE,'Paid',TRUE,'Online');

INSERT INTO expenses (expense_date,subcategory_id,member_id,vendor_id,payment_method_id,amount,quantity,description,is_recurring,paid_status,essential,location) 
VALUES ('2026-06-15',12,2,NULL,4,12000,1,'House Maintenance expense for June 2026',TRUE,'Paid',TRUE,'Home');

INSERT INTO expenses (expense_date,subcategory_id,member_id,vendor_id,payment_method_id,amount,quantity,description,is_recurring,paid_status,essential,location)
VALUES ('2026-06-20',9,2,5,4,20000,1,'Car EMI expense for June 2026',TRUE,'Paid',TRUE,'Local service center');

INSERT INTO expenses (expense_date,subcategory_id,member_id,vendor_id,payment_method_id,amount,quantity,description,is_recurring,paid_status,essential,location) 
VALUES ('2026-06-08',4,1,6,2,600,1,'Eating Outside expense for June 2026',FALSE,'Paid',FALSE,'Local hotel');

INSERT INTO expenses (expense_date,subcategory_id,member_id,vendor_id,payment_method_id,amount,quantity,description,is_recurring,paid_status,essential,location) 
VALUES ('2026-06-23',4,1,6,1,400,1,'Eating Outside expense for June 2026',FALSE,'Paid',FALSE,'Local hotel');

-- ============================================================
-- UPDATE examples
-- ============================================================
-- 1) Correct an amount (demonstration)
UPDATE expenses SET amount = amount + 50 WHERE expense_id = 1;
--Inference: The amount of expense_id 1 is updated without creating a new
--transaction.

-- 2) Mark a pending expense as paid
UPDATE expenses SET paid_status = 'Paid' WHERE expense_id = 2;
--Inference: A pending transaction can be updated after payment is completed.


-- 3) Correct vendor information
UPDATE vendors SET vendor_name = 'VI' WHERE vendor_name = 'VI';
--Inference: Vendor records can be corrected using an UPDATE statement.



-- 4) Correct recurring status
UPDATE expenses SET is_recurring = TRUE WHERE expense_id = 3;
--Inference: Recurring expense classification can be maintained when the 
--transaction details change.



-- ============================================================
-- DELETE examples
-- ============================================================
-- Delete a temporary vendor that has no referenced expenses:
DELETE FROM vendors WHERE vendor_name = 'Test Vendor';

-- Example duplicate deletion pattern (run only after identifying a duplicate):
-- DELETE FROM expenses
-- WHERE expense_id = <duplicate_expense_id>;

-- ============================================================
-- ALTER examples
-- ============================================================
ALTER TABLE expenses ADD COLUMN IF NOT EXISTS budget_tag VARCHAR(30);
--Inference: The expense table can store additional budgeting and 
--explanatory information.

ALTER TABLE expenses ADD COLUMN IF NOT EXISTS notes TEXT;
--Inference: The expense table can store additional budgeting 
--and explanatory information.

ALTER TABLE vendors ADD COLUMN IF NOT EXISTS contact_note VARCHAR(120);
--Inference: Vendor records can be extended with contact-related notes.


-- ============================================================
-- DROP example
-- ============================================================
CREATE TABLE IF NOT EXISTS test_expenses (
    test_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    test_description TEXT
);
--Inference: The test table provides a safe object 
--for demonstrating INSERT and DROP operations.

INSERT INTO test_expenses(test_description) VALUES ('Temporary test transaction');
--Inference: The test table provides a safe object for demonstrating
--INSERT and DROP operations.

DROP TABLE test_expenses;
--Inference: The test object is permanently deleted after the demonstration.

-- ============================================================
-- ANALYSIS QUERIES
-- ============================================================

-- ============================================================
-- 1. TOTAL HOUSEHOLD EXPENDITURE DURING THREE MONTHS
-- ============================================================

SELECT
    ROUND(SUM(amount), 2) AS total_household_expenditure
FROM expenses;

-- INFERENCE:
-- This query calculates the total amount spent by the household
-- during June, July and August.
-- The result represents the complete three-month expenditure.


-- ============================================================
-- 2. AVERAGE EXPENSE PER TRANSACTION
-- ============================================================

SELECT
    ROUND(AVG(amount), 2) AS average_expense_per_transaction
FROM expenses;

-- INFERENCE:
-- This shows the average amount spent in one transaction.
-- It helps the family understand the typical size of an expense.


-- ============================================================
-- 3. HIGHEST INDIVIDUAL EXPENSE
-- ============================================================

SELECT
    expense_id,
    expense_date,
    amount,
    description
FROM expenses
ORDER BY amount DESC
LIMIT 1;

-- INFERENCE:
-- The first record after sorting in descending order is the
-- highest individual expense.
-- This helps identify major financial commitments.


-- ============================================================
-- 4. LOWEST INDIVIDUAL EXPENSE
-- ============================================================

SELECT
    expense_id,
    expense_date,
    amount,
    description
FROM expenses
ORDER BY amount ASC
LIMIT 1;

-- INFERENCE:
-- This identifies the smallest individual expense recorded
-- in the three-month period.


-- ============================================================
-- 5. NUMBER OF EXPENSE TRANSACTIONS
-- ============================================================

SELECT
    COUNT(*) AS total_expense_transactions
FROM expenses;

-- INFERENCE:
-- This gives the total number of expense transactions recorded
-- during the three months.


-- ============================================================
-- 6. MONTH WITH HIGHEST TOTAL EXPENDITURE
-- ============================================================

SELECT
    TO_CHAR(DATE_TRUNC('month', expense_date), 'Month') AS month,
    ROUND(SUM(amount), 2) AS total_expenditure
FROM expenses
GROUP BY DATE_TRUNC('month', expense_date)
ORDER BY total_expenditure DESC
LIMIT 1;

-- INFERENCE:
-- The month returned by this query had the highest household
-- expenditure among June, July and August.


-- ============================================================
-- 7. MONTH WITH LOWEST TOTAL EXPENDITURE
-- ============================================================

SELECT
    TO_CHAR(DATE_TRUNC('month', expense_date), 'Month') AS month,
    ROUND(SUM(amount), 2) AS total_expenditure
FROM expenses
GROUP BY DATE_TRUNC('month', expense_date)
ORDER BY total_expenditure ASC
LIMIT 1;

-- INFERENCE:
-- The month returned here had the lowest total expenditure.


-- ============================================================
-- 8. INCREASE OR DECREASE FROM FIRST MONTH TO THIRD MONTH
-- ============================================================

WITH monthly AS (
    SELECT
        DATE_TRUNC('month', expense_date) AS month,
        SUM(amount) AS total
    FROM expenses
    GROUP BY DATE_TRUNC('month', expense_date)
),
comparison AS (
    SELECT
        MAX(CASE WHEN month =
            (SELECT MIN(month) FROM monthly)
            THEN total END) AS first_month_total,

        MAX(CASE WHEN month =
            (SELECT MAX(month) FROM monthly)
            THEN total END) AS third_month_total
    FROM monthly
)
SELECT
    ROUND(first_month_total, 2) AS first_month_expenditure,
    ROUND(third_month_total, 2) AS third_month_expenditure,
    ROUND(third_month_total - first_month_total, 2) AS difference,
    CASE
        WHEN third_month_total > first_month_total
            THEN 'INCREASED'
        WHEN third_month_total < first_month_total
            THEN 'DECREASED'
        ELSE 'NO CHANGE'
    END AS expenditure_trend
FROM comparison;

-- INFERENCE:
-- If the result is INCREASED, household spending increased
-- from the first month to the third month.
-- If DECREASED, spending reduced.
-- If NO CHANGE, spending remained the same.


-- ============================================================
-- 9. MONTH WITH HIGHEST NUMBER OF TRANSACTIONS
-- ============================================================

SELECT
    TO_CHAR(DATE_TRUNC('month', expense_date), 'Month') AS month,
    COUNT(*) AS number_of_transactions
FROM expenses
GROUP BY DATE_TRUNC('month', expense_date)
ORDER BY number_of_transactions DESC
LIMIT 1;

-- INFERENCE:
-- This identifies the month in which the household made
-- the highest number of expense transactions.


-- ============================================================
-- 10. SIGNIFICANT CHANGE IN SPENDING BETWEEN THREE MONTHS
-- ============================================================

WITH monthly AS (
    SELECT
        DATE_TRUNC('month', expense_date) AS month,
        SUM(amount) AS total
    FROM expenses
    GROUP BY DATE_TRUNC('month', expense_date)
)
SELECT
    TO_CHAR(month, 'Month') AS month,
    ROUND(total, 2) AS total_expenditure,
    ROUND(
        total - LAG(total) OVER (ORDER BY month),
        2
    ) AS change_from_previous_month,
    ROUND(
        ((total - LAG(total) OVER (ORDER BY month))
        / NULLIF(LAG(total) OVER (ORDER BY month), 0)) * 100,
        2
    ) AS percentage_change
FROM monthly
ORDER BY month;

-- INFERENCE:
-- This compares each month with the previous month.
-- A positive percentage means spending increased.
-- A negative percentage means spending decreased.
-- A large percentage change indicates a significant change.


-- ============================================================
-- 11. MAJOR TYPES OF EXPENSES
-- ============================================================

SELECT
    c.category_name,
    ROUND(SUM(e.amount), 2) AS total_amount,
    COUNT(*) AS number_of_transactions
FROM expenses e
JOIN expense_subcategories s
    ON e.subcategory_id = s.subcategory_id
JOIN expense_categories c
    ON s.category_id = c.category_id
GROUP BY c.category_name
ORDER BY total_amount DESC;

-- INFERENCE:
-- This lists all major household expense categories.
-- Categories with larger total amounts represent major
-- spending areas.


-- ============================================================
-- 12. EXPENSE TYPE CONSUMING LARGEST AMOUNT
-- ============================================================

SELECT
    c.category_name,
    ROUND(SUM(e.amount), 2) AS total_amount
FROM expenses e
JOIN expense_subcategories s
    ON e.subcategory_id = s.subcategory_id
JOIN expense_categories c
    ON s.category_id = c.category_id
GROUP BY c.category_name
ORDER BY total_amount DESC
LIMIT 1;

-- INFERENCE:
-- The category returned by this query consumed the largest
-- amount of household money during the three months.


-- ============================================================
-- 13. EXPENSE TYPE OCCURRING MOST FREQUENTLY
-- ============================================================

SELECT
    c.category_name,
    COUNT(*) AS frequency
FROM expenses e
JOIN expense_subcategories s
    ON e.subcategory_id = s.subcategory_id
JOIN expense_categories c
    ON s.category_id = c.category_id
GROUP BY c.category_name
ORDER BY frequency DESC
LIMIT 1;

-- INFERENCE:
-- This identifies the category with the highest number
-- of transactions.


-- ============================================================
-- 14. TOP THREE SPENDING AREAS
-- ============================================================

SELECT
    c.category_name,
    ROUND(SUM(e.amount), 2) AS total_amount
FROM expenses e
JOIN expense_subcategories s
    ON e.subcategory_id = s.subcategory_id
JOIN expense_categories c
    ON s.category_id = c.category_id
GROUP BY c.category_name
ORDER BY total_amount DESC
LIMIT 3;

-- INFERENCE:
-- These are the top three areas where the household spends
-- the most money.


-- ============================================================
-- 15. FREQUENT BUT RELATIVELY SMALL EXPENSES
-- ============================================================

SELECT
    s.subcategory_name,
    COUNT(*) AS number_of_transactions,
    ROUND(AVG(e.amount), 2) AS average_amount,
    ROUND(SUM(e.amount), 2) AS total_amount
FROM expenses e
JOIN expense_subcategories s
    ON e.subcategory_id = s.subcategory_id
GROUP BY s.subcategory_name
HAVING COUNT(*) >= 3
   AND AVG(e.amount) <= 1000
ORDER BY number_of_transactions DESC;

-- INFERENCE:
-- These expenses happen frequently but each transaction is
-- relatively small.
-- Examples may include milk, vegetables and petrol.
-- Such expenses should be monitored because small amounts
-- can accumulate over time.


-- ============================================================
-- 16. IDENTIFY RECURRING EXPENSES
-- ============================================================

SELECT
    s.subcategory_name,
    COUNT(*) AS occurrences,
    ROUND(SUM(e.amount), 2) AS total_recurring_amount
FROM expenses e
JOIN expense_subcategories s
    ON e.subcategory_id = s.subcategory_id
WHERE e.is_recurring = TRUE
GROUP BY s.subcategory_name
ORDER BY total_recurring_amount DESC;

-- INFERENCE:
-- This identifies expenses marked as recurring.
-- These expenses are important for monthly budgeting.


-- ============================================================
-- 17. TOTAL MONEY SPENT ON RECURRING EXPENSES
-- ============================================================

SELECT
    ROUND(SUM(amount), 2) AS total_recurring_expenses
FROM expenses
WHERE is_recurring = TRUE;

-- INFERENCE:
-- This gives the total amount spent on recurring expenses
-- during the three-month period.


-- ============================================================
-- 18. WHICH RECURRING EXPENSES SHOULD BE REVIEWED?
-- ============================================================

SELECT
    s.subcategory_name,
    COUNT(*) AS occurrences,
    ROUND(SUM(e.amount), 2) AS total_amount
FROM expenses e
JOIN expense_subcategories s
    ON e.subcategory_id = s.subcategory_id
WHERE e.is_recurring = TRUE
GROUP BY s.subcategory_name
HAVING SUM(e.amount) >= 1000
ORDER BY total_amount DESC;

-- INFERENCE:
-- Recurring expenses with high cumulative amounts should
-- be reviewed carefully.
-- The family should check whether each recurring expense
-- is necessary and properly budgeted.


-- ============================================================
-- 19. HIGH-VALUE RECURRING EXPENSES
-- ============================================================

SELECT
    e.expense_date,
    s.subcategory_name,
    e.amount,
    e.description
FROM expenses e
JOIN expense_subcategories s
    ON e.subcategory_id = s.subcategory_id
WHERE e.is_recurring = TRUE
  AND e.amount >= 10000
ORDER BY e.amount DESC;

-- INFERENCE:
-- This identifies recurring transactions of ₹10,000 or more.
-- These are major financial commitments and require proper
-- monthly planning.


-- ============================================================
-- 20. MOST FREQUENTLY USED PAYMENT METHOD
-- ============================================================

SELECT
    p.method_name,
    COUNT(*) AS number_of_transactions
FROM expenses e
JOIN payment_methods p
    ON e.payment_method_id = p.payment_method_id
GROUP BY p.method_name
ORDER BY number_of_transactions DESC
LIMIT 1;

-- INFERENCE:
-- The payment method returned here is used for the largest
-- number of household transactions.


-- ============================================================
-- 21. PAYMENT METHOD ACCOUNTING FOR LARGEST AMOUNT
-- ============================================================

SELECT
    p.method_name,
    ROUND(SUM(e.amount), 2) AS total_amount
FROM expenses e
JOIN payment_methods p
    ON e.payment_method_id = p.payment_method_id
GROUP BY p.method_name
ORDER BY total_amount DESC
LIMIT 1;

-- INFERENCE:
-- This identifies the payment method through which the
-- largest amount of money was spent.


-- ============================================================
-- 22. TOTAL SPENT THROUGH CASH
-- ============================================================

SELECT
    ROUND(SUM(e.amount), 2) AS cash_expenditure
FROM expenses e
JOIN payment_methods p
    ON e.payment_method_id = p.payment_method_id
WHERE LOWER(p.method_name) = 'cash';

-- INFERENCE:
-- This gives the total household expenditure made using cash.


-- ============================================================
-- 23. TOTAL SPENT THROUGH DIGITAL PAYMENT METHODS
-- ============================================================

SELECT
    ROUND(SUM(e.amount), 2) AS digital_payment_expenditure
FROM expenses e
JOIN payment_methods p
    ON e.payment_method_id = p.payment_method_id
WHERE LOWER(p.method_name) IN ('upi', 'online', 'card', 'net banking');

-- INFERENCE:
-- This calculates expenditure made using digital payment
-- methods such as UPI, card or online payment.


-- ============================================================
-- 24. HIGH-VALUE DIGITAL PAYMENT TRANSACTIONS
-- ============================================================

SELECT
    e.expense_id,
    e.expense_date,
    s.subcategory_name,
    e.amount,
    p.method_name,
    v.vendor_name
FROM expenses e
JOIN expense_subcategories s
    ON e.subcategory_id = s.subcategory_id
JOIN payment_methods p
    ON e.payment_method_id = p.payment_method_id
LEFT JOIN vendors v
    ON e.vendor_id = v.vendor_id
WHERE LOWER(p.method_name) IN ('upi', 'online', 'card', 'net banking')
  AND e.amount >= 10000
ORDER BY e.amount DESC;

-- INFERENCE:
-- This identifies large-value expenses made digitally.
-- Such transactions should be monitored because they have
-- a significant impact on household expenditure.


-- ============================================================
-- 25. EXPENSES ABOVE A SIGNIFICANT THRESHOLD
-- ============================================================
-- Threshold selected for this household: ₹10,000

SELECT
    e.expense_id,
    e.expense_date,
    s.subcategory_name,
    e.amount,
    v.vendor_name,
    e.description
FROM expenses e
JOIN expense_subcategories s
    ON e.subcategory_id = s.subcategory_id
LEFT JOIN vendors v
    ON e.vendor_id = v.vendor_id
WHERE e.amount >= 10000
ORDER BY e.amount DESC;

-- INFERENCE:
-- ₹10,000 is considered a significant threshold for this
-- household.
-- Transactions equal to or above this amount require
-- special attention in budgeting.


-- ============================================================
-- 26. UNUSUALLY HIGH EXPENSES
-- ============================================================
-- Using statistical method:
-- Expense > Average + 2 × Standard Deviation

SELECT
    e.expense_id,
    e.expense_date,
    s.subcategory_name,
    e.amount,
    e.description
FROM expenses e
JOIN expense_subcategories s
    ON e.subcategory_id = s.subcategory_id
WHERE e.amount >
      (
          SELECT AVG(amount)
                 + 2 * STDDEV_POP(amount)
          FROM expenses
      )
ORDER BY e.amount DESC;

-- INFERENCE:
-- This uses a statistical rule to identify unusually high
-- expenses compared with the overall transaction pattern.
-- Such transactions may need further investigation.


-- ============================================================
-- 27. EXPENSES OCCURRING ONLY ONCE WITH SIGNIFICANT IMPACT
-- ============================================================

SELECT
    s.subcategory_name,
    COUNT(*) AS occurrence,
    ROUND(SUM(e.amount), 2) AS total_amount,
    MIN(e.expense_date) AS expense_date
FROM expenses e
JOIN expense_subcategories s
    ON e.subcategory_id = s.subcategory_id
GROUP BY s.subcategory_name
HAVING COUNT(*) = 1
   AND SUM(e.amount) >= 10000
ORDER BY total_amount DESC;

-- INFERENCE:
-- This identifies expense types that occurred only once
-- but had a large financial impact.
-- Such expenses are important for understanding unusual
-- or occasional spending.


-- ============================================================
-- 28. INVESTIGATE THREE SIGNIFICANT / HIGH-VALUE EXPENSES
-- ============================================================

SELECT
    e.expense_id,
    e.expense_date,
    s.subcategory_name,
    e.amount,
    v.vendor_name,
    p.method_name,
    e.is_recurring,
    e.essential,
    e.description
FROM expenses e
JOIN expense_subcategories s
    ON e.subcategory_id = s.subcategory_id
LEFT JOIN vendors v
    ON e.vendor_id = v.vendor_id
JOIN payment_methods p
    ON e.payment_method_id = p.payment_method_id
WHERE e.amount >= 10000
ORDER BY e.amount DESC
LIMIT 3;

-- INFERENCE:
-- The top three high-value transactions can be investigated
-- using their category, vendor, payment method, recurring
-- status and description.
--
-- In this household dataset, likely major expenses are:
-- 1. Class Fees       → ₹20,000
-- 2. Car EMI          → ₹20,000
-- 3. House Maintenance → ₹12,000
--
-- Class Fees:
-- This is an education-related expense and is a planned
-- high-value commitment.
--
-- Car EMI:
-- This is a recurring transportation/financial commitment
-- and should be included in the monthly budget.
--
-- House Maintenance:
-- This is a high-value housing expense and should be planned
-- separately because it has a large effect on monthly cash flow.