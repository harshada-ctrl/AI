-- ============================================================
-- Quarterly Family Expense Budget
-- THREE-MONTH ANALYSIS
-- Months: September, October, November 2026
-- ============================================================


-- ============================================================
------------------------ EXPENSE CATEGORIES -------------------
-- ============================================================

CREATE TABLE expense_categories (
    category_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    category_name VARCHAR(100) NOT NULL UNIQUE
);

-- ============================================================
------------------------ EXPENSE SUBCATEGORIES ----------------
-- ============================================================

CREATE TABLE expense_subcategories (
    subcategory_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    category_id INT NOT NULL,
    subcategory_name VARCHAR(100) NOT NULL,
    
    CONSTRAINT fk_subcategory_category
        FOREIGN KEY (category_id)
        REFERENCES expense_categories(category_id)
);


-- ============================================================
------------------------ FAMILY MEMBER ------------------------
-- ============================================================


CREATE TABLE family_members (
    member_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    member_name VARCHAR(100) NOT NULL
);


-- ============================================================
------------------------ PAYMENT METHOD -----------------------
-- ============================================================


CREATE TABLE payment_methods (
    payment_method_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    payment_method_name VARCHAR(50) NOT NULL UNIQUE
);

-- ============================================================
------------------------ VENDORS ------------------------------
-- ============================================================

CREATE TABLE vendors (
    vendor_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    vendor_name VARCHAR(100) NOT NULL
);

-- ============================================================
------------------------ EXPENSES -----------------------------
-- ============================================================

CREATE TABLE expenses (
    expense_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    expense_date DATE NOT NULL,
    subcategory_id INT NOT NULL,
    member_id INT NOT NULL,
    vendor_id INT,
    payment_method_id INT NOT NULL,
    amount NUMERIC(10,2) NOT NULL,
    quantity INT DEFAULT 1,
    description VARCHAR(255),
    is_recurring BOOLEAN DEFAULT FALSE,
    payment_status VARCHAR(20) DEFAULT 'Paid',

    CONSTRAINT chk_amount
        CHECK (amount > 0),

    CONSTRAINT chk_quantity
        CHECK (quantity > 0),

    CONSTRAINT chk_payment_status
        CHECK (payment_status IN ('Paid', 'Pending')),

    CONSTRAINT fk_expense_subcategory
        FOREIGN KEY (subcategory_id)
        REFERENCES expense_subcategories(subcategory_id),

    CONSTRAINT fk_expense_member
        FOREIGN KEY (member_id)
        REFERENCES family_members(member_id),

    CONSTRAINT fk_expense_vendor
        FOREIGN KEY (vendor_id)
        REFERENCES vendors(vendor_id),

    CONSTRAINT fk_expense_payment
        FOREIGN KEY (payment_method_id)
        REFERENCES payment_methods(payment_method_id)
);

-- ============================================================
------------------------ QUARTERLY BUDGET ---------------------
-- ============================================================


CREATE TABLE quarterly_budget (
    budget_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    category_id INT NOT NULL,
    budget_month DATE NOT NULL,
    proposed_amount NUMERIC(10,2) NOT NULL,
    reason VARCHAR(255),

    CONSTRAINT chk_budget_amount
        CHECK (proposed_amount > 0),

    CONSTRAINT fk_budget_category
        FOREIGN KEY (category_id)
        REFERENCES expense_categories(category_id)
);

-- ============================================================
--------- DATA INSERT INTO EXPENSE CATEGORIES -----------------
-- ============================================================


INSERT INTO expense_categories (category_name)
VALUES
('Food'),
('Utilities'),
('Transportation'),
('Medical'),
('Education'),
('Housing'),
('Financial'),
('Discretionary');

-- ============================================================
--------- DATA INSERT INTO FAMILY MEMBERS ---------------------
-- ============================================================

INSERT INTO family_members (member_name)
VALUES
('HARSHADA'),
('ASHISH');

-- ============================================================
--------- DATA INSERT INTO PAYMENT METHODS --------------------
-- ============================================================

INSERT INTO payment_methods (payment_method_name)
VALUES
('Cash'),
('UPI');

-- ============================================================
--------- DATA INSERT INTO VENDORS ----------------------------
-- ============================================================

INSERT INTO vendors (vendor_name)
VALUES
('D-Mart'),
('Medicos'),
('Corporation'),
('HP Petrol Pump'),
('Airtel'),
('Jio'),
('Vi'),
('AIgenius'),
('Sai Automobiles'),
('Blackstone Hotel');


