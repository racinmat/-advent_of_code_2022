DROP TABLE IF EXISTS dec16;

CREATE TABLE dec16 (
    line_number bigint NOT NULL GENERATED ALWAYS AS IDENTITY,
    value bigint NOT NULL
);

\COPY dec01 (value) FROM '2022/dec16/input.txt'
VACUUM ANALYZE dec01;
