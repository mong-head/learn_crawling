from google_images_download import google_images_download   #importing the library

response = google_images_download.googleimagesdownload()   #class instantiation

arguments = {"keywords":"Polar bears,baloons,Beaches","limit":20,"print_urls":True}   #creating list of arguments
paths = response.download(arguments)   #passing the arguments to the function
print(paths)   #printing absolute paths of the downloaded image

'''
여러분! pip uninstall google-_images_download 쳐서 삭제하고
pip install git+https://github.com/Joeclinton1/google-images-download.git 
이걸로 하세요! 이게 최신버전입니다.

주의사항 : 
1. 실행시킬 python 스크립트 파일을  google-images-download 디렉토리에 넣어두고 실행해야 한다는 점. 저 같은 경우 google.py 스크립트 파일이 아래 경로에 있는 것을 알 수 있습니다.
2. git이 설치돼어있어야 합니다.
'''