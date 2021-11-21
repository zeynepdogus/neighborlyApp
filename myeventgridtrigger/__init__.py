import logging
import json
import azure.functions as func

def main(req: func.HttpRequest, sendGridMessage: func.Out[str]) -> func.HttpResponse:

    value = "Sending message from my Azure Functions HTTP Trigger"

    message = {
        "personalizations": [ {
          "to": [{
            "email": "doguszeynep@gmail.com"
            }]}],
        "subject": "Test",
        "content": [{
            "type": "text/plain",
            "value": value }]}

    sendGridMessage.set(json.dumps(message))
    return func.HttpResponse("Message successfully sent.")