🌱- About Me
Hi, I’m @jems0812I a Server and Network Support Specialist with extensive experience in configuring and managing Mikrotik OS routers (v6 and v7). I am also a programmer with solid knowledge in SQL Server databases and programming languages such as Go, HTML, CSS, JavaScript, and Python. I am committed to continuous learning and implementing efficient technological solutions.
Skills
Server and Network Support
Configuration and administration of Mikrotik OS routers (v6 and v7)
Programming Languages
Go
HTML
CSS
JavaScript
Python
Database Management
SQL Server
Continuous Learning
Always striving to learn new technologies and improve my skills
Efficient Solutions
Focused on implementing efficient and effective technological solutions
print("Hello, World!")
package main

import "fmt"

func main() {
    fmt.Println("Hello, World!")
}

<!DOCTYPE html>
<html>
<head>
    <title>Hello World</title>
</head>
<body>
    <h1>Hello, World!</h1>
</body>
</html>

<?php
echo "Hello, World!";
?>

console.log("Hello, World!");


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
