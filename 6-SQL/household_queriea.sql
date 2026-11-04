
/*Part A — Basic Expense Analysis
1. Household Expense Overview
The family wants to see its complete expense history.
Display:
•	Expense ID
•	Expense Date
•	Amount
•	Description
•	Payment Status*/


SELECT
    expense_id,
    expense_date,
    amount,
    description,
    paid_status
FROM expenses
ORDER BY expense_id;


/*2. High-Value Expenses
The family wants to identify expenses that require special attention.
Find all expenses where the amount is greater than ₹2,000.*/


SELECT *
FROM expenses
WHERE amount > 2000;

/*3. Small Daily Expenses
The family suspects that many small expenses are gradually increasing its overall spending.
Find all expenses where the amount is less than ₹500.
*/

SELECT *
FROM expenses
WHERE amount < 500;


/*4. Expense Range
The family wants to review expenses between ₹1,000 and ₹5,000.
Find all such expenses using comparison operators.
*/

SELECT *
FROM expenses
WHERE amount >= 1000
  AND amount <= 5000;


/*5. Exceptional Expenses
The family wants to identify unusually large transactions.
Find all expenses where the amount is ₹10,000 or more.
*/

SELECT *
FROM expenses
WHERE amount >= 10000;


/*Part B — Understanding Payment Behaviour
6. Payment Methods Used
The family uses different methods to pay its expenses.
Find the different payment methods used in the expense records.
*/


SELECT DISTINCT pm.payment_method_name
FROM expenses e
JOIN payment_methods pm
ON e.payment_method_id = pm.payment_method_id;


/*7. UPI Spending
The family wants to know which transactions were paid using UPI.
Display all UPI transactions.
*/

SELECT
    e.expense_id,
    e.expense_date,
    e.amount,
    e.description
FROM expenses e
JOIN payment_methods pm
ON e.payment_method_id = pm.payment_method_id
WHERE pm.payment_method_name = 'UPI';



/*8. Cash Spending
Find all expenses paid using Cash.
*/
SELECT
    e.expense_id,
    e.expense_date,
    e.amount,
    e.description
FROM expenses e
JOIN payment_methods pm
ON e.payment_method_id = pm.payment_method_id
WHERE pm.payment_method_name = 'Cash';

/*9. Large UPI Transactions
The family wants to review high-value digital payments.
Find expenses where:
•	amount is greater than ₹2,000
•	AND payment method is UPI.
*/

SELECT e.*
FROM expenses e
JOIN payment_methods pm
ON e.payment_method_id = pm.payment_method_id
WHERE e.amount > 2000
  AND pm.payment_method_name = 'UPI';

/*10. Cash or UPI
Find expenses greater than ₹2,000 where the payment method was either Cash or UPI.
Use OR appropriately.
*/


SELECT e.*
FROM expenses e
JOIN payment_methods pm
ON e.payment_method_id = pm.payment_method_id
WHERE e.amount > 2000
  AND (
      pm.payment_method_name = 'Cash'
      OR pm.payment_method_name = 'UPI'
  );

/*11. Non-UPI Expenses
The family wants to identify transactions that were not paid through UPI.
Display those expenses.
*/


SELECT e.*
FROM expenses e
JOIN payment_methods pm
ON e.payment_method_id = pm.payment_method_id
WHERE pm.payment_method_name <> 'UPI';


/*Part C — Recurring and Pending Expenses
12. Regular Household Commitments
The family wants to identify expenses that occur regularly.
Find all recurring expenses.
*/


SELECT *
FROM expenses
WHERE is_recurring = TRUE;

/*13. Cost of Recurring Expenses
Calculate the total amount committed to recurring expenses.
*/

SELECT SUM(amount) AS total_recurring_expenses
FROM expenses
WHERE is_recurring = TRUE;


/*14. Expensive Recurring Commitments
The family wants to review recurring commitments costing more than ₹1,000.
Find all recurring expenses where:
amount > ₹1,000
*/

SELECT *
FROM expenses
WHERE is_recurring = TRUE
  AND amount > 1000;

/*15. Pending Payments
The family wants to identify payments that still require attention.
Find all expenses whose payment status is:
PENDING or PARTIAL
*/


SELECT *
FROM expenses
WHERE paid_status IN ('PENDING', 'PARTIAL');


/*16. Recurring Pending Expenses
Identify expenses that are:
•	recurring
•	AND pending
These are important because they represent regular financial commitments that have not yet been settled.
*/

SELECT *
FROM expenses
WHERE is_recurring = TRUE
  AND paid_status = 'PENDING';

/*Part D — Household Spending Patterns
17. Number of Transactions
How many individual expense transactions have been recorded by the family?
*/

SELECT COUNT(*) AS total_transactions
FROM expenses;


/*18. Total Household Spending
Calculate the total amount spent across all recorded expenses.
*/

SELECT SUM(amount) AS total_household_spending
FROM expenses;

/*19. Average Expense
Calculate the average amount spent per transaction.
*/

SELECT ROUND(AVG(amount), 2) AS average_expense
FROM expenses;

/*20. Highest and Lowest Expenses
Find:
•	highest expense
•	lowest expense
The family wants to understand the range of its spending.
*/

SELECT
    MAX(amount) AS highest_expense,
    MIN(amount) AS lowest_expense
FROM expenses;

/*21. Different Expense Types
Find the number of different subcategories in which the family has recorded expenses.
Use DISTINCT.
*/

SELECT COUNT(DISTINCT subcategory_id) AS different_expense_types
FROM expenses;

/*22. Expenses of a Particular Family Member
The family wants to review expenses associated with member_id = 1.
Find:
•	number of transactions
•	total amount spent
•	average expense amount
for this family member.
*/


SELECT
    COUNT(*) AS number_of_transactions,
    SUM(amount) AS total_amount,
    ROUND(AVG(amount), 2) AS average_amount
FROM expenses
WHERE member_id = 1;


/*Part E — Searching Information Using LIKE
23. Vendor Search
The family remembers that it made a payment to a vendor whose name contains the word:
"Hospital"
Find that vendor using pattern matching.
*/


SELECT *
FROM vendors
WHERE vendor_name LIKE '%Hospital%';


SELECT *
FROM vendors
WHERE vendor_name ILIKE '%hospital%';

/*24. Store Search
Find vendors whose name contains:
"Store"
*/

SELECT *
FROM vendors
WHERE vendor_name LIKE '%Store%';

/*25. Monthly Expenses
The family wants to identify expenses whose description contains the word:
"Monthly"
Use LIKE.
*/


SELECT *
FROM expenses
WHERE description LIKE '%Monthly%';


/*26. Bill-Related Subcategories
Find subcategories whose names contain the word:
"Bill"
*/


SELECT *
FROM expense_subcategories
WHERE subcategory_name LIKE '%Bill%';

/*27. Starting Letter Search
Find vendors whose names start with the letter "A".
*/

SELECT *
FROM vendors
WHERE vendor_name LIKE 'A%';

/*Part F — Logical Conditions and Operator Precedence
28. High-Priority Expenses
The family wants to identify expenses satisfying either of these conditions:
•	amount is greater than ₹5,000
OR
•	amount is greater than ₹2,000 AND payment was made through UPI.
Write the query and carefully consider operator precedence.
*/


SELECT e.*
FROM expenses e
JOIN payment_methods pm
ON e.payment_method_id = pm.payment_method_id
WHERE e.amount > 5000
   OR (
       e.amount > 2000
       AND pm.payment_method_name = 'UPI'
   );

/*29. Expenses Requiring Review
Find expenses that are:
•	recurring
•	AND amount greater than ₹2,000
•	AND payment status is PAID
*/


SELECT *
FROM expenses
WHERE is_recurring = TRUE
  AND amount > 2000
  AND paid_status = 'PAID';


/*30. Unusual Spending
Find expenses where:
•	amount is less than ₹500
OR
•	amount is greater than ₹5,000
but exclude expenses that are PENDING.
Use AND, OR, NOT and appropriate parentheses.
*/


SELECT *
FROM expenses
WHERE
    (
        amount < 500
        OR amount > 5000
    )
    AND NOT paid_status = 'PENDING';





-- FINAL REAL-LIFE ANALYSIS

-- 1.	What is the total household expenditure?
   57,349

-- 2.	What is the average expense?
    3,823.27 per transaction

-- 3. What is the highest individual expense?
     25,000 — College Fees
	 
-- 4. How many expenses are recurring?
    6 recurring expenses
	
-- 5. How much money is committed to recurring expenses?
   40,949

-- 6. Which payment methods are being used?
Cash
UPI
Debit Card
Net Banking

-- 7. How much spending is done through UPI?
   16,600

-- 8. How many expenses are pending or partially paid?
      0

	  
-- 9. How many expenses are above ₹2,000?
    7 expenses

-- 10. Three expenses the family should review carefully
         1. College Fees — ₹25,000
		 2. Property Tax — ₹8,500
		 3. Electricity Bill — ₹3,250