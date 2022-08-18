# Design Address Model

## Address of Order: Shipping, Billing

[Ref](https://dba.stackexchange.com/questions/111101/storing-a-billing-address-best-practice-in-orders-table)

## Standard Address

[Ref](https://stackoverflow.com/questions/7639637/sql-database-design-best-practice-addresses/7639805#7639805)

```bash
City, State, Country, postalcode
```

```SQL
CREATE TABLE DB.dbo.Addresses
    (
        Id          INT
                    NOT NULL
                    IDENTITY(1, 1)
                    PRIMARY KEY
                    CHECK (Id > 0),

        Address1    VARCHAR(120)
                                NOT NULL,

        Address2    VARCHAR(120),

        Address3    VARCHAR(120),

        City        VARCHAR(100)
                    NOT NULL,

        State       CHAR(2)
                    NOT NULL,

        Country     CHAR(2)
                    NOT NULL,

        PostalCode  VARCHAR(16)
                    NOT NULL
    )

CREATE TABLE DB.dbo.Orders
    (
        Id          INT
                    NOT NULL
                    IDENTITY(1000, 1)
                    PRIMARY KEY
                    CHECK (Id > 1000),

        Address     INT
                    CONSTRAINT fk_Orders_Address
                    FOREIGN KEY REFERENCES Addresses(Id)
                    CHECK (Address > 0)
                    NOT NULL,

        -- other columns....
    )

CREATE TABLE DB.dbo.Customers
    (
        Id          INT
                    NOT NULL
                    IDENTITY(1000, 1)
                    PRIMARY KEY
                    CHECK (Id > 1000),

        Address     INT
                    CONSTRAINT fk_Customers_Address
                    FOREIGN KEY REFERENCES Addresses(Id)
                    CHECK (Address > 0)
                    NOT NULL,

        -- other columns....
    )
```

## Address used for: customers, employees, shipments, orders

## Design with address, address2

[Ref](https://dev.mysql.com/doc/sakila/en/sakila-structure-tables-address.html)
Columns
address_id: A surrogate primary key used to uniquely identify each address in the table.

address: The first line of an address.

address2: An optional second line of an address.

district: The region of an address, this may be a state, province, prefecture, etc.

city_id: A foreign key pointing to the city table.

postal_code: The postal code or ZIP code of the address (where applicable).

phone: The telephone number for the address.

last_update: When the row was created or most recently updated.

location: A Geometry column with a spatial index on it.

## Address line 1 vs line 2

[Ref](https://www.quora.com/What-do-they-mean-by-address-line-1-and-address-line-2)
Địa chỉ nhà riêng: 25 Trần Phú, P.12, Q.5, TP. Hồ Chí Minh
=> Address 1: 25 TRAN PHU P.12 Q.5
Address 2: Bỏ trống
City: HO CHI MINH

Địa chỉ chung cư hoặc ký túc xá: Phòng 10C, chung cư Green House, 20 Hùng Vuơng, P.4, Q.5, TP. Hồ Chí Minh
=> Address 1: 20 HUNG VUONG P.4 Q.5
Address 2: PHONG 10C
City: HO CHI MINH
