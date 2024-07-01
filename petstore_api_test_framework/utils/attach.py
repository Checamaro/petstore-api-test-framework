import json

import allure
import logging
from allure_commons.types import AttachmentType
from requests import Response


def response_attaching(response: Response):

    allure.attach(
        body=response.request.url,
        name="Request url",
        attachment_type=AttachmentType.TEXT,
    )

    allure.attach(
            body=json.dumps(response.request.body, indent=4, ensure_ascii=True),
            name="Request body",
            attachment_type=AttachmentType.JSON,
            extension="json",
    )

    allure.attach(
            body=json.dumps(response.json(), indent=4, ensure_ascii=True),
            name="Response body",
            attachment_type=AttachmentType.JSON,
            extension="json",
    )
    allure.attach(
        body=str(response.status_code),
        name="Response status code",
        attachment_type=AttachmentType.TEXT,
    )


def logging_response(response):
    logging.info(response.request.url)
    logging.info(response.request.body)
    logging.info(response.status_code)
    logging.info(response.text)
