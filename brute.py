
import itertools 
import string 
import sys  
import requests 
import argparse   

def brute( username , password , url)  :    
    #add the two parameters (username , password)    
    PARAMS = { 
              'username': username, 
              'password' : password  
             }   
    
    print(url , PARAMS)

    #r = requests.get(url = URL, params = PARAMS) 
      
    #data = r.json() 

    #print(data)
 
def main () :   

    #parser
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--username", help="valid username" )
    parser.add_argument("-url", "--url", help="url to attack  ")
     
    args = parser.parse_args()  

    #load the password files  
    with open("passwords.txt") as passwords:
        for password in passwords:  

            #valid username
            username = args.username   

            password = password.rstrip("\n" )  

            url = args.url   

            #brute force the login 
            brute( username , password  , url )

if __name__ == "__main__":
    main()  



        




        

