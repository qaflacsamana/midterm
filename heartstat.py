from flask import Flask, jsonify, request
app = Flask(__name__)
heartstat = [
    {
        "heart_id" : "1",
        "date" : ["November 20, 2023"],
        "heart_rate" : ["120/80"]
    }
]

@app.route('/Heart', methods=['Get'])
def getStat():
    return jsonify(heartstat)

@app.route('/Heart', methods=['Post'])
def addStat():
    add = request.get_json()
    heartstat.append(add)
    return{'id': len(heartstat)},200

@app.route('/Heart/<int:index>', methods=['Delete'])
def deleteStat(index):
    heartstat.pop(index)
    return 'Deleted', 200

if __name__ == '__main__':
    app.run()
