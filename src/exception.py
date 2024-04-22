import sys

class MyException(Exception):
    def __init__(self, message, error_detail:sys):
        super().__init__(message)
        self.message = error_message_details(message, error_detail)

    def __str__(self):
        return self.message
    
def error_message_details(error, error_detail:sys):
    _,_,tb = sys.exc_info()
    filename = tb.tb_frame.f_code.co_filename
    error_message = f"Error occured in scipt name {filename} line number {tb.tb_lineno} error message {str(error)} error details {str(error_detail)}"

    return error_message