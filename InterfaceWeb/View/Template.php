<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="Other/Styles/styles.css">
    <script defer src="Other/Js/script.js"></script>
    <title><?php echo $this->title; ?></title>
</head>
<body>


    <header>
        <h1><?php echo $this->title; ?></h1>
    </header>

    <main>
        <section class="display">
            <ul>
                <li><button id="btnTrump">Donald Trump</button></li>
                <li><button id="btnBiden">Joe Biden</button></li>
            </ul>
        </section>

        <?php echo $this->legend; ?>

        <?php echo $this->content; ?>
    </main>

</body>
</html>
