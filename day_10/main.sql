DROP TABLE IF EXISTS dec10;

CREATE TABLE dec10 (
    line_number bigint NOT NULL GENERATED ALWAYS AS IDENTITY,
    value bigint NOT NULL
);

\COPY dec01 (value) FROM '2022/dec10/input.txt'
VACUUM ANALYZE dec01;
