
SELECT a, b, c, path
FROM
    (
        SELECT DISTINCT 
            k[0] AS a,
            k[1] AS b,
            k[2] AS c,
            path
        FROM
            {{ source('test', 'ranked_binary_file_input') }}
            LATERAL VIEW EXPLODE(shingles(content, 3)) AS k
    )
ORDER BY 1,2,3,4
