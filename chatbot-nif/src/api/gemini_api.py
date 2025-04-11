class GeminiAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.gemini.com/v1"

    def query_api(self, question):
        import requests

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        payload = {
            "question": question
        }
        
        response = requests.post(f"{self.base_url}/query", json=payload, headers=headers)
        
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": "Failed to get response from Gemini API"}