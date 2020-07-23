import subprocess
import webbrowser
import sys

web_sites = [
    'https://github.com/users/KuligKamil/projects/1',
    'https://fastapi.tiangolo.com/tutorial/',
    'http://localhost:5050/browser/',
    'http://localhost:8000/docs',
    'http://localhost:8000/redoc'
]
if sys.platform == 'darwin':  # in case of OS X
    for url in web_sites:
        subprocess.Popen(['open', url])
else:
    for url in web_sites:
        webbrowser.open_new_tab(url)
