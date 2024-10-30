import json
import os
from datetime import datetime
import pytz

class DatabaseHandler:
    def __init__(self, file_path="data.json", timezone="UTC"):
        self.file_path = file_path
        self.timezone = timezone
        # Ensure file exists and is initialized as an empty list if it doesn't
        if not os.path.exists(self.file_path):
            with open(self.file_path, "w") as file:
                json.dump([], file)  # Initialize with an empty list
    
    def _load_data(self):
        with open(self.file_path, "r") as file:
            data = json.load(file)
            # Ensure data is a list, convert if necessary
            if isinstance(data, dict):
                data = []  # Reset to an empty list if it's a dictionary
        return data
    
    def _save_data(self, data):
        with open(self.file_path, "w") as file:
            json.dump(data, file, indent=4)
    
    def add_question(self, question, answer):
        data = self._load_data()
        current_time = datetime.now(pytz.timezone(self.timezone)).isoformat()
        new_entry = {
            "ques": question,
            "ans": answer,
            "dateTime": current_time
        }
        data.append(new_entry)
        self._save_data(data)
    
    def remove_question(self, question):
        data = self._load_data()
        data = [entry for entry in data if entry["ques"] != question]
        self._save_data(data)
    
    def edit_question(self, question, new_answer):
        data = self._load_data()
        for entry in data:
            if entry["ques"] == question:
                entry["ans"] = new_answer
                entry["dateTime"] = datetime.now(pytz.timezone(self.timezone)).isoformat()
                break
        self._save_data(data)
    
    def get_answer(self, question):
        data = self._load_data()
        for entry in data:
            if entry["ques"] == question:
                return entry
        return None
    
    def list_all_questions(self):
        data = self._load_data()
        return [entry for entry in data]
