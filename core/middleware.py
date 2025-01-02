import time
import logging
from django.db import connection
from django.conf import settings

logger = logging.getLogger(__name__)

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()
        
        response = self.get_response(request)
        
        duration = time.time() - start_time
        
        # Log request details
        logger.info(
            f"Path: {request.path} | Method: {request.method} | "
            f"Duration: {duration:.2f}s | Status: {response.status_code}"
        )
        
        # Log database queries in debug mode
        if settings.DEBUG:
            queries = len(connection.queries)
            logger.debug(f"Number of queries: {queries}")
            
        return response 