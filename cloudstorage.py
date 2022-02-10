import dropbox

class TransferData:

    def __init__(self, access_token):
        self.access_token = access_token
    
    def upload_file(self, file_from, file_to):
        dbx= dropbox.Dropbox(self.access_token)

        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = "sl.BBxpZC_ahamcFWyQkG9Kv4DmhQeRfDfCBVEwimhBhN8mml09upCeLJZJ7WoWIez8rbCgY1WAAlI1cwJB4BvJL-EUV9XOOIbczAaNSDDZi4qH9kJIMXP7daqFGZ0G6dsk3QwHMaE"
    transferData = TransferData(access_token)
    file_from = input("Enter the file path to transfer:")
    file_to = input("Enter the full path to upload the file to dropbox:")
    
    transferData.upload_file(file_from, file_to)
    print("File has been moved")

main()