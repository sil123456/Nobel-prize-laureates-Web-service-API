//select count(*) as numberofcity from (select distinct city from Affiliations where name = 'University of California' group by city) count;


db.laureates.aggregate([
    { $unwind: "$nobelPrizes" },
    { $unwind: "$nobelPrizes.affiliations"},
    { $match: { "nobelPrizes.affiliations.name.en": "University of California" } },
    { $group: { '_id': "$nobelPrizes.affiliations.city.en", count: { $sum: 1 } } },
    { $group: { '_id': null, locations: { $sum: 1 } } },
    { $project: {'_id': 0}}
])

