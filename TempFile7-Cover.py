import re
from Classes.ClassDoostiha import *
from Classes.ClassHex import *
from Classes.ClassIMDB import *
from Classes.Timer import Timer
from Forms.CreateCovers.ClassTable import *


class Main:
    def __init__(self):
        films_array = []

        # paths = [
        #     'D:\Tab\Temp\(DA1545) - Alexander and the Terrible, Horrible, No Good, Very Bad Day (2014)',
        #     'D:\Tab\Temp\(DA1873) - Interview with the Vampire The Vampire Chronicles (1994)',
        #     'D:\Tab\Temp\(DA1955) - Master and Commander The Far Side of the World (2003)',
        #     'D:\Tab\Temp\(DA2183) - The Assassination of Jesse James by the Coward Robert Ford (2007)',
        #     'D:\Tab\Temp\(DA2183) - The Assassination of Jesse James by the Coward Robert Ford (2007) - Copy',
        #     'D:\Tab\Temp\(DA2571) - Harry Potter 7 and the Deathly Hallows Part 1 (2010)',
        #     'D:\Tab\Temp\(DA2572) - Harry Potter 8 and the Deathly Hallows Part 2 (2011)',
        #     'D:\Tab\Temp\(DA2586) - Indiana Jones 4 and the Kingdom of the Crystal Skull (2008)',
        #     'D:\Tab\Temp\(DA2652) - Night at the Museum 2 Battle of the Smithsonian (2009)',
        #     'D:\Tab\Temp\(DA2652) - Night at the Museum 2 Battle of the Smithsonian (2009) - Copy',
        #     'D:\Tab\Temp\(DA2663) - Pirates of the Caribbean 1 The Curse of the Black Pearl (2003)',
        #     'D:\Tab\Temp\(DA2667) - Pirates of the Caribbean 5 Dead Men Tell No Tales (2017)',
        #     'D:\Tab\Temp\(DA2711) - Teenage Mutant Ninja Turtles 2 Out of the Shadows (2016)',
        #     'D:\Tab\Temp\(DA2718) - The Chronicles of Narnia 1 The Lion the Witch and the Wardrobe (2005)',
        #     'D:\Tab\Temp\(DA2720) - The Chronicles of Narnia 3 The Voyage of the Dawn Treader (2010)',
        #     'D:\Tab\Temp\(DA2720) - The Chronicles of Narnia 3 The Voyage of the Dawn Treader (2010) 2',
        #     'D:\Tab\Temp\(DA2720) - The Chronicles of Narnia 3 The Voyage of the Dawn Treader (2010) 3',
        #     'D:\Tab\Temp\(DA2720) - The Chronicles of Narnia 3 The Voyage of the Dawn Treader (2010) 5',
        #     'D:\Tab\Temp\(DA2738) - The Lord of the Rings 1 The Fellowship of the Ring (2001)',
        #     'D:\Tab\Temp\(DA2738) - The Lord of the Rings 1 The Fellowship of the Ring (2001) 4',
        #     'D:\Tab\Temp\(DA2740) - The Lord of the Rings 3 The Return of the King (2003)',
        #     'D:\Tab\Temp\(DA2740) - The Lord of the Rings 3 The Return of the King (2003) 2',
        #     'D:\Tab\Temp\(DA2859) - The Brocade Mouse Royal Cat Nine Deep Blood Wolf (2021)',
        #     'D:\Tab\Temp\(DA2859) - The Brocade Mouse Royal Cat Nine Deep Blood Wolf (2021) 2',
        #     'D:\Tab\Temp\(DA2956) -  Doctor Strange 2 in the Multiverse of Madness (2022)',
        #     'D:\Tab\Temp\(DA2956) -  Doctor Strange 2 in the Multiverse of Madness (2022)2'
        # ]

        paths = [
            'D:\Wallpaper\Tab\Temp\(DA1545) - Alexander and the Terrible, Horrible, No Good, Very Bad Day (2014)',
            'D:\Wallpaper\Tab\Temp\(DA1873) - Interview with the Vampire The Vampire Chronicles (1994)',
            'D:\Wallpaper\Tab\Temp\(DA1955) - Master and Commander The Far Side of the World (2003)',
            'D:\Wallpaper\Tab\Temp\(DA2183) - The Assassination of Jesse James by the Coward Robert Ford (2007)',
            'D:\Wallpaper\Tab\Temp\(DA2183) - The Assassination of Jesse James by the Coward Robert Ford (2007) - Copy',
            'D:\Wallpaper\Tab\Temp\(DA2571) - Harry Potter 7 and the Deathly Hallows Part 1 (2010)',
            'D:\Wallpaper\Tab\Temp\(DA2572) - Harry Potter 8 and the Deathly Hallows Part 2 (2011)',
            'D:\Wallpaper\Tab\Temp\(DA2586) - Indiana Jones 4 and the Kingdom of the Crystal Skull (2008)',
            'D:\Wallpaper\Tab\Temp\(DA2652) - Night at the Museum 2 Battle of the Smithsonian (2009)',
            'D:\Wallpaper\Tab\Temp\(DA2652) - Night at the Museum 2 Battle of the Smithsonian (2009) - Copy',
            'D:\Wallpaper\Tab\Temp\(DA2663) - Pirates of the Caribbean 1 The Curse of the Black Pearl (2003)',
            'D:\Wallpaper\Tab\Temp\(DA2667) - Pirates of the Caribbean 5 Dead Men Tell No Tales (2017)',
            'D:\Wallpaper\Tab\Temp\(DA2711) - Teenage Mutant Ninja Turtles 2 Out of the Shadows (2016)',
            'D:\Wallpaper\Tab\Temp\(DA2718) - The Chronicles of Narnia 1 The Lion the Witch and the Wardrobe (2005)',
            'D:\Wallpaper\Tab\Temp\(DA2720) - The Chronicles of Narnia 3 The Voyage of the Dawn Treader (2010)',
            'D:\Wallpaper\Tab\Temp\(DA2720) - The Chronicles of Narnia 3 The Voyage of the Dawn Treader (2010) 2',
            'D:\Wallpaper\Tab\Temp\(DA2720) - The Chronicles of Narnia 3 The Voyage of the Dawn Treader (2010) 3',
            'D:\Wallpaper\Tab\Temp\(DA2720) - The Chronicles of Narnia 3 The Voyage of the Dawn Treader (2010) 5',
            'D:\Wallpaper\Tab\Temp\(DA2738) - The Lord of the Rings 1 The Fellowship of the Ring (2001)',
            'D:\Wallpaper\Tab\Temp\(DA2738) - The Lord of the Rings 1 The Fellowship of the Ring (2001) 4',
            'D:\Wallpaper\Tab\Temp\(DA2740) - The Lord of the Rings 3 The Return of the King (2003)',
            'D:\Wallpaper\Tab\Temp\(DA2740) - The Lord of the Rings 3 The Return of the King (2003) 2',
            'D:\Wallpaper\Tab\Temp\(DA2859) - The Brocade Mouse Royal Cat Nine Deep Blood Wolf (2021)',
            'D:\Wallpaper\Tab\Temp\(DA2859) - The Brocade Mouse Royal Cat Nine Deep Blood Wolf (2021) 2',
            'D:\Wallpaper\Tab\Temp\(DA2956) -  Doctor Strange 2 in the Multiverse of Madness (2022)',
            'D:\Wallpaper\Tab\Temp\(DA2956) -  Doctor Strange 2 in the Multiverse of Madness (2022)2'
        ]

        for i in paths:
            all_details = []

            file = rename_file_paths_by_os(i)

            film = None

            if os.path.isdir(file):
                if os.path.exists(file + CustomNames.EXTRACTED_DATA):
                    film = Film.json_file_to_class(file + CustomNames.EXTRACTED_DATA)
            if film:
                all_details.append(file)
                all_details.append(film)

                films_array.append(all_details)

        if films_array:
                Table(films_array, 15, 0, 1, 1, 1, "ex")


Main()
