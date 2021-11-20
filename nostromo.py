import time
import sys
import os

# 'weyland-yutani' ascii font for title
# 'building better worlds' ascii font for header

# set window height-width
os.system("printf '\033[8;40;116t'")

# create character delay effect for printout 's' is string variable
def delay_print(s):
  for c in s:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.02)

def cls():
    print("\n" * 50)
    
cls()

print("""



██╗    ██╗███████╗██╗   ██╗██╗      █████╗ ███╗   ██╗██████╗       ██╗   ██╗██╗   ██╗████████╗ █████╗ ███╗   ██╗██╗
██║    ██║██╔════╝╚██╗ ██╔╝██║     ██╔══██╗████╗  ██║██╔══██╗      ╚██╗ ██╔╝██║   ██║╚══██╔══╝██╔══██╗████╗  ██║██║
██║ █╗ ██║█████╗   ╚████╔╝ ██║     ███████║██╔██╗ ██║██║  ██║█████╗ ╚████╔╝ ██║   ██║   ██║   ███████║██╔██╗ ██║██║
██║███╗██║██╔══╝    ╚██╔╝  ██║     ██╔══██║██║╚██╗██║██║  ██║╚════╝  ╚██╔╝  ██║   ██║   ██║   ██╔══██║██║╚██╗██║██║
╚███╔███╔╝███████╗   ██║   ███████╗██║  ██║██║ ╚████║██████╔╝         ██║   ╚██████╔╝   ██║   ██║  ██║██║ ╚████║██║
 ╚══╝╚══╝ ╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝          ╚═╝    ╚═════╝    ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝


    ╔╗ ┬ ┬┬┬  ┌┬┐┬┌┐┌┌─┐    ╔╗ ┌─┐┌┬┐┌┬┐┌─┐┬─┐    ╦ ╦┌─┐┬─┐┬  ┌┬┐┌─┐    
    ╠╩╗│ │││   │││││││ ┬    ╠╩╗├┤  │  │ ├┤ ├┬┘    ║║║│ │├┬┘│   ││└─┐    
    ╚═╝└─┘┴┴─┘─┴┘┴┘└┘└─┘    ╚═╝└─┘ ┴  ┴ └─┘┴└─    ╚╩╝└─┘┴└─┴─┘─┴┘└─┘ 


""")

delay_print("Beta Version 0.0.4\n\n")

delay_print("Make your selection:\n\n")

delay_print("""
1.  USS Nostromo Crew Roster
2.  Ship Command Data-Log
3.  M.O.T.H.E.R. [CLASSIFIED]
4.  Weyland-Yutani Corp Employee Handbook
5.  Initiative 5147 [CLASSIFIED]
\n
""")

delay_print("COMMAND INTERFACE 2137 READY FOR INQUIRY\n\n")
delay_print("Please log onto secure systems with assigned ID: \n")




