from flask import Flask, jsonify, request

app = Flask(__name__)

inventario = [
    {"hostname": "Dist-SW02", "ip": "10.0.0.2", "status": "down"},
    {"hostname": "Access-SW03", "ip": "10.0.0.3", "status": "up"},
    {"hostname": "Edge-R01", "ip": "172.16.1.1", "status": "down"},
]

@app.route("/")
def inicio():
    return jsonify({
        "mensaje": "API de inventario de red",
        "endpoints": [
            "GET  /inventario",
            "GET  /inventario?status=up|down",
            "GET  /inventario/<hostname>",
            "POST /inventario",
        ],
    })

@app.route("/inventario", methods=["GET"])
def listar_dispositivos():
    status = request.args.get("status")
    if status:
        filtrados = [d for d in inventario if d["status"] == status]
        return jsonify(filtrados), 200
    return jsonify(inventario), 200

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000, debug=True)

