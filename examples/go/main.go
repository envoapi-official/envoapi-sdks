package main

import (
	"context"
	"encoding/json"
	"fmt"
	"log"
	"os"

	"github.com/envoapi-official/envoapi-sdks/go"
)

func main() {
	options := []envoapi.Option{}
	if base := os.Getenv("ENVOAPI_BASE_URL"); base != "" {
		options = append(options, envoapi.WithBaseURL(base))
	}
	client, err := envoapi.NewClient(options...)
	if err != nil {
		log.Fatal(err)
	}
	username := os.Getenv("ENVOAPI_USERNAME")
	if username == "" {
		username = "alice"
	}
	result, err := client.Profiles.GetPosts(context.Background(), envoapi.GetProfilePostsParams{Username: username})
	if err != nil {
		log.Fatal(err)
	}
	body, err := json.Marshal(result.Body)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(string(body))
}
