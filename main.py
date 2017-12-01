from downloader import Downloader
from extractor import Extractor

# https://github.com/kennethreitz/clint cool shit \Q-Q/
from clint.textui import colored, puts

if __name__ == "__main__":
    dl = Downloader()
    ex = Extractor()

    puts(colored.green("getting video keys."))
    puts(colored.green(ex.get_viewkeys(dl.get("https://pornhub.com"))))
    puts(colored.green("starting to download videos."))


