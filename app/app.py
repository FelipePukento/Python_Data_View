from flask import Flask, jsonify
import psycopg2
import threading
import time
import random

app = Flask(__name__)

# Conexión a la base de datos
conn = psycopg2.connect(
    dbname='test_db',
    user='postgres',
    password='password',
    host='db',  # nombre del servicio en docker-compose
    port='5432'
)
cur = conn.cursor()

# Función para agregar datos aleatorios a la base de datos cada segundo
def add_random_data():
    while True:
        name = f'Random {random.randint(1, 1000)}'
        value = random.uniform(1, 100)
        cur.execute("INSERT INTO data (name, value) VALUES (%s, %s)", (name, value))
        conn.commit()
        print(f"Inserted: {name}, {value}")
        time.sleep(1)

# Iniciar el hilo para agregar datos aleatorios
thread = threading.Thread(target=add_random_data)
thread.start()

@app.route('/')
def index():
    cur.execute('SELECT id, name, value FROM data')
    rows = cur.fetchall()
    return jsonify(rows)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
