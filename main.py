from downloader import Downloader
from extractor import Extractor

# https://github.com/kennethreitz/clint cool shit \Q-Q/
from clint.textui import colored, puts

if __name__ == "__main__":
    dl = Downloader()
    ex = Extractor()
    url = "https://pornhub.com"

    puts(colored.green("getting video keys."))
    main_page = dl.get(url)
    viewkeys = ex.get_viewkeys(main_page)

    puts(colored.green("starting to download videos."))
