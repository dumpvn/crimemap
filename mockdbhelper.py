"""
a mock database does nothing.
"""

class MockDBHelper:
    def connect(self):
        pass
    
    def get_all_inputs(self):
        return []
    
    def add_input(self, data):
        pass
    
    def clear_all(self):
        pass
    
    def add_crime(self, category, date, latitude, longitude, description):
        pass

    def get_all_crimes(self):
        return [{
            '': '',
            'latitude': -33.301304,
            'longitude': 26.523355,
            'date': "2000-01-01",
            'category': "mugging",
            'description': "mock description"
        },
        ]
