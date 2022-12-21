import unittest
import smtplib
import OTP as OTP 
import Sender_data


class TestingOTPSender(unittest.TestCase):
    def assertBetween(self, x, low, hi):
        if not (low <= x <= hi):
            raise AssertionError(
                'Length of OTP should be in between %r and %r' % (low, hi))


    def test_generateOTP(self):
        size = 5

        otp = OTP.generateOTP(size)
    
        self.assertEqual(len(otp), size, 'OTP length does not match')
        self.assertBetween(len(otp), 4, 8)

 

    def test_validateEmail(self):
        receiver_email = 'username@domain.in'

        self.assertIn('@', receiver_email, "Email is not valid")
        self.assertIn('.in', receiver_email, "Email is not valid")


    def test_validateEmail2(self) :
        receiver_email = 'username@domain.com'

        self.assertIn('@', receiver_email, "Email is not valid")
        self.assertIn('.com', receiver_email, "Email is not valid")


    def test_sendOTP(self):
        otp = OTP.generateOTP(5)
        r_email = 'mendhenandini44@dbatu.ac.in'
        r_name='Nandini'
        self.assertBetween(len(otp), 4, 8)
        
        self.assertIn('@', r_email, "Email is not valid")
        self.assertIn('.in', r_email, "Email is not valid")

        OTP.send_email(r_name,r_email,otp) 


if __name__ == '__main__':
    unittest.main()
