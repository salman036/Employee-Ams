from attendance import db, app
from attendance.models import Company, User, Department, Timesheet


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'app': app, 'Company': Company, 'User': User, 'Department': Department, 'Timesheet': Timesheet}
