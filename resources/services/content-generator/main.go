/*########################################################################
#
#     (   )
#  (   ) (
#   ) _   )
#    ( \_
#  _(_\ \)__
# (____\___))
#
# BIG FAT WARNING:
#
# This is a shit code. Don't learn anything from it. It's supposed to work
# and be very easy to understand. Nothing more, nothing less.
#
# golearnistio: content-generator
#
#   A dummy service pretending to generate some content fetched by
#	various components
#
########################################################################*/

package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"os"
	"strings"
	"time"
)

type HttpResp struct {
	Status string
}

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
	http.HandleFunc("/generate-bs", bs_generator_handler)
	log.Fatal(http.ListenAndServe("0.0.0.0:8003", nil))
}

func bs_generator_handler(w http.ResponseWriter, r *http.Request) {
	// this is a secured endpoint, let's verify session token
	if !verify_request_token(r) {
		log.Println("Unauthorized request")
		error_401_handler(w)
		return
	}

	w.Header().Set("Content-Type", "application/json; charset=utf-8")
	if r.Method == "GET" {
		switch bs_type := r.URL.Query().Get("bs-type"); bs_type {
		case "1":
			bs_content := generate_bs_content_1()
			w.WriteHeader(http.StatusOK)
			w.Write([]byte(
				fmt.Sprintf("{\"content\": \"%s\"}", bs_content),
			))
		default:
			log.Printf("404: wrong bs-type: %s", bs_type)
			error_404_handler(w, "no-content-for-this-bs-type")
			return
		}
	} else {
		error_405_handler(w)
		return
	}
}

func generate_bs_content_1() string {
	// TODO: connecting to DBs, cache, queue
	// for now let's just pretend we do something
	time.Sleep(150 * time.Millisecond)
	return "some content"
}

func verify_request_token(r *http.Request) bool {
	// send sync request to auth-service and verify session token sent
	// in Authorization: Bearer token

	reqToken := r.Header.Get("Authorization")
	if reqToken == "" {
		return false
	}

	splitToken := strings.Split(reqToken, " ")
	if len(splitToken) < 2 {
		return false
	}

	client := http.Client{
		Timeout: 1 * time.Second,
	}

	authServiceURL := os.Getenv("ISTIO_SVC_auth_service")+"/verify-session-token?token="+splitToken[1]
	req, err := client.Get(authServiceURL)
	if err != nil {
		return false
	}

	if req.StatusCode == http.StatusOK {
		defer req.Body.Close()

		var req_status = new(HttpResp)
		err := json.NewDecoder(req.Body).Decode(req_status)
		if err != nil {
			return false
		}
		if strings.ToUpper(req_status.Status) == "AUTHORIZED" {
			return true
		}
	}
	return false
}

func test_services_conns_handler(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json; charset=utf-8")
	var failed_services []string

	if r.Method == "GET" {
		for _, envvar := range os.Environ() {
			_envvar := strings.SplitN(envvar, "=", 2)
			if strings.HasPrefix(_envvar[0], "ISTIO_SVC_") {
				if !verify_service_connectivity(_envvar[1]) {
					failed_services = append(failed_services, _envvar[0])
				}
			}
		}

		// TODO: add verification of DBs + cache + queue connections

		if len(failed_services) > 0 {
			w.WriteHeader(500)
			connstatus := ConnStatusFailStruct{
				ConnStatusFail: strings.Join(failed_services, ","),
			}
			json.NewEncoder(w).Encode(connstatus)
		} else {
			w.WriteHeader(http.StatusOK)
			connstatus := StatusStruct{Status: "OK"}
			json.NewEncoder(w).Encode(connstatus)
		}
	} else {
		error_405_handler(w)
		return
	}
}

func verify_service_connectivity(svc_url string) bool {
	client := http.Client{
		Timeout: 1 * time.Second,
	}

	req, err := client.Get(svc_url)
	if err != nil {
		return false
	}

	if req.StatusCode == http.StatusOK {
		defer req.Body.Close()

		var req_status = new(HttpResp)
		err := json.NewDecoder(req.Body).Decode(req_status)
		if err != nil {
			return false
		}

		if strings.ToUpper(req_status.Status) == "OK" {
			return true
		}
		return false
	}

	return false
}

func status_handler(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json; charset=utf-8")
	if r.Method == "GET" {
		w.WriteHeader(http.StatusOK)

		status := StatusStruct{Status: "OK"}
		json.NewEncoder(w).Encode(status)
	} else {
		error_405_handler(w)
		return
	}
}

func error_404_handler(w http.ResponseWriter, desc_sl ...string) {
	desc := "404 not found"
	if len(desc_sl) > 0 {
		desc = strings.Join(desc_sl, "")
	}
	msg := fmt.Sprintf("{\"status\": \"%s\"}", desc)
	w.WriteHeader(http.StatusNotFound)
	w.Write([]byte(msg))
}

func error_401_handler(w http.ResponseWriter) {
	w.WriteHeader(http.StatusUnauthorized)
	w.Write([]byte(`{"status": "unauthorized"}`))
}

func error_405_handler(w http.ResponseWriter) {
	w.WriteHeader(http.StatusMethodNotAllowed)
	w.Write([]byte(`{"status": "method-not-allowed"}`))
}