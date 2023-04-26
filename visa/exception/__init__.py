import os
import sys


class customException(Exception):
    def __init__(self, error_message: Exception, error_details:sys):
        super().__init__(error_message)
        self.error_message = customException.get_detaild_error_message(error_message = error_message,
                                                                      error_details= error_details)
        



        def get_detaild_error_message(self, error_message: Exception, error_details:sys)->str:
            _,_,exec_tb = error_details.exc_info()
            exception_block_line_number = exec_tb.tb_frame.f_lineno
            try_block_line_number = exec_tb.tb_lineno
            file_name = exec_tb.tb_frame.f_code.co_filename
            error_message = f"""
            error occured in script:
            [ {file_name}] at
            try block line number : [{try_block_line_number}] and exception block line number: [{exception_block_line_numbe}]
            error message =:[{error_message}]
            """
            
    def __str__(self):
        return self.error_message
    
    def __repr__(self) -> str:
        return customException.__name__.str()





            