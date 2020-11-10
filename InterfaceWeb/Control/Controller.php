<?php

require_once('View/View.php');

class Controller{
    protected $view;

    public function __construct($view){
        $this->view = $view;
    }

    public function execute($trump, $biden){
        $trumpJsonArray = $this->getAppTraitementResult($trump);
        $bidenJsonArray = $this->getAppTraitementResult($biden);

        //var_dump($bidenJsonArray);

        $this->view->makeHomePage();
    }

    public function getAppTraitementResult($name){
        $jsonString = file_get_contents('../AppTraitement/Result/'.$name.'.json');
        $jsonArray = json_decode($jsonString, true);
        return $jsonArray;
    }

    public function statisticsBare(){
        // $dataPoints = array(
        // 	array("label"=> "Education", "y"=> 284935),
        // 	array("label"=> "Entertainment", "y"=> 256548),
        // 	array("label"=> "Lifestyle", "y"=> 245214),
        // 	array("label"=> "Business", "y"=> 233464),
        // 	array("label"=> "Music & Audio", "y"=> 200285),
        // 	array("label"=> "Personalization", "y"=> 194422),
        // 	array("label"=> "Tools", "y"=> 180337),
        // 	array("label"=> "Books & Reference", "y"=> 172340),
        // 	array("label"=> "Travel & Local", "y"=> 118187),
        // 	array("label"=> "Puzzle", "y"=> 107530)
        // );
        //
        // <script>
        // window.onload = function () {
        //
        // var chart = new CanvasJS.Chart("chartContainer", {
        // 	animationEnabled: true,
        // 	theme: "light2", // "light1", "light2", "dark1", "dark2"
        // 	title: {
        // 		text: "Top 10 Google Play Categories - till 2017"
        // 	},
        // 	axisY: {
        // 		title: "Number of Apps"
        // 	},
        // 	data: [{
        // 		type: "column",
        // 		dataPoints: <?php echo json_encode($dataPoints, JSON_NUMERIC_CHECK);
        // 	}]
        // });
        // chart.render();
        // }
    }

    public function tagCloud(){
        // db_query('SELECT COUNT(*) AS count, id, name FROM ... ORDER BY count DESC');
        //
        // $steps = 6;
        // $tags = array();
        // $min = 1e9;
        // $max = -1e9;
        //
        // while ($tag = db_fetch_object($result)) {
        //     $tag->number_of_posts = $tag->count; #sets the amount of items a certain tag has attached to it
        //     $tag->count = log($tag->count);
        //     $min = min($min, $tag->count);
        //     $max = max($max, $tag->count);
        //     $tags[$tag->tid] = $tag;
        // }
        // // Note: we need to ensure the range is slightly too large to make sure even
        // // the largest element is rounded down.
        // $range = max(.01, $max - $min) * 1.0001;
        //
        // foreach ($tags as $key => $value) {
        //     $tags[$key]->weight = 1 + floor($steps * ($value->count - $min) / $range);
        // }
    }
}
