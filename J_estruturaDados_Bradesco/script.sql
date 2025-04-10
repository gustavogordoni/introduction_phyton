CREATE TABLE agenda (
    N_IDCONTATO INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    T_NOMECONTATO VARCHAR(30) NOT NULL,
    T_TELEFONECONTATO VARCHAR(14) NOT NULL,
    T_EMAILCONTATO VARCHAR(30)
);

CREATE TABLE alunos (
    CODIGO INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    NOME VARCHAR(50) NOT NULL,
    ENDERECO VARCHAR(22) NOT NULL,
    TELEFONE VARCHAR(28) NOT NULL,
    NOTAS DECIMAL(0.2) NOT NULL,
    TURMA VARCHAR(21)
);

CREATE TABLE clientes (
    CLIENTES_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    NOME TEXT NOT NULL,
    REGIAO TEXT,
    ENDERECO TEXT,
    CIDADE TEXT,
    ESTADO TEXT,
    CEP INTEGER
);

INSERT INTO
    "CLIENTES" (
        "CLIENTES_ID",
        "NOME",
        "REGIAO",
        "ENDERECO",
        "CIDADE",
        "ESTADO",
        "CEP"
    )
VALUES (
        1,
        'LITE Industrial',
        'Southwest',
        '729 Ravine Way',
        'Irving',
        'TX',
        75014
    ),
    (
        2,
        'Rex Tooling Inc',
        'Southwest',
        '6129 Collie Blvd',
        'Dallas',
        'TX',
        75201
    ),
    (
        3,
        'Re-Barre Construction',
        'Southwest',
        '9043 Windy Dr',
        'Irving',
        'TX',
        75032
    ),
    (
        4,
        'Prairie Construction',
        'Southwest',
        '264 Long Rd',
        'Moore',
        'OK',
        62104
    ),
    (
        5,
        'Marsh Lane Metal Works',
        'Southeast',
        '9143 Marsh Ln',
        'Avondale',
        'LA',
        79782
    );

SELECT CLIENTES_ID, REGIAO FROM CLIENTES;

SELECT CLIENTES_ID, CEP FROM CLIENTES;

SELECT CLIENTES_ID, ENDERECO FROM CLIENTES;

SELECT
    PRODUCT_ID,
    DESCRIPTION,
    PRICE,
    PRICE * 1.05 AS TAXED_PRICE
FROM PRODUCT;

SELECT * FROM station_data;

CREATE TABLE clientes (
    CLIENTES_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    NOME TEXT NOT NULL,
    REGIAO TEXT,
    ENDERECO TEXT,
    CIDADE TEXT,
    ESTADO TEXT,
    CEP INTEGER
);

INSERT INTO
    clientes (
        "CLIENTES_ID",
        "NOME",
        "REGIAO",
        "ENDERECO",
        "CIDADE",
        "ESTADO",
        "CEP"
    )
VALUES (
        1,
        'LITE Industrial',
        'Southwest',
        '729 Ravine Way',
        'Irving',
        'TX',
        75014
    ),
    (
        2,
        'Rex Tooling Inc',
        'Southwest',
        '6129 Collie Blvd',
        'Dallas',
        'TX',
        75201
    ),
    (
        3,
        'Re-Barre Construction',
        'Southwest',
        '9043 Windy Dr',
        'Irving',
        'TX',
        75032
    ),
    (
        4,
        'Prairie Construction',
        'Southwest',
        '264 Long Rd',
        'Moore',
        'OK',
        62104
    ),
    (
        5,
        'Marsh Lane Metal Works',
        'Southeast',
        '9143 Marsh Ln',
        'Avondale',
        'LA',
        79782
    );

CREATE TABLE CUSTOMER_ORDER (
    ORDER_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    ORDER_DATE DATE NOT NULL,
    SHIP_DATE DATE,
    CUSTOMER_ID INTEGER REFERENCES CUSTOMER (CUSTOMER_ID) NOT NULL,
    PRODUCT_ID INTEGER REFERENCES PRODUCT (PRODUCT_ID) NOT NULL,
    ORDER_QTY INTEGER NOT NULL,
    SHIPPED BOOLEAN NOT NULL DEFAULT (0)
);

INSERT INTO
    "CUSTOMER_ORDER" (
        "ORDER_ID",
        "ORDER_DATE",
        "SHIP_DATE",
        "CUSTOMER_ID",
        "PRODUCT_ID",
        "ORDER_QTY",
        "SHIPPED"
    )
VALUES (
        '1',
        '2015-05-15',
        '2015-05-18',
        '1',
        '1',
        '450',
        'false'
    ),
    (
        '2',
        '2015-05-18',
        '2015-05-21',
        '3',
        '2',
        '600',
        'false'
    ),
    (
        '3',
        '2015-05-20',
        '2015-05-23',
        '3',
        '5',
        '300',
        'false'
    ),
    (
        '4',
        '2015-05-18',
        '2015-05-22',
        '5',
        '4',
        '375',
        'false'
    ),
    (
        '5',
        '2015-05-17',
        '2015-05-20',
        '3',
        '2',
        '500',
        'false'
    );

CREATE TABLE PRODUCT (
    PRODUCT_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    DESCRIPTION TEXT,
    PRICE DECIMAL
);

INSERT INTO
    "PRODUCT" (
        "PRODUCT_ID",
        "DESCRIPTION",
        "PRICE"
    )
VALUES (1, 'Copper', 7.51),
    (2, 'Aluminum', 2.58),
    (3, 'Silver', 15),
    (4, 'Steel', 12.31),
    (5, 'Bronze', 4),
    (6, 'Duralumin', 7.6),
    (7, 'Solder', 14.16),
    (8, 'Stellite', 13.31),
    (9, 'Brass', 4.75);

SELECT * FROM STATION_DATA WHERE year = 2009;

SELECT * FROM station_data WHERE year != 2009

SELECT * FROM station_data WHERE year <> 2009

SELECT * FROM station_data WHERE year >= 2006 AND year <= 2008

SELECT COUNT(*) AS record_count FROM station_data;

SELECT year, COUNT(*) AS record_count
FROM STATION_DATA
WHERE
    tornado = 1
GROUP BY
    year;

SELECT year, month, COUNT(*) AS record_count
FROM STATION_DATA
WHERE
    tornado = 1
GROUP BY
    year,
    month

SELECT year, COUNT(*) AS record_count
FROM STATION_DATA
WHERE
    tornado = 1
GROUP BY
    year;

SELECT year, month, COUNT(*) AS record_count
FROM STATION_DATA
WHERE
    tornado = 1
GROUP BY
    year,
    month

SELECT year, month, COUNT(*) AS record_count
FROM station_data
WHERE
    tornado = 1
GROUP BY
    year,
    month
ORDER BY year DESC, month

SELECT
    report_code,
    year,
    month,
    day,
    wind_speed,
    CASE
        WHEN wind_speed >= 39 THEN 'Rápido'
        WHEN wind_speed >= 29
        AND wind_speed < 40 THEN 'Moderado'
        ELSE 'Fraco'
    END as wind_severity
FROM station_data

SELECT
    report_code,
    year,
    month,
    day,
    wind_speed,
    CASE
        WHEN wind_speed >= 39 THEN 'Rápido'
        WHEN wind_speed >= 29
        AND wind_speed < 40 THEN 'Moderado'
        ELSE 'Fraco'
    END as wind_severity
FROM station_data