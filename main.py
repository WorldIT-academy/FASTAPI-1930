import colorama 
import uvicorn

colorama.init(autoreset= True)
RED = colorama.Fore.RED
YELLOW = colorama.Fore.YELLOW

def main():
    """ """
    try:
        #
        uvicorn.run("modules:app", reload= True) 
    except Exception as exception:
        print(f"\n{RED}ERROR: {YELLOW}{exception}\n")
        

if __name__ == "__main__":
    main()