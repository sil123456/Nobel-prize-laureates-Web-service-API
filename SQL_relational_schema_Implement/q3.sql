select familyname from Laureates group by coalesce(familyname, id) having count(*)>=5;