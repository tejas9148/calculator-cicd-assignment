
import json

from app import add, subtract, multiply

def lambda_handler(event, context):
    try:
        if isinstance(event, str):
            event = json.loads(event)

        if not isinstance(event, dict):
            raise ValueError("Event must be a JSON object")

        operation = event.get("operation")
        a = event.get("a")
        b = event.get("b")

        operations = {
            "add": add,
            "subtract": subtract,
            "multiply": multiply,
        }

        if operation not in operations:
            return {
                "statusCode": 400,
                "body": json.dumps({
                    "error": "Operation must be add, subtract, or multiply"
                }),
            }

        result = operations[operation](a, b)

        return {
            "statusCode": 200,
            "body": json.dumps({
                "operation": operation,
                "a": a,
                "b": b,
                "result": result,
            }),
        }

    except (TypeError, ValueError, json.JSONDecodeError) as exc:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": str(exc)}),
        }
