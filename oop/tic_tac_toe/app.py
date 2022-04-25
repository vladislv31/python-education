from controllers import Controller
from views import UnixTerminalView


view = UnixTerminalView()
controller = Controller(view)

controller.index()
