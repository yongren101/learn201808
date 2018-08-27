<?php

class Single
{
    static private $instance;
    //参数
    private $config;

    private function __construct($config)
    {
        $this->config = $config;
        echo "创建实例";
    }

    //防止克隆对象
    private function __clone(){}

    static public function getInstance($config)
    {
        if (!self::$instance instanceof self) {
            self::$instance = new self($config);
        }
        return self::$instance;

    }

    public function getName()
    {
        echo $this->config;
    }
}
