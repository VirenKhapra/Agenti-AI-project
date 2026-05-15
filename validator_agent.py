import json

def validate_data(data):

    required_fields = [
        "customer_name",
        "transaction_id",
        "amount",
        "payment_method",
        "account_number",
        "transaction_date",
        "currency",
        "transaction_type",
        "merchant_name",
        "status"
    ]

    try:

        cleaned_data = (
            data.replace("```json", "")
                .replace("```", "")
                .strip()
        )

        parsed = json.loads(cleaned_data)

        # Ensure JSON is a list
        if not isinstance(parsed, list):

            return {
                "status": "invalid",
                "error": "Expected a JSON array"
            }

        missing_fields = []

        # Validate each transaction
        for transaction in parsed:

            for field in required_fields:

                if field not in transaction or transaction[field] == "":

                    missing_fields.append(field)

        if missing_fields:

            return {
                "status": "invalid",
                "missing_fields": list(set(missing_fields))
            }

        return {
            "status": "valid",
            "data": parsed
        }

    except Exception as e:

        return {
            "status": "invalid",
            "error": str(e)
        }
