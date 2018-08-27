<?php
/**
 * Created by PhpStorm.
 * User: KLC
 * Date: 2018/8/24
 * Time: 15:58
 */
require_once 'BlackInterface.php';

class BlackAdapter implements BlackInterface
{
    private $adaptee;

    function __construct(Animal $adaptee)
    {
        $this->adaptee = $adaptee;
    }

    public function walkNow()
    {
       $this->adaptee->walk();
    }

    public function singing()
    {
        echo 'I can singing!';
    }
}