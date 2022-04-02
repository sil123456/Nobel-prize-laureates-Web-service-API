select count(*) as yearcount from (select awardYear from NobelPrizes N, Affiliations A, Laureates L where N.id = L.id and gender is NULL group by awardYear) Ycount;

