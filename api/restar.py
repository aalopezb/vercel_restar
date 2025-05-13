import json

def handler(request):
    try:
        
        a = float(request.args.get("a", 0))
        b = float(request.args.get("b", 0))
        resultado = a - b
        return json.dumps({"resultado": resultado}), 200
    except Exception as e:
        return json.dumps({"error": str(e)}), 400