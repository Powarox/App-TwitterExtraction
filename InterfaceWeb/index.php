<?php
require_once('View/View.php');
require_once("Control/Controller.php");

// Instanciation class
$view = new View();
$controller = new Controller($view);


// Action
$controller->execute('Trump', 'Biden');


// Affichage Template
$view->render('Template.php');
