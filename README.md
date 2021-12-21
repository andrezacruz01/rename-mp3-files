# rename-mp3-files

This script renames .mp3 filenames with the [www.slider.kz] extension.


#### If you want to use another folder, change:

For Windows users:
````
location = r'C:\Users\USER\Downloads'
````

For Unix users:
````
location = r'/Users/user/Documents'
`````

#### If you want to change the extension:

`````
new_name = m_file.replace(" [www.slider.kz]", "")
``````

#### If you want to change the file extension:

`````
m_file.endswith('.mp3')
``````

#### To run the script:

Go to the folder where the script is located and run (use the terminal or cmd):

```
python script_rename.py
````

*Note: This is a v1 script*

