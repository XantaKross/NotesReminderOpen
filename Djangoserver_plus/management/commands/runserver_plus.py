import atexit
from django.core.management.commands.runserver import Command as RunserverCommand
from Djangoserver_plus.signals import socket_ready


class Command(RunserverCommand):
    help = "Starts the Django development server with additional processes."

    def handle(self, *args, **options):
        # sends the socket_ready signal with the self.socket variable as a parameter.

        # Register the SocketClient to be disconnected on shutdown
        atexit.register(socket_ready.disconnect)

        super().handle(*args, **options)

        # If the server is shut down by a signal (e.g. Ctrl+C), terminate the processes and disconnect the socket
        socket_ready.disconnect()
