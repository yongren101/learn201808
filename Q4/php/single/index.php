<?php
/**
 * Created by PhpStorm.
 * User: KLC
 * Date: 2018/8/24
 * Time: 15:35
 */
require_once 'Single.php';
$db1 = Single::getInstance(1);
$db1->getName();
echo "<br>";
$db2 = Single::getInstance(4);
$db2->getName();