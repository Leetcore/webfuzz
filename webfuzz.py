import argparse
import requests

class main:
    url: str = ""
    cookies: str = ""
    method: str = "GET"
    response = requests.Response
    hide_status_code: str = ""
    min_size: int = 0
    payload: str = ""

    def init(self, url: str):
        if url:
            self.url = url
        print("FUZZING TOOL")
        while True:
            menue = input().strip().lower()
            if menue == "help":
                print("show options")
                print("show response")
                print("set url URL")
                print("set method")
                print("set cookies COOKIESTRING")
                print("hide status code")
            if menue == "show options":
                print(f"url = {self.url}")
                print(f"cookies = {self.cookies}")
                print(f"hide status code = {self.hide_status_code}")
                print(f"hide min size = {self.min_size}")
            if menue == "show response":
                print(f"method = {self.method}")
                print(f"url = {self.response.url}")
                print(f"headers = {str(self.response.headers)}")
                print(f"body = {self.response.text}")
            if "set url" in menue:
                self.url = menue.replace("set url", "").strip()
            if "set cookies" in menue:
                self.cookies = menue.replace("set cookies", "").strip()
            if "set method" in menue:
                self.method = menue.replace("set method", "").strip()
            if "hide status code" in menue:
                self.hide_status_code = menue.replace("hide status code", "").strip()
            if "hide min size" in menue:
                self.min_size = int(menue.replace("hide min size", "").strip())
            if "reset hide" in menue:
                self.hide_status_code = ""
            if menue == "run":
                print(f"status\t\tsize\t\tpayload")
                with open(input_file, "r") as file:
                    try:
                        for line in file.readlines():
                            line = line.strip()
                            self.payload = line
                            url = self.url.replace("FUZZ", line)
                            self.response = requests.request(self.method, url)
                            self.show_response()
                    except KeyboardInterrupt:
                        print("\n")
            
    def show_response(self):
        if str(self.response.status_code) not in self.hide_status_code and self.min_size < len(str(self.response.text)):
            print(f"{self.response.status_code}\t\t{len(str(self.response.text))}\t\t{self.payload}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Fuzz web requests with python"
    )
    parser.add_argument(
        "-i", type=str, default="./input.txt", help="Path to input file. Default: input.txt"
    )
    parser.add_argument(
        "-url", type=str, default="", help="set url URL"
    )
    args = parser.parse_args()
    input_file = args.i
    url = args.url
    main().init(url)