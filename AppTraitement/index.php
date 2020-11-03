<?php

require_once("ParsingJson.php");


// Initialisation Class ParsingJson
$parsingJson = new ParsingJson("JsonFiles/us_election_tweet_part6.json");
$parsingJson->getJsonToArray();



// Séparation Trump / Biden Tweet
$parsingJson->findTrumpOrBiden();

$trumpArray = $parsingJson->getTrumpArray();
$bidenArray = $parsingJson->getBidenArray();



// Suppressions mots inutile
$banWord = $parsingJson->regexpBanWord();

$trumpImportantWords = $parsingJson->extractionImportantWord($banWord, $trumpArray);
$bidenImportantWords = $parsingJson->extractionImportantWord($banWord, $bidenArray);



// Count occurence mots
$trumpCountOccurence = $parsingJson->countOccurenceWord($trumpImportantWords);
$bidenCountOccurence = $parsingJson->countOccurenceWord($bidenImportantWords);



// Trié les array par ordre décroissant
$trumpSortedArray = $parsingJson->arraySorted($trumpCountOccurence);
$bidenSortedArray = $parsingJson->arraySorted($bidenCountOccurence);



// Création file result
$parsingJson->createResultFile("Trump", $trumpSortedArray);
$parsingJson->createResultFile("Biden", $bidenSortedArray);




// Test For App
$parsingJson = new ParsingJson("Python/FileTest2.json");
$test = $parsingJson->getJsonToArray();

var_dump($test);


$jsonString = file_get_contents("Python/FileTest2.json");
$jsonArray = json_decode($jsonString, true);

var_dump($jsonArray);

$jsonString = file_get_contents("us_election20_tweet_pr.json");
$jsonArray = json_decode($jsonString, true);

var_dump($jsonArray);






// Test For InterfaceWeb
$trumpJsonString = file_get_contents("Result/Trump.json");
$trumpJsonArray = json_decode($trumpJsonString, true);

$bidenJsonString = file_get_contents("Result/Biden.json");
$bidenJsonArray = json_decode($bidenJsonString, true);


//var_dump($trumpJsonArray);
//var_dump($bidenJsonArray);














// Mise en page Json

/*$file = fopen("test_json.php", "r+");




if (!($f=fopen("exemple.txt","r+"))) // Ouverture file read/write
    exit("Unable to open file!");


// ecriture
$f = 'exemple.txt';
$text = "ma chaine de caractères";
$handle = fopen($f,"w");

// regarde si le fichier est accessible en écriture
if (is_writable($f)) {
// Ecriture
    if (fwrite($handle, $text) === FALSE) {
      echo 'Impossible d\'écrire dans le fichier '.$f.'';
      exit;
    }

    echo 'Ecriture terminé';

    fclose($handle);

}
else {
      echo 'Impossible d\'écrire dans le fichier '.$f.'';
    }



if (feof($f))   // Find the end
    echo 'Fin du fichier';*/
