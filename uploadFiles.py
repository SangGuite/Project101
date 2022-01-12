import dropbox
import os

from dropbox.files import WriteMode

class TransferData:
    def __init__(self,accessToken):
        self.accessToken = accessToken

    def upload_file(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.accessToken)
        for root, dirs, files in os.walk(file_from):
            for fileName in files:
                local_path = os.path.join(root,fileName)
                relative_path = os.path.relpath(local_path,file_from)
                dropbox_path = os.path.join(file_to,relative_path)
                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
    accessToken = 'sl.A__LWYJj1dysYfAwqvkEo14vnUEH7z-et15wIwB6hvPJRmYNrjsdNWVMp5izuJvUbNth0bCYpUYmXIBktATnD9rUMBrZZKKBJ929Ak7pUas0TIeTMBvx49bWd5vwvExdbXbR0ig'
    transferData = TransferData(accessToken)

    file_from = 'C:/Users/Sang/Cloud Storage/FolderA/trial.txt'
    file_to = '/MuanhlunsangGuiteBackupApp/trial.txt'

    transferData.upload_file(file_from,file_to)
    print("The file has moved.")

if __name__ == '__main__':
    main()