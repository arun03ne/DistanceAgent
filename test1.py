from flask import Flask, request, jsonify
from graph import Graph  # Import from the graph.py file

# Flask application
app = Flask(__name__)

# Initialize graph and add edges
graph = Graph()
graph.add_edge('A', 'B', 1)
graph.add_edge('A', 'C', 4)
graph.add_edge('B', 'C', 2)
graph.add_edge('B', 'D', 5)
graph.add_edge('C', 'D', 1)

@app.route('/find-path', methods=['GET'])
def find_path():
    start = request.args.get('start')
    end = request.args.get('end')
    path, distance = graph.dijkstra(start, end)
    if path:
        return jsonify({'path': path, 'distance': distance}), 200
    else:
        return jsonify({'error': 'No path found'}), 404

if __name__ == '__main__':
    app.run(debug=True)