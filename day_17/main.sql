DROP TABLE IF EXISTS dec17;

CREATE TABLE dec17 (
    line_number bigint NOT NULL GENERATED ALWAYS AS IDENTITY,
    value bigint NOT NULL
);

\COPY dec01 (value) FROM '2022/dec17/input.txt'
VACUUM ANALYZE dec01;
