<?php 
    require '../Models/function.php';
    class DataGetter{
        public static function getInfos($infos){
            
            $bd = new Database('loginsystem');
            $mail = $infos['username'];
            $mdp = $infos['password'];
            $datetime = Date::getCurrentTime();
        
            $bd -> execute("INSERT INTO user(mail,mdp, date_time) values(?, ?, ?)",
            [$mail,$mdp, $datetime] );
        
            
        }
    }
?>