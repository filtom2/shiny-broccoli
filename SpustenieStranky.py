import webbrowser
import time
socialMedia = ["www.instagram.com", "www.youtube.com"]
def open_tabs(url_list):
    for element in url_list:
        webbrowser.open_new_tab(element)
def main():
    webbrowser.open("www.facebook.com", new=0, autoraise=False)
    time.sleep(3)
    open_tabs(socialMedia)
main()