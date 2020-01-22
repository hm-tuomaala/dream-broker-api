## Dream Broker api app
This is my implementation of Dream Brokers coding challenge  
You can analyze text input with api at: /analyze

# Usage example
Command:  

curl --header "Content-Type: application/json" \  
     --request POST \  
     --data '{"text":"hello 2 times  "}' \  
    https://mysuperawesomeapi.com/analyze  

will produce:  

{  
            "textLength":{"withSpaces":15,"withoutSpaces":11},  
            "wordCount":3,  
            "characterCount":[{"e":2},{"h":1},{"i":1},{"l":2},{"m":1},{"o":1},{"s":1},{"t":1}]  
}
