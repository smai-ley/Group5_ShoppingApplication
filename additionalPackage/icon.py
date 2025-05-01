#icon.py 

# Because we are iconic!

class Icon():
    def __init__(self):
        pass
    
    def bear(self):
        print("ʕᵔᴥᵔʔ")
    
    def cat(self):
        print(r"""
                        /\_/\           ___
                       = o_o =_______    \ \  
                        __^      __(  \.__) )
                    (@)<_____>__(_____)____/
        """)
    
    def balloon(self):
        print (r"""
                                         _ .--.
                                        ( `    )
                                     .-'      `--,
                          _..----.. (             )`-.
                        .'_|` _|` _|(  .__,           )
                       /_|  _|  _|  _(        (_,  .-'
                      ;|  _|  _|  _|  '-'__,--'`--'
                      | _|  _|  _|  _| |
                  _   ||  _|  _|  _|  _|
                _( `--.\_|  _|  _|  _|/
             .-'       )--,|  _|  _|.`
            (__, (_      ) )_|  _| /
              `-.__.\ _,--'\|__|__/
                            ;____;
                             \YT/
                              ||
                             |""|
                             '=='
         """)
        
    def print_art(self, icon_type):
        """
        Prints out art associated with a specific icon 
        @param icon_type, str fed in from show_info in customer
        @return none
        """
        try:
            icon_type = icon_type.lower()
            if (icon_type == "shirt"):
                print(r"""
                ____ ____
               /| |/|\| |\
              /_| ´ |.` |_\
                |   |.  |
                |   |.  |
                |___|.__|
                """)
            elif(icon_type == "pants"):
                print(r"""
                ,==c==.
                |_/|\_|
                | ´|` |
                |  |  |
                |  |  |
                |__|__|
                            """)
            elif(icon_type == "t-shirt"):
                print(r"""
                __   __  
               /  `-'  \ 
              /_| U   |_\
                |  C  |  
                |   ! |  
                |_____|
                      
                            """)
            elif (icon_type == "hoodie"):
                print(r"""      
                __   __    
               /  `-'  \   
              / |     | \  
             / /| ___ |\ \ 
            /_/ |/   \| \_\
                |_____|
                    """)
            elif (icon_type == "socks"):
                print(r"""
                 ________ __
                |_______ |__|
                |------- |--`-------.
                |        `--------.  \
                |              |   \  |
                \              |    |/
                  \_________________/
                      """)
        except:
            return None
        