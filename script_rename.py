"""
    This code renames .mp3 files from www.slider.kz
    Author: Andreza Cruz
"""

import os


def rename_mp3_files(location):
    for root, dirs, files in os.walk(location):
        for m_file in files:
            if m_file.endswith('.mp3'):
                print("OLD FILE NAME: " + m_file)

                old_file = os.path.join(location, m_file)
                
                # Change here the website extension
                new_name = m_file.replace(" [www.slider.kz]", "")
                new_file = os.path.join(location, new_name)
                print("NEW FILE NAME: " + new_file)

                os.rename(old_file, new_file)
                print("WORKED")	

# For Windows Users
# location = r'C:\Users\USER\Downloads'

# For Unix Users
location = r'/Users/user/Documents/Songs'

rename_mp3_files(location)
