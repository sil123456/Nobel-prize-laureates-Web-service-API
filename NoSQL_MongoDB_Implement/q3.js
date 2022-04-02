

//select familyname from Laureates group by coalesce(familyname, id) having count(*)>=5;



db.laureates.aggregate([
        // First Stage
        { $group: { _id : "$familyName.en", count: { $sum: 1 }}},
        // Second Stage
        { $match: { _id: { "$exists": true, "$ne": null}}},
        { $match: {count: {$gte: 5}}},
        { $project: { "familyName": "$_id", _id: 0  }},
])

