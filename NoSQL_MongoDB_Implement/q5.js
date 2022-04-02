// select count(*) as yearcount from (select awardYear from NobelPrizes N, Affiliations A, Laureates L where N.id = L.id and gender is NULL group by awardYear) Ycount;
// In how many years a Nobel prize was awarded to an organization (as opposed to a person) in at least one category?

db.laureates.aggregate([
    { $unwind: "$nobelPrizes" },
    
    { $match: {"orgName": {$exists: true}}},
    { $group: { '_id': "$nobelPrizes.awardYear", count: { $sum: 1 } } },

    { $group: { '_id': null, years: { $sum: 1 } } },
    { $project: {'_id': 0}}
])