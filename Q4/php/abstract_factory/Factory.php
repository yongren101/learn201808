<?php
/**
 * 工程类，主要用来创建对象
 * 功能：输入相应的值, 返回对应的对象实例
 *
 */
require_once 'class/Class1.php';
require_once 'class/Class2.php';
require_once 'class/Class3.php';
require_once 'class/Class4.php';
class Factory
{

    public static function getInstance($tag)
    {
        switch ($tag) {
            case '1':
                return new Class1();
                break;
            case '2':
                return new Class2();
                break;
            case '3':
                return new Class3();
                break;
            case '4':
                return new Class4();
                break;
        }
    }
}

