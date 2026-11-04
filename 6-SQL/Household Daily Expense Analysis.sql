--STEP 1 : EXPENSE CATEGORY TABLE

CREATE TABLE expense_categories
(
    category_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    category_name VARCHAR(50) NOT NULL UNIQUE,
    description VARCHAR(200)
);


-- STEP 2 : EXPENSE SUBCATEGORY TABLE

CREATE TABLE expense_subcategories
(
    subcategory_id      INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    category_id         INTEGER NOT NULL,
    subcategory_name    VARCHAR(60) NOT NULL,
    description         VARCHAR(200),

    CONSTRAINT fk_subcategory_category
        FOREIGN KEY (category_id)
        REFERENCES expense_categories(category_id),

    CONSTRAINT uq_category_subcategory
        UNIQUE (category_id, subcategory_name)
);


-- STEP 3 : FAMILY MEMBER TABLE

CREATE TABLE family_members
(
    member_id       INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    member_name     VARCHAR(60) NOT NULL,
    relationship    VARCHAR(30),
    date_of_birth   DATE
);

-- STEP 4 : PAYMENT METHOD TABLE

CREATE TABLE payment_methods
(
    payment_method_id
        INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    payment_method_name
        VARCHAR(40) NOT NULL UNIQUE
);

-- STEP 5 : VENDOR / SERVICE PROVIDER TABLE

CREATE TABLE vendors
(
    vendor_id       INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    vendor_name     VARCHAR(100) NOT NULL,
    vendor_type     VARCHAR(50),
    city            VARCHAR(50),
    contact_number  VARCHAR(15)
);

-- STEP 6 : MAIN EXPENSE TRANSACTION TABLE

CREATE TABLE expenses
(
    expense_id          BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,

    expense_date        DATE NOT NULL,

    subcategory_id      INTEGER NOT NULL,

    member_id           INTEGER,

    vendor_id           INTEGER,

    payment_method_id   INTEGER,

    amount              NUMERIC(12,2) NOT NULL,

    quantity            NUMERIC(10,2),

    bill_number         VARCHAR(50),

    description         VARCHAR(255),

    is_recurring        BOOLEAN DEFAULT FALSE,

    due_date            DATE,

    paid_status         VARCHAR(10) DEFAULT 'PAID',

    created_at          TIMESTAMP DEFAULT CURRENT_TIMESTAMP,


    -- Amount must always be positive
    CONSTRAINT chk_expense_amount
        CHECK (amount > 0),


    -- Valid payment status
    CONSTRAINT chk_paid_status
        CHECK (paid_status IN ('PAID', 'PENDING', 'PARTIAL')),


    -- Foreign Key: Expense → Subcategory
    CONSTRAINT fk_expense_subcategory
        FOREIGN KEY (subcategory_id)
        REFERENCES expense_subcategories(subcategory_id),


    -- Foreign Key: Expense → Family Member
    CONSTRAINT fk_expense_member
        FOREIGN KEY (member_id)
        REFERENCES family_members(member_id),


    -- Foreign Key: Expense → Vendor
    CONSTRAINT fk_expense_vendor
        FOREIGN KEY (vendor_id)
        REFERENCES vendors(vendor_id),


    -- Foreign Key: Expense → Payment Method
    CONSTRAINT fk_expense_payment
        FOREIGN KEY (payment_method_id)
        REFERENCES payment_methods(payment_method_id)
);

-- STEP 7 : INSERT EXPENSE CATEGORIES

INSERT INTO expense_categories
(category_name, description)
VALUES
('Grocery',
 'Daily household grocery and food items'),

('Utilities',
 'Electricity, water, gas, mobile and internet'),

('Housing',
 'Building maintenance, repair and home expenses'),

('Taxes',
 'Property tax and other government taxes'),

('Medical',
 'Hospital, doctor, medicine and healthcare'),

('Food Outside',
 'Restaurant, hotel and online food'),

('Transportation',
 'Petrol, diesel, bus, auto, taxi and vehicle expenses'),

('Tourism',
 'Travel, vacation and sightseeing expenses'),

('Education',
 'School, college, books and educational expenses'),

('Clothing',
 'Clothes, footwear and accessories'),

('Domestic Services',
 'Maid, cleaning and household services'),

('Insurance',
 'Life, health and vehicle insurance'),

('Loan and EMI',
 'Loan installments and EMI payments'),

('Entertainment',
 'Movies, games and entertainment'),

('Personal Care',
 'Salon, cosmetics and personal care'),

('Social',
 'Functions, gifts and social activities'),

('Miscellaneous',
 'Other household expenses');

 -- STEP 8 : INSERT EXPENSE SUBCATEGORIES

 -- ---------------- GROCERY ----------------

INSERT INTO expense_subcategories
(category_id, subcategory_name, description)
VALUES
(1, 'Kirana', 'Rice, wheat, pulses, oil, spices etc.'),
(1, 'Vegetables', 'Daily vegetables'),
(1, 'Fruits', 'Fresh fruits'),
(1, 'Milk', 'Milk and dairy products'),
(1, 'Bakery', 'Bread, biscuits and bakery items'),
(1, 'Meat / Fish', 'Non-vegetarian food items');


-- ---------------- UTILITIES ----------------

INSERT INTO expense_subcategories
(category_id, subcategory_name)
VALUES
(2, 'Electricity Bill'),
(2, 'Water Bill'),
(2, 'Gas Cylinder'),
(2, 'Mobile Recharge'),
(2, 'Internet Bill'),
(2, 'DTH / Cable');


-- ---------------- HOUSING ----------------

INSERT INTO expense_subcategories
(category_id, subcategory_name)
VALUES
(3, 'Building Maintenance'),
(3, 'House Repair'),
(3, 'Plumbing'),
(3, 'Electrical Repair'),
(3, 'Furniture'),
(3, 'Painting');


-- ---------------- TAXES ----------------

INSERT INTO expense_subcategories
(category_id, subcategory_name)
VALUES
(4, 'Property Tax'),
(4, 'Municipal Tax'),
(4, 'Vehicle Tax'),
(4, 'Other Government Tax');


-- ---------------- MEDICAL ----------------

INSERT INTO expense_subcategories
(category_id, subcategory_name)
VALUES
(5, 'Doctor Consultation'),
(5, 'Hospital'),
(5, 'Medicines'),
(5, 'Medical Tests'),
(5, 'Dental'),
(5, 'Emergency Medical');


-- ---------------- FOOD OUTSIDE ----------------

INSERT INTO expense_subcategories
(category_id, subcategory_name)
VALUES
(6, 'Restaurant'),
(6, 'Hotel'),
(6, 'Online Food'),
(6, 'Tea / Snacks');


-- ---------------- TRANSPORTATION ----------------

INSERT INTO expense_subcategories
(category_id, subcategory_name)
VALUES
(7, 'Petrol'),
(7, 'Diesel'),
(7, 'Bus'),
(7, 'Auto'),
(7, 'Taxi'),
(7, 'Parking'),
(7, 'Vehicle Maintenance');


-- ---------------- TOURISM ----------------

INSERT INTO expense_subcategories
(category_id, subcategory_name)
VALUES
(8, 'Hotel Stay'),
(8, 'Train Ticket'),
(8, 'Flight Ticket'),
(8, 'Tour Package'),
(8, 'Sightseeing');


-- ---------------- EDUCATION ----------------

INSERT INTO expense_subcategories
(category_id, subcategory_name)
VALUES
(9, 'School Fees'),
(9, 'College Fees'),
(9, 'Books'),
(9, 'Stationery'),
(9, 'Tuition / Coaching'),
(9, 'Online Course');


-- ---------------- CLOTHING ----------------

INSERT INTO expense_subcategories
(category_id, subcategory_name)
VALUES
(10, 'Clothes'),
(10, 'Footwear'),
(10, 'Accessories');


-- ---------------- DOMESTIC SERVICES ----------------

INSERT INTO expense_subcategories
(category_id, subcategory_name)
VALUES
(11, 'Maid'),
(11, 'Cleaning'),
(11, 'Laundry'),
(11, 'Gardening');


-- ---------------- INSURANCE ----------------

INSERT INTO expense_subcategories
(category_id, subcategory_name)
VALUES
(12, 'Life Insurance'),
(12, 'Health Insurance'),
(12, 'Vehicle Insurance'),
(12, 'Home Insurance');


-- ---------------- LOAN AND EMI ----------------

INSERT INTO expense_subcategories
(category_id, subcategory_name)
VALUES
(13, 'Home Loan EMI'),
(13, 'Vehicle Loan EMI'),
(13, 'Personal Loan EMI'),
(13, 'Education Loan EMI');


-- ---------------- ENTERTAINMENT ----------------

INSERT INTO expense_subcategories
(category_id, subcategory_name)
VALUES
(14, 'Movie'),
(14, 'OTT Subscription'),
(14, 'Games'),
(14, 'Events');


-- ---------------- PERSONAL CARE ----------------

INSERT INTO expense_subcategories
(category_id, subcategory_name)
VALUES
(15, 'Salon'),
(15, 'Cosmetics'),
(15, 'Personal Care Products');


-- ---------------- SOCIAL ----------------

INSERT INTO expense_subcategories
(category_id, subcategory_name)
VALUES
(16, 'Gifts'),
(16, 'Marriage Function'),
(16, 'Festival'),
(16, 'Donation');


-- ---------------- MISCELLANEOUS ----------------

INSERT INTO expense_subcategories
(category_id, subcategory_name)
VALUES
(17, 'Miscellaneous'),
(17, 'Other');


-- STEP 9 : INSERT FAMILY MEMBERS

INSERT INTO family_members
(member_name, relationship, date_of_birth)
VALUES
('Rajesh', 'Father', '1975-05-15'),
('Sunita', 'Mother', '1978-09-20'),
('Amit', 'Son', '2005-03-12'),
('Priya', 'Daughter', '2008-07-25');


-- STEP 10 : INSERT PAYMENT METHODS

INSERT INTO payment_methods
(payment_method_name)
VALUES
('Cash'),
('UPI'),
('Debit Card'),
('Credit Card'),
('Net Banking'),
('Cheque'),
('Auto Debit');


-- STEP 11 : INSERT VENDORS

INSERT INTO vendors
(vendor_name, vendor_type, city, contact_number)
VALUES
('Local Kirana Store', 'Grocery', 'Aurangabad', '9000000001'),

('D-Mart', 'Supermarket', 'Aurangabad', '9000000002'),

('MSEDCL', 'Electricity', 'Aurangabad', '9000000003'),

('Municipal Corporation', 'Government', 'Aurangabad', '9000000004'),

('City Hospital', 'Hospital', 'Aurangabad', '9000000005'),

('Apollo Pharmacy', 'Pharmacy', 'Aurangabad', '9000000006'),

('Indian Oil', 'Petrol Pump', 'Aurangabad', '9000000007'),

('ABC Restaurant', 'Restaurant', 'Aurangabad', '9000000008'),

('IRCTC', 'Railway', 'India', '9000000009'),

('Reliance Jio', 'Telecom', 'India', '9000000010');

-- STEP 12 : INSERT SAMPLE EXPENSES


-- IMPORTANT:
-- Subcategory IDs are based on the insertion order above.
--
--  1  = Kirana
--  2  = Vegetables
--  4  = Milk
--
--  7  = Electricity Bill
-- 10  = Mobile Recharge
--
-- 13  = Building Maintenance
--
-- 19  = Property Tax
--
-- 21  = Doctor Consultation
-- 22  = Hospital
-- 23  = Medicines
-- 24  = Medical Tests
--
-- 27  = Restaurant
--
-- 32  = Petrol
-- 34  = Bus
-- 35  = Auto
--
-- 40  = Hotel Stay
-- 41  = Train Ticket
--
-- 48  = College Fees


INSERT INTO expenses
(
    expense_date,
    subcategory_id,
    member_id,
    vendor_id,
    payment_method_id,
    amount,
    quantity,
    bill_number,
    description,
    is_recurring,
    due_date,
    paid_status
)
VALUES


-- GROCERY


('2026-01-02', 1, 2, 1, 2,
 2350.00, 1, 'KIR001',
 'Monthly kirana purchase',
 FALSE, NULL, 'PAID'),

('2026-01-05', 2, 2, NULL, 1,
 450.00, 1, NULL,
 'Weekly vegetables',
 FALSE, NULL, 'PAID'),

('2026-01-10', 4, 2, NULL, 1,
 900.00, 1, NULL,
 'Monthly milk expenses',
 TRUE, NULL, 'PAID'),

-- ELECTRICITY


('2026-01-07', 7, 1, 3, 2,
 3250.00, 1, 'ELEC001',
 'Monthly electricity bill',
 TRUE, '2026-01-10', 'PAID'),

-- BUILDING MAINTENANCE
('2026-01-10', 13, 1, NULL, 2,
 2500.00, 1, 'MAINT001',
 'Monthly building maintenance',
 TRUE, '2026-01-10', 'PAID'),


-- PROPERTY TAX

('2026-01-15', 19, 1, 4, 2,
 8500.00, 1, 'TAX001',
 'Annual property tax',
 TRUE, '2026-01-31', 'PAID'),


-- MEDICAL

('2026-01-18', 21, 1, 5, 2,
 500.00, 1, 'HOS001',
 'Doctor consultation',
 FALSE, NULL, 'PAID'),

('2026-01-18', 23, 1, 6, 2,
 1250.00, 1, 'MED001',
 'Medicines',
 FALSE, NULL, 'PAID'),

('2026-01-20', 24, 2, 5, 3,
 4500.00, 1, 'LAB001',
 'Medical tests',
 FALSE, NULL, 'PAID'),

-- RESTAURANT

('2026-01-21', 27, 1, 8, 3,
 1850.00, 4, 'RES001',
 'Family dinner',
 FALSE, NULL, 'PAID'),

-- TRANSPORTATION

('2026-01-22', 32, 1, 7, 2,
 2000.00, 40, 'PET001',
 'Petrol',
 FALSE, NULL, 'PAID'),

('2026-01-23', 35, 3, NULL, 1,
 300.00, 5, NULL,
 'Auto travelling',
 FALSE, NULL, 'PAID'),

-- TOURISM

('2026-01-25', 41, 1, 9, 2,
 3200.00, 4, 'TRN001',
 'Family train tickets',
 FALSE, NULL, 'PAID'),


-- EDUCATION

('2026-01-28', 48, 3, NULL, 5,
 25000.00, 1, 'EDU001',
 'College fees',
 TRUE, NULL, 'PAID'),

-- MOBILE

('2026-01-30', 10, 1, 10, 2,
 799.00, 1, 'MOB001',
 'Monthly mobile recharge',
 TRUE, NULL, 'PAID');

 -- STEP 13 : VERIFY TABLES

SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'public'
ORDER BY table_name;


-- STEP 14 : VERIFY DATA

SELECT * FROM expense_categories;

SELECT * FROM expense_subcategories;

SELECT * FROM family_members;

SELECT * FROM payment_methods;

SELECT * FROM vendors;

SELECT * FROM expenses;


