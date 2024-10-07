from flask import Flask, request, jsonify
import requests
import json
from langchain_community.llms import Ollama

app = Flask(__name__)

cached_llm = Ollama(model="llama3.2:3b")

@app.route('/connect_ollama',methods=["POST"])
def connect_ollama():
    try:
        #get data from the fronted post request
        data = request.json
        print("data=====",data)

        #extract necessary fields from the data if needed
        user_input = data.get("user_input")
        print(user_input)
        print(type(user_input))

        if not user_input:
            return jsonify({"error":"user input is required"}),400

        response = cached_llm.invoke(user_input)
        print(response)
        # print(response.status_code)
        return json.dumps(response)

    except Exception as e:
        return jsonify({"error":str(e)})


if __name__ == "__main__":
    app.run(debug=True)
