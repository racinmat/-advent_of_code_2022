DROP TABLE IF EXISTS dec04;

CREATE TABLE dec04 (
    line_number bigint NOT NULL GENERATED ALWAYS AS IDENTITY,
    value bigint NOT NULL
);

\COPY dec01 (value) FROM '2022/dec04/input.txt'
VACUUM ANALYZE dec01;
