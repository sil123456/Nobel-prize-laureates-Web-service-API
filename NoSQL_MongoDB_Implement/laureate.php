<?php
// get the id parameter from the request
    $id = intval($_GET['id']);

    $mng = new MongoDB\Driver\Manager("mongodb://localhost:27017");

    $options = ['projection' => ['_id' => 0]];
    $filter = ['id' => strval($id)];
    $query = new MongoDB\Driver\Query($filter, $options); 
    #$query = new MongoDB\Driver\Query([]); 

    $rows = $mng->executeQuery("nobel.laureates", $query);
    foreach ($rows as $row) {
        echo json_encode($row, JSON_PRETTY_PRINT);
    }
?>