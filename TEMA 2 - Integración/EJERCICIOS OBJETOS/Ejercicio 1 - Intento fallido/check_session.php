<?php
session_start();
if (empty($_SESSION)) {
    echo "success";
} else {
    echo "error";
}
