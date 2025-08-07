import threading
from datetime import datetime
from django.contrib.auth import get_user_model
from django.conf import settings
from core.utils import send_html_email


def generate_password():
    return get_user_model().objects.make_random_password()


def generate_student_id():
    # Generate a username based on first and last name and registration date
    org_name="TNC"
    registered_year = datetime.now().strftime("%Y")
    students_count = get_user_model().objects.filter(is_trainee=True).count()
    return f"{org_name}-{settings.STUDENT_ID_PREFIX}-{registered_year}-{students_count}"


def generate_lecturer_id():
    # Generate a username based on first and last name and registration date
    org_name="TNC"
    registered_year = datetime.now().strftime("%Y")
    lecturers_count = get_user_model().objects.filter(is_instructor_examiner=True).count()
    return f"{org_name}-{settings.LECTURER_ID_PREFIX}-{registered_year}-{lecturers_count}"

def generate_operations_id():
    org_name="TNC"
    registered_year = datetime.now().strftime("%Y")
    operations_count = get_user_model().objects.filter(is_operations=True).count()
    return f"{org_name}-{settings.OPERATIONS_ID_PREFIX}-{registered_year}-{operations_count}"

# def generate_examiner_id():
#     org_name="TNC"
#     registered_year = datetime.now().strftime("%Y")
#     examiners_count = get_user_model().objects.filter(is_examiner=True).count()
#     return f"{org_name}-{settings.EXAMINER_ID_PREFIX}-{registered_year}-{examiners_count}"

def generate_student_credentials():
    return generate_student_id(), generate_password()

def generate_lecturer_credentials():
    return generate_lecturer_id(), generate_password()

def generate_operations_credentials():
    return generate_operations_id(), generate_password()

# def generate_examiner_credentials():
#     return generate_examiner_id(), generate_password()


class EmailThread(threading.Thread):
    def __init__(self, subject, recipient_list, template_name, context):
        self.subject = subject
        self.recipient_list = recipient_list
        self.template_name = template_name
        self.context = context
        threading.Thread.__init__(self)

    def run(self):
        send_html_email(
            subject=self.subject,
            recipient_list=self.recipient_list,
            template=self.template_name,
            context=self.context,
        )


def send_new_account_email(user, password):
    if user.is_trainee:
        template_name = "accounts/email/new_student_account_confirmation.html"
    elif user.is_instructor_examiner:
        template_name = "accounts/email/new_lecturer_account_confirmation.html"
    elif user.is_operations:
        template_name = "accounts/email/new_lecturer_account_confirmation.html"
    # elif user.is_examiner:
    #     template_name = "accounts/email/new_lecturer_account_confirmation.html"
    email = {
        "subject": "Your SkyLearn account confirmation and credentials",
        "recipient_list": [user.email],
        "template_name": template_name,
        "context": {"user": user, "password": password},
    }
    EmailThread(**email).start()
