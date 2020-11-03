<?php

require_once("ParsingJson.php");


// Initialisation Class ParsingJson
$parsingJson = new ParsingJson("Python/FileTest2.json");
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



// Récupération des 25 premier elements
$trumpBestElems = $parsingJson->getFirstElemsArray($trumpSortedArray, 25);
$bidenBestElems = $parsingJson->getFirstElemsArray($bidenSortedArray, 25);


// Création file result
$parsingJson->createResultFile("Trump", $trumpBestElems);
$parsingJson->createResultFile("Biden", $bidenBestElems);




// Test For App
// $parsingJson = new ParsingJson("Python/FileTest2.json");
// $test = $parsingJson->getJsonToArray();




// Test For InterfaceWeb
$trumpJsonString = file_get_contents("Result/Trump.json");
$trumpJsonArray = json_decode($trumpJsonString, true);

$bidenJsonString = file_get_contents("Result/Biden.json");
$bidenJsonArray = json_decode($bidenJsonString, true);

// Affichage
var_dump($trumpJsonArray);
var_dump($bidenJsonArray);
