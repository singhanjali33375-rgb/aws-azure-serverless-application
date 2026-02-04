import logging
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    name = req.params.get('name', 'User')
    logging.info('Azure Function processed a request.')

    return func.HttpResponse(
        f"Hello {name}, this is an Azure Function response",
        status_code=200
    )
