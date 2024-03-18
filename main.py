import cmd
import random
import os
import requests


class TcUpload(cmd.Cmd):
    def create_url_and_curl(self, path, url, url_suffix, token):
        files_folder = path
        files_in_folder = os.listdir(files_folder)
        upload_url = url
        file_count = len(
            [name for name in os.listdir(files_folder) if os.path.isfile(os.path.join(files_folder, name))])
        print("Starting upload...")
        for i in range(file_count):
            file_id = random.randint(0, 1000000)
            suffix = url_suffix + "?id=" + str(file_id)
            all_url = upload_url + suffix
            files = {'upload_file': open(path + files_in_folder[i], 'rb')}
            headers = {'Authorization': 'Bearer ' + token}
            x = requests.post(all_url, data=None, files=files, json=None, headers=headers)
            if x == '200' or x == '201':
                print(str(x.status_code) + ' The file uploaded successfully')
            else:
                print(str(x.status_code) + ' The file failed to upload')
        i += 1
        requests.session().close()


if __name__ == '__main__':

    print("***Welcome to Trustification file uploader tool!***")
    path = input("Please enter the path to upload your SBOM or CSAF files from: ")  # Enter the files' path
    url = input("Please enter the server URL to upload the files to: ")   # Enter the remote server URL to upload files
    url_suffix = input("Please enter the URL suffix for your upload i.e. /api/v1/sbom or /api/v1/vex: ") # Enter suffix
    token = input("Please enter the bearer token: ")  # Enter the bearer token of Trustification api server
    TcUpload().create_url_and_curl(path, url, url_suffix, token)
