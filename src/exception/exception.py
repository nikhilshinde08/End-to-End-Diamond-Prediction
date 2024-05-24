
#please check sys model for checking the code functionalities

import sys

class CustomException(Exception):
    def __init__(self, error_message, error_details: sys):
        self.error_message = error_message
        _, _, exc_tb = error_details.exc_info()
        self.lineno = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return "Error occurred in Python script name [{0}] line number [{1}] error message: {2}".format(
            self.file_name, self.lineno, str(self.error_message))

def trigger_exception():
    """Function to trigger a division by zero exception."""
    a = 1 / 0

def main():
    """Main execution block."""
    try:
        trigger_exception()
    except Exception as e:
        raise CustomException(e, sys)

if __name__ == "__main__":
    main()
