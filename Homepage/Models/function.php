<?php 

    Class Date {
        public static function getCurrentTime(){
            $currentTime = new DateTime();
            return $currentTime->format('Y-m-d H:i:s');
        }
    }
    
?>