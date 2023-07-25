import requests

from dto.trandesk_document_response import TranDeskDocumentContent


class HttpRequest:

    def __init__(self, endpoint: str):
        self.url = "https://documenter.gw.postman.com"
        self.endpoint = endpoint

    def execute(self) -> requests.Response:
        return requests.get(self.url + self.endpoint)


if __name__ == '__main__':
    http_request = HttpRequest(endpoint="")

    trandesk_document_content = TranDeskDocumentContent(response=http_request.execute())
    for row in trandesk_document_content.item:
        for inner_item in row.item:
            print(inner_item['name'], inner_item['request']['url'])
