DROP TABLE IF EXISTS dec21;

CREATE TABLE dec21 (
    line_number bigint NOT NULL GENERATED ALWAYS AS IDENTITY,
    value bigint NOT NULL
);

\COPY dec01 (value) FROM '2022/dec21/input.txt'
VACUUM ANALYZE dec01;
