import dropbox

access_token = 'sl.BGslZDsHAzSZoY7J9D_kW6pK_laqmXSOWeSJ4Sr5bbjscuzcN28SEu73NJ6WDjxdRH-NZXOtyWcPKXX2xVbaoScJyP8fI0z_Xht5ln81fI6f5csIn4LuZw-v7qC5QUlxkxEQdFASwxAH'
dbx = dropbox.Dropbox(access_token)

source = input("give the file name to import")
destination=input("give the file destination")


data=open(source,'rb').read()

dbx.files_upload(data,destination)
