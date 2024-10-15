from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import (
    extend_schema_view,
    extend_schema,
    OpenApiExample,
    OpenApiResponse
)

from station_api.schemas.examples.common_responses import (
    unauthorized_response,
    forbidden_response,
)
from station_api.schemas.examples.orders import (
    order_list_json,
    order_create_request_json,
    order_create_response_json,
    error_400_empty_fields,
    error_400_invalid_place
)
from station_api.serializers import OrderListSerializer, OrderSerializer


order_list_create_schema = extend_schema_view(
    list=extend_schema(
        description="Retrieve list of authorised user orders",
        examples=[
            OpenApiExample(
                name="Order list example",
                value=order_list_json
            )
        ],
        responses={
            200: OrderListSerializer(many=True),
            401: unauthorized_response
        },
    ),
    create=extend_schema(
        description="Create a new order",
        request=OrderSerializer(),
        examples=[
            OpenApiExample(
                name="Order request example",
                value=order_create_request_json,
                request_only=True,
            ),
            OpenApiExample(
                name="Order response example",
                value=order_create_response_json,
                response_only=True,
            )
        ],
        responses={
            201: OrderSerializer(),
            400: OpenApiResponse(
                description="Bad request, invalid data",
                response=OpenApiTypes.OBJECT,
                examples=[
                    OpenApiExample(
                        name="Empty required fields example",
                        value=error_400_empty_fields,
                        response_only=True,
                    ),
                    OpenApiExample(
                        name="Not unique (cargo, seat, trip) example",
                        value=error_400_invalid_place,
                        response_only=True,
                    )
                ]
            ),
            401: unauthorized_response,
            403: forbidden_response,
        }
    )
)