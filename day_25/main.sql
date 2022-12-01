DROP TABLE IF EXISTS dec25;

CREATE TABLE dec25 (
    line_number bigint NOT NULL GENERATED ALWAYS AS IDENTITY,
    value bigint NOT NULL
);

\COPY dec01 (value) FROM '2022/dec25/input.txt'
VACUUM ANALYZE dec01;
