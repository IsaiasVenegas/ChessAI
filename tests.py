import unittest
from processing import *


class ProcessingTest(unittest.TestCase):
    def test_is_white_movement(self):
        self.assertEqual(check_color(0, 0), 1)

    def test_is_black_movement(self):
        self.assertEqual(check_color(1, 0), 2)

    def test_pawn_normal_movement(self):
        self.assertEqual(
            parse_special_move(0, "e4", 0),
            ("e4", 1)
        )

    def test_piece_normal_movement(self):
        self.assertEqual(
            parse_special_move(0, "Bc4", 0),
            ("Bc4", 1)
        )
    
    def test_pawn_promotion_movement(self):
        self.assertEqual(
            parse_special_move(0, "f8=Q", 0),
            ("f8", 1)
        )

    def test_check_movement(self):
        self.assertEqual(
            parse_special_move(0, "Bb4+", 0),
            ("Bb4", 1)
        )

    def test_mate_movement(self):
        self.assertEqual(
            parse_special_move(0, "Bd1#", 0),
            ("Bd1", 1)
        )

    def test_pawn_capture_movement(self):
        self.assertEqual(
            parse_special_move(0, "cxd5", 0),
            ("d5", 2)
        )

    def test_piece_capture_movement(self):
        self.assertEqual(
            parse_special_move(0, "Nxe5", 0),
            ("Ne5", 2)
        )

    def test_white_queenside_castling(self):
        self.assertEqual(
            parse_special_move(0, "O-O-O", 0),
            ("Rc1", 3)
        )

    def test_black_queenside_castling(self):
        self.assertEqual(
            parse_special_move(1, "O-O-O", 0),
            ("Rc8", 3)
        )

    def test_white_kingide_castling(self):
        self.assertEqual(
            parse_special_move(0, "O-O", 0),
            ("Rg1", 3)
        )

    def test_black_kingside_castling(self):
        self.assertEqual(
            parse_special_move(1, "O-O", 0),
            ("Rg8", 3)
        )

    def test_pawn_promotion_and_check_movement(self):
        self.assertEqual(
            parse_special_move(0, "f8=Q+", 0),
            ("f8", 1)
        )

    def test_pawn_capture_promotion_and_mate_movement(self):
        self.assertEqual(
            parse_special_move(0, "exf8=Q#", 0),
            ("f8", 2)
        )

    def test_is_pawn(self):
        self.assertEqual(parse_piece("f", 0), 1)

    def test_is_king(self):
        self.assertEqual(parse_piece("K", 0), 6)

    def test_column(self):
        self.assertEqual(parse_column("a", 0), 1)

    def test_parse_movements(self):
        # Includes Rad1 movement with desambiguation notation
        self.assertEqual(parse_movements(
            ["d4",    "d5",   "Nf3",   "Nxe5",  "Rd1",    "Rad1",  "f8=Q",  "f8=Q+", "exf8=Q+","Bb4+", "Kh5#"]),
            [1110044, 2110045, 1210063, 2220055, 1410041, 2410041, 1110068, 2110068, 1120068, 2310024, 1610085 ])


if __name__ == "__main__":
    unittest.main()
