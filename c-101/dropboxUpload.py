import dropbox
class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):

        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'fQVOI-dBFWsAAAAAAAAAAWhOfaNyq0ICnwY0CMU7aroW8kyZTvZ6GhtkmJwYx9sy'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer - ")
    file_to = input("Enter the full path to upload to dropbox - ")

    # API v2
    transferData.upload_file(file_from, file_to)
    print("File has been moved. :)")

main()

