Use climbing;
SELECT * FROM climbing.raw_data_climbing_survey_enc;

select* from raw_data_climbing_survey_enc where Gender = 'Female' and level like '7B';
SELECT * FROM climbing_shoes;
SELECT * FROM grading_system;

SELECT climbing_shoes.brand,climbing_shoes.level,climbing_shoes.difficulty,grading_system.french_level,grading_system.GB_level
FROM climbing_shoes
JOIN grading_system
ON climbing_shoes.difficulty = grading_system.difficulty;
# 
Select `Climbing shoes`, SUM(level) as nbLevels FROM raw_data_climbing_survey_enc group by `Climbing shoes`
Order by nbLevels DESC
LIMIT 1;

Select gender, age  FROM raw_data_climbing_survey_enc
Where competition = 'yes'
;