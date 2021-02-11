package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"os"
	"strings"
)

type StatusStruct struct {
	Status string `json:"status"`
}

type ConnStatusFailStruct struct {
	ConnStatusFail string `json:"connfail"`
}

func main() {
	http.HandleFunc("/", status_handler)
	http.HandleFunc("/status", status_handler)
	http.HandleFunc("/test-services-conns", status_handler)
	log.Fatal(http.ListenAndServe("0.0.0.0:8000", nil))
}

func test_services_conns_handler(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json; charset=utf-8")
	if r.Method == "POST" {
		for _, envvar := range os.Environ() {
			pair := strings.SplitN(e, "=", 2)
			fmt.Printf("%s: %s\n", pair[0], pair[1])
		}
		w.WriteHeader(http.StatusOK)
		connstatus := ConnStatusFailStruct{ConnStatusFail: "ok"}
		json.NewEncoder(w).Encode(connstatus)
	} else {
		error_404_handler(w)
	}
}
func status_handler(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json; charset=utf-8")
	if r.Method == "GET" {
		w.WriteHeader(http.StatusOK)
		// w.Write([]byte(`{"message": "hello world"}`))

		status := StatusStruct{Status: "ok"}
		json.NewEncoder(w).Encode(status)
	} else {
		error_404_handler(w)
	}
}

func error_404_handler(w http.ResponseWriter) {
	w.WriteHeader(http.StatusNotFound)
	w.Write([]byte(`{"status": "404 not found"}`))
}
