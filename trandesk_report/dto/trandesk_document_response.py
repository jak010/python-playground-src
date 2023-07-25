from __future__ import annotations

from dataclasses import dataclass
from typing import List, TypedDict
import requests


@dataclass
class TranDeskDocumentResponse:
    info: dict
    item: list[dict]


class TranDeskDocumentContent:
    def __init__(self, response: requests.Response):
        self.data = response.json()

    @property
    def info(self) -> TranDeskDocumentInfo:
        return TranDeskDocumentInfo(**self.data['info'])

    @property
    def item(self) -> List[TranDeskDocumentItem]:
        _obj = []
        for item in self.data['item']:
            trandesk_document_item = TranDeskDocumentItem(**item)
            [TranDeskDocumentItemMeta(**each) for each in trandesk_document_item.item]

            _obj.append(trandesk_document_item)
        return _obj


@dataclass
class TranDeskDocumentInfo:
    _postman_id: str
    name: str
    description: str
    schema: str
    toc: list
    owner: str
    collectionId: str
    publishedId: str
    public: bool
    customColor: dict
    publishDate: str


@dataclass
class TranDeskDocumentItem:
    _postman_id: str
    id: str
    name: str
    description: str
    item: List[TranDeskDocumentItemMeta]


@dataclass
class TranDeskDocumentItemMeta(TypedDict):
    id: str
    name: str
    protocolProfileBehavior: dict
    request: TranDeskDocumentItemMetaRequest
    response: list
    _postman_id: str


class TranDeskDocumentItemMetaRequest(TypedDict):
    auth: dict
    description: str
    header: list[dict]
    method: str
    url: str
    urlObject: dict


"""TranDeskDocumentItemMeta
{'_postman_id': '',
 'id': '',
 'name': '',
 'protocolProfileBehavior': {'disableBodyPruning': True},
 'request': {'auth': {'basic': {'basicConfig': [{'key': '',
                                                 'value': ''},
                                                {'key': '',
                                                 'value': ''}]},
                      'isInherited': False,
                      'type': 'basic'},
             'description': ' '
                            '',
             'header': [{'key': '',
                         'type': '',
                         'value': ''}],
             'method': '',
             'url': '',
             'urlObject': {'host': [''],
                           'path': [''],
                           'query': [],
                           'variable': []}},
 'response': [{'_postman_previewlanguage': 'json',
               'body': {},
               'code': 200,
               'cookie': [],
               'header': [{'key': 'Content-Length', 'value': '1192'},
                          {'key': 'Content-Type', 'value': 'application/json'},
                          {'key': 'Date',
                           'value': 'Mon, 03 Jul 2023 10:13:35 GMT'},
                          {'key': 'Server', 'value': 'Kestrel'},
                          {'key': 'X-Frame-Options', 'value': 'SAMEORIGIN'},
                          {'key': 'X-Content-Type-Options', 'value': 'nosniff'},
                          {'key': 'X-XSS-Protection', 'value': '1; mode=block'},
                          {'key': 'Strict-Transport-Security',
                           'value': 'max-age=63072000; includeSubdomains; '
                                    'preload'},
                          {'key': 'Permissions-Policy',
                           'value': 'geolocation=(self), microphone=()'},
                          {'key': 'Referrer-Policy', 'value': 'no-referrer'}],
               'id': '',
               'name': '',
               'originalRequest': {'header': [{'key': '',
                                               'type': 'text',
                                               'value': ''}],
                                   'method': '',
                                   'url': ''},
               'responseTime': None,
               'status': 'OK'},
              {'_postman_previewlanguage': 'json',
               'body': '{\n'
                       '    "id": "",\n'
                       '    "code": ,\n'
                       '    "status": "",\n'
                       '    "title": "",\n'
                       '    "description": "",\n'
                       '    "link": '
                       '"",\n'
                       '    "timestamp": ""\n'
                       '}',
               'code': 400,
               'cookie': [],
               'header': [{'key': 'Content-Length', 'value': '324'},
                          {'key': 'Content-Type', 'value': 'application/json'},
                          {'key': 'Date',
                           'value': 'Mon, 03 Jul 2023 10:12:51 GMT'},
                          {'key': 'Server', 'value': 'Kestrel'},
                          {'key': 'X-Frame-Options', 'value': 'SAMEORIGIN'},
                          {'key': 'X-Content-Type-Options', 'value': 'nosniff'},
                          {'key': 'X-XSS-Protection', 'value': '1; mode=block'},
                          {'key': 'Strict-Transport-Security',
                           'value': 'max-age=63072000; includeSubdomains; '
                                    'preload'},
                          {'key': 'Permissions-Policy',
                           'value': 'geolocation=(self), microphone=()'},
                          {'key': '', 'value': ''}],
               'id': '',
               'name': '',
               'originalRequest': {'header': [{'key': '',
                                               'type': '',
                                               'value': ''}],
                                   'method': '',
                                   'url': ''},
               'responseTime': None,
               'status': ''}]}
"""
