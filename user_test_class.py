import unittest
import pymongo

class TestQuizApp(unittest.TestCase):
    def setUp(self):
        # Set up a connection to MongoDB
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.client["quiz_app_db"]  # Replace with your database name
        self.users_collection = self.db["users"]  # Collection for user data

    def tearDown(self):
        # Close the MongoDB connection
        self.client.close()

    def test_signup(self):
        # Simulate user signup
        new_user = {"username": "testuser", "password": "testpassword"}
        self.users_collection.insert_one(new_user)

        # Verify that the user was added successfully
        count = self.users_collection.count_documents({})
        self.assertEqual(count, 1)

    def test_login(self):
        # Simulate user login
        user_credentials = {"username": "testuser", "password": "testpassword"}
        user = self.users_collection.find_one(user_credentials)
        self.assertIsNotNone(user)

    def test_invalid_login(self):
        # Attempt login with invalid credentials
        invalid_credentials = {"username": "nonexistentuser", "password": "wrongpassword"}
        user = self.users_collection.find_one(invalid_credentials)
        self.assertIsNone(user)

if __name__ == "__main__":
    unittest.main()
