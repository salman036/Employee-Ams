class Constant(object):
    POST = 'POST'
    GET = 'GET'
    JPG = 'jpg'
    JPEG = 'jpeg'
    PNG = 'png'
    COMPANY_NAME_ALREADY_EXIST = 'Company name already exist'
    USERNAME_ALREADY_EXIST = 'This User Name is already exist'
    USERNAME_DOES_NOT_EXIST = 'This user name does not exist'
    REGISTER_SUCCESSFULLY = 'Register Successfully'
    SUCCESS_FLASH_MESSAGE = 'success'
    DANGER_FLASH_MESSAGE = 'danger'
    WARNING_FLASH_MESSAGE = 'warning'
    INFO_FLASH_MESSAGE = 'info'
    LOGIN_SUCCESSFULLY = 'Login Successfully'
    USER_NAME_OR_PASSWORD_INCORRECT = 'User Name or password incorrect'
    USER_ADDED_SUCCESSFULLY = "Added user successfully"
    UPDATE_USER_SUCCESSFULLY = "Update user Successfully"

    # Regular Expression Constant
    REGULAR_EXPRESSION_PASSWORD = "^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])(?=.{8,})"
    REGULAR_EXPRESSION_EMAIL = "^[a-z]{1,50}_?[0-9]{0,30}@gmail\.com$"
    REGULAR_PASSWORD_EXPRESSION_MESSAGE = "Minimum 8 characters, one uppercase," \
                                          "one lowercase, one number and one special character:"
    REGULAR_EXPRESSION_EMAIL_MESSAGE = "Email must be end with @gmail.com"
    ADMIN_ACCESS_MESSAGE = 'That api is only for Company Admin'
    DEPARTMENT_MESSAGE = 'Add Department Successfully'
    DEPARTMENT_ALREADY_EXIST = 'This department name is already exist'
    UPDATE_DEPARTMENT = 'Update department Successfully'
    DELETE_DEPARTMENT = 'Delete department Successfully'

    ALREADY_CHECK_IN = "Already check in"
    ALREADY_CHECK_OUT = "Already check out"
    FIRST_CHECK_IN_PLEASE = "First check in please"
    CHECK_OUT_SUCCESSFULLY = "Check out successfully"
    CHECK_IN_SUCCESSFULLY = "Check In successfully"
    EMAIL_ALREADY_EXIST = "This Email is already exist"
    RESET_PASSWORD_EMAIL_SEND = "An email has been sent with instructions to reset your password."
    EMAIL_DOES_NOT_EXIST = "Email does not exist"
    INVALID_TOKEN = "Invalid or expire token"
    RESET_PASSWORD = "Reset Password"
    PASSWORD_UPDATE = "Your password has been updated! You are now able to log in"
    SELECT_DEPARTMENT = 'Please select department'
    ATTENDANCE = 'Attendance'
    ATTENDANCE_RECORD = 'Attendance Record'
    DEPARTMENT = 'Departments'
    RESET_REQUEST = 'Reset Request'


class FormConstant(object):
    FULL_NAME = 'Full Name'
    NAME = 'Name'
    USER_NAME = 'User Name'
    EMAIL = 'EMAIL'
    DEPARTMENT = 'Department'
    EMPLOYEE_NUM = 'Employee Num'
    UPLOAD_IMAGE = 'Upload image'
    MEMO = 'Memo'
    PASSWORD = 'Password'
    CONFIRM_PASSWORD = 'Confirm Password'
    COMPANY = 'Company'
    SUBMIT = 'Submit'
    REGISTER = 'Register Now'
    CREATE = 'Create'
    LOGIN = 'Login'
    DIGIT_ID = 'Digit ID'
    ROLE = 'Role'
    UPDATE = 'Update'


class StackHolder(object):
    ADMIN = 'admin'
    EMPLOYEE = 'employee'


class FormTitlesConstant(object):
    UPDATE_DEPARTMENT = 'Update Department'
    CREATE_DEPARTMENT = 'Create Department'
    ADD_USER = 'Create User'
    REGISTER_COMPANY = 'Register Company'
    LOGIN = 'Login'
    ADD_DEPARTMENT = 'Add Department'
    ALL_DEPARTMENT = 'All Department'
    HOME = 'Home'
    UPDATE_USER = 'Update User'
