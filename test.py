import unittest
from unittest.mock import MagicMock
from enum import Enum
from landmark_point import LandmarkPoint

# Assuming the above code is in a module named 'metaring_module'
# from metaring_module import Metaring, LandmarkPoint

class TestMetaring(unittest.TestCase):

    def setUp(self):
        # Prepare a mock result object, with a nested structure
        self.mock_result = MagicMock()
        self.mock_result.face_landmarks = MagicMock()
        self.mock_result.face_landmarks.landmark = [MagicMock() for _ in range(500)]  # Simulate 500 landmarks

        # Simulate some landmark positions (x, y, z) for testing
        self.mock_result.face_landmarks.landmark[356].x = 0.5
        self.mock_result.face_landmarks.landmark[356].y = 0.6
        self.mock_result.face_landmarks.landmark[356].z = 0.7

        self.mock_result.face_landmarks.landmark[109].x = 0.1
        self.mock_result.face_landmarks.landmark[109].y = 0.2
        self.mock_result.face_landmarks.landmark[109].z = 0.3

        # Define a sample points dictionary using `LandmarkPoint` Enum
        self.points = {
            LandmarkPoint.temple_R_B: 356,  # Maps to landmark index 356
            LandmarkPoint.forehead_R: 109,  # Maps to landmark index 109
        }

    def test_get_position(self):
        # Call the get_position method
        positions = LandmarkPoint.get_position(self.mock_result, self.points)

        # Check the correctness of returned positions
        self.assertIn(LandmarkPoint.temple_R_B, positions)
        self.assertIn(LandmarkPoint.forehead_R, positions)

        # Assert that the correct coordinates are returned for temple_R_B (index 356)
        self.assertEqual(positions[LandmarkPoint.temple_R_B], (0.5, 0.6, 0.7))

        # Assert that the correct coordinates are returned for forehead_R (index 109)
        self.assertEqual(positions[LandmarkPoint.forehead_R], (0.1, 0.2, 0.3))

    def test_get_position_empty_points(self):
        # Test when the points dictionary is empty
        positions = LandmarkPoint.get_position(self.mock_result, {})
        self.assertEqual(positions, {})  # Should return an empty dictionary

    def test_get_position_invalid_landmark(self):
        # Test with an invalid landmark index (out of bounds)
        self.mock_result.face_landmarks.landmark = [MagicMock() for _ in range(5)]  # Only 5 landmarks now

        # Define points with an out-of-bounds index
        invalid_points = {
            LandmarkPoint.temple_R_B: 356,  # 356 is out of bounds
        }

        with self.assertRaises(IndexError):
            LandmarkPoint.get_position(self.mock_result, invalid_points)

    def test_get_position_missing_face_landmarks(self):
        # Test when face_landmarks is missing
        mock_result_no_landmarks = MagicMock()
        mock_result_no_landmarks.face_landmarks = None

        with self.assertRaises(AttributeError):
            LandmarkPoint.get_position(mock_result_no_landmarks, self.points)


if __name__ == '__main__':
    unittest.main()
