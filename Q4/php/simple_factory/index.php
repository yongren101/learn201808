<?php
/**
 * Created by PhpStorm.
 * User: KLC
 * Date: 2018/8/24
 * Time: 15:24
 */
require_once 'Factory.php';
$Factory = Factory::getInstance(1);
echo $Factory->getName();