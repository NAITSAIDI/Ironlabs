SELECT * FROM climbing_shoes;
SELECT * FROM grading_system;

SELECT climbing_shoes.brand,climbing_shoes.level,climbing_shoes.difficulty,grading_system.french_level,grading_system.GB_level
FROM climbing_shoes
JOIN grading_system
ON climbing_shoes.difficulty = grading_system.difficulty;
