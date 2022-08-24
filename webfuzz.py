import argparse
from typing import Dict
import requests

class main:
    url: str = ""
    cookies: str = ""
    method: str = "GET"
    body: str | Dict[str, str] = ""
    response = requests.Response
    hide_status_code: str = ""
    min_size: int = 0
    payload: str = ""
    headers = {}

    def init(self, url: str, session: bool, method: str):
        if url:
            self.url = url
        if session:
            self.use_session = session
            self.session = requests.Session()
        if method:
            self.method = method
        print("FUZZING TOOL")
        while True:
            menue = input().strip()
            if menue == "help" or menue == "":
                print("show options")
                print("show response")
                print("set url URL")
                print("set method")
                print("set cookies COOKIESTRING")
                print("hide status code")
            if menue == "show options":
                print(f"url = {self.url}")
                print(f"method = {self.method}")
                print(f"use single sessions = {self.use_session}")
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
                self.headers = {"Cookie": self.cookies}
            if "set cookie" in menue:
                cookie = menue.replace("set cookies", "").strip()
                self.headers = {"Cookie": self.cookies + "; " + cookie}
            if "set body" in menue:
                self.body = menue.replace("set body", "").strip()
            if "set form" in menue:
                body_input = menue.replace("set form", "").strip()
                body_array = body_input.split("&")
                self.body = {}
                for body in body_array:
                    body_inputs = body.split("=")
                    self.body[body_inputs[0]] = body_inputs[1]
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
                            if session:
                                self.response = self.session.request(self.method, url, headers=self.headers, data=self.body)
                            else:
                                self.response = requests.request(self.method, url, headers=self.headers, data=self.body)
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
        "-method", type=str, default="GET", help="Set HTTP method"
    )
    parser.add_argument(
        "-session", type=bool, default=True, help="Use single HTTP session"
    )
    parser.add_argument(
        "-url", type=str, default="", help="set url URL"
    )
    args = parser.parse_args()
    input_file = args.i
    method = args.method
    url = args.url
    session = args.session
    main().init(url, session, method)