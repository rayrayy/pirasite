import logging
import subprocess
import time
# import boot

logger = logging.getLogger(__name__)


class Error(Exception):
    pass


class ShutdownError(Error):
    pass


def shutdown():
    logger.info('Shutting down system')
    return _exec_shutdown(mode = "boot")


def restart():
    logger.info('Rebooting system')
    return _exec_shutdown(mode = "reboot")


def _exec_shutdown(mode):
    if mode == "reboot":
        try:
            result = subprocess.Popen('source app/boot.sh',
                                    # capture_output=True,
                                    # text=True,
                                    # check=True, 
                                    # shell=False,
                                    stdout = subprocess.PIPE, 
                                    stderr = subprocess.STDOUT,
                                    shell=True, 
                                    executable='/bin/bash')
        except subprocess.CalledProcessError as e:
            raise ShutdownError(e) from e
        # if 'failed' in result.stderr.lower():
        #     raise ShutdownError(result.stdout + result.stderr)

        if result.stdout:
            logger.info(result.stdout.read())
        if result.stderr:
            logger.info(result.stderr.read())
        time.sleep(5)
        try:
            result = subprocess.Popen('source app/boot.sh',
                                    # capture_output=True,
                                    # text=True,
                                    # check=True, 
                                    # shell=False,
                                    stdout = subprocess.PIPE, 
                                    stderr = subprocess.STDOUT,
                                    shell=True, 
                                    executable='/bin/bash')
        except subprocess.CalledProcessError as e:
            raise ShutdownError(e) from e
        # if 'failed' in result.stderr.lower():
        #     raise ShutdownError(result.stdout + result.stderr)

        if result.stdout:
            logger.info(result.stdout.read())
        if result.stderr:
            logger.info(result.stderr.read())
    if mode == "boot":
        try:
            result = subprocess.Popen('source app/boot.sh',
                                    # capture_output=True,
                                    # text=True,
                                    # check=True, 
                                    # shell=False,
                                    stdout = subprocess.PIPE, 
                                    stderr = subprocess.STDOUT,
                                    shell=True, 
                                    executable='/bin/bash')
        except subprocess.CalledProcessError as e:
            raise ShutdownError(e) from e
        # if 'failed' in result.stderr.lower():
        #     raise ShutdownError(result.stdout + result.stderr)

        if result.stdout:
            logger.info(result.stdout.read())
        if result.stderr:
            logger.info(result.stderr.read())
    return True