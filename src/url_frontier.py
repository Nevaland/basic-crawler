from src.fetcher.fetcher import fetch

BOANNEWS_ALL_ARTICLE_URL = "https://www.boannews.com/media/t_list.asp"


class UrlFrontier:

    def __init__(self):
        self.url = []
        self.url.append(BOANNEWS_ALL_ARTICLE_URL)

    def run(self):
        for url in self.url:
            print(" [+] " + str(url))
            content = self._fetch(url)
            print(content)

    def _fetch(self, url):
        return fetch(url)

    def _parse(self, content):
        return content


if __name__ == "__main__":
    print("[*] Run Url Frontier")
    url_frontier = UrlFrontier()
    url_frontier.run()
