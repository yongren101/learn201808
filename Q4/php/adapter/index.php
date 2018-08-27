<?php
/**
 * Created by PhpStorm.
 * User: KLC
 * Date: 2018/8/24
 * Time: 16:03
 */
require_once 'class/Dog.php';
require_once 'class/BlackAdapter.php';

$Dog = new Dog();
$Dog->call();
$Dog->walk();

$BlackDog= new BlackAdapter($Dog);
$BlackDog->walknow();
$BlackDog->singing();

