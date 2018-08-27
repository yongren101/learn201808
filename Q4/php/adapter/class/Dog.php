<?php
/**
 * Created by PhpStorm.
 * User: KLC
 * Date: 2018/8/24
 * Time: 15:56
 */
require_once 'Animal.php';

class Dog extends Animal
{
    public function call()
    {
        echo 'call';
    }

    public  function walk()
    {
        echo 'walk';
    }
}