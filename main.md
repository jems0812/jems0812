<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>About Me</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
            color: #333;
        }
        .container {
            max-width: 800px;
            margin: 20px auto;
            padding: 20px;
            background-color: #fff;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            font-size: 24px;
            margin-bottom: 20px;
            color: #2c3e50;
        }
        h2 {
            font-size: 20px;
            margin-top: 20px;
            color: #2c3e50;
        }
        p {
            margin-bottom: 10px;
        }
        ul {
            list-style-type: none;
            padding: 0;
        }
        ul li {
            margin-bottom: 10px;
            padding-left: 20px;
            position: relative;
        }
        ul li:before {
            content: "🌱";
            position: absolute;
            left: 0;
            color: #27ae60;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🌱- About Me</h1>
        <p>Hi, I’m <strong>@jems0812</strong>. I am a <strong>Server and Network Support Specialist</strong> with extensive experience in configuring and managing Mikrotik OS routers (v6 and v7). I am also a programmer with solid knowledge in SQL Server databases and programming languages such as Go, HTML, CSS, JavaScript, and Python. I am committed to continuous learning and implementing efficient technological solutions.</p>
        
        <h2>Skills</h2>
        <ul>
            <li><strong>Server and Network Support</strong></li>
            <li>Configuration and administration of Mikrotik OS routers (v6 and v7)</li>
            <li><strong>Programming Languages</strong></li>
            <ul>
                <li>Go</li>
                <li>HTML</li>
                <li>CSS</li>
                <li>JavaScript</li>
                <li>Python</li>
            </ul>
            <li><strong>Database Management</strong></li>
            <li>SQL Server</li>
            <li><strong>Continuous Learning</strong></li>
            <li>Always striving to learn new technologies and improve my skills</li>
            <li><strong>Efficient Solutions</strong></li>
            <li>Focused on implementing efficient and effective technological solutions</li>
        </ul>
    </div>
</body>
</html>



<!---
package main

import (
	"database/sql"
	"fmt"
	"log"
	"net/http"

	_ "github.com/lib/pq"
)

// Configuración de la base de datos
const (
	host     = "tu_host"
	port     = 5432
	user     = "tu_usuario"
	password = "tu_contraseña"
	dbname   = "tu_basedatos"
)

// Función principal
func main() {
	// Conectar a la base de datos
	psqlInfo := fmt.Sprintf("host=%s port=%d user=%s password=%s dbname=%s sslmode=disable",
		host, port, user, password, dbname)
	db, err := sql.Open("postgres", psqlInfo)
	if err != nil {
		log.Fatal(err)
	}
	defer db.Close()

	// Probar la conexión a la base de datos
	err = db.Ping()
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println("¡Conectado exitosamente a la base de datos!")

	// Configurar servidor HTTP
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		w.WriteHeader(http.StatusOK)
		fmt.Fprintln(w, "¡Bienvenido a mi servidor web en Go!")
	})
	fmt.Println("Iniciando servidor en :8080")
	log.Fatal(http.ListenAndServe(":8080", nil))
}

--->
