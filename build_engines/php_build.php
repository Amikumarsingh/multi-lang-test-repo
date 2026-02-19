#!/usr/bin/env php
<?php
$result = 0;
system('phpunit tests/test_php.php', $result);
exit($result);
?>
