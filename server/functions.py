def process_request(request):
    method = request.get("method")
    params = request.get("params", [])

    if method == "say_hello":
        return {"result": f"Hello, {params[0]}!"}
    elif method == "add_numbers":
        return {"result": sum(params)}
    else:
        return {"error": "Method not found"}
