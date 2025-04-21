from flask import Flask, request, jsonify
from nba_api.stats.static import players

app = Flask(__name__)

@app.route('/search', methods=['GET'])
def search_player():
    query = request.args.get('name', '').lower()
    if not query:
        return jsonify([])

    all_players = players.get_players()
    matches = [p for p in all_players if query in p['full_name'].lower()]
    return jsonify(matches)

if __name__ == '__main__':
    app.run(debug=True)
