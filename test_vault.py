import unittest
from vault_security import check_password

class TestVaultSecurity(unittest.TestCase):

    def test_password_length(self):
        self.assertFalse(check_password("abc"))  # massa curta

    def test_password_has_number(self):
        self.assertFalse(check_password("Password"))  # no té número

    def test_password_has_uppercase(self):
        self.assertFalse(check_password("password1"))  # no té majúscula

    def test_password_not_contains_admin(self):
        self.assertFalse(check_password("Admin1234"))  # conté 'admin'

    def test_password_valid(self):
        self.assertTrue(check_password("Secure123"))  # contrasenya bona


if __name__ == "__main__":
    unittest.main()
