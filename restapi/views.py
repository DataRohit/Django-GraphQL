from django.views.decorators.http import require_http_methods
from django.http import JsonResponse


@require_http_methods(["GET"])
def RestAPIHome(request):
    return JsonResponse(
        {
            "data": {
                "message": "Welcome to Django-GraphQL Home URL!",
                "owner": "DataRohit",
            }
        },
        status=200,
    )
