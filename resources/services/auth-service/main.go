package main

import (
	"encoding/json"
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
	http.HandleFunc("/test-services-conns", test_services_conns_handler)
	log.Fatal(http.ListenAndServe("0.0.0.0:8002", nil))
}

func test_services_conns_handler(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json; charset=utf-8")
	var failed_services []string

	if r.Method == "GET" {
		for _, envvar := range os.Environ() {
			_envvar := strings.SplitN(envvar, "=", 2)
			println(_envvar[0])
			if strings.HasPrefix(_envvar[0], "ISTIO_SVC_") {
				if !verify_service_connectivity(_envvar[1]) {
					failed_services = append(failed_services, _envvar[0])
				}
			}
		}

		if len(failed_services) > 0 {
			w.WriteHeader(500)
			connstatus := ConnStatusFailStruct{
				ConnStatusFail: strings.Join(failed_services, ","),
			}
			json.NewEncoder(w).Encode(connstatus)
		} else {
			w.WriteHeader(http.StatusOK)
			connstatus := StatusStruct{Status: "ok"}
			json.NewEncoder(w).Encode(connstatus)
		}
	} else {
		error_404_handler(w)
	}
}

func verify_service_connectivity(svc_url string) bool {
	_, err := http.Get(svc_url)
	if err != nil {
		return true
	}

	return false
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
